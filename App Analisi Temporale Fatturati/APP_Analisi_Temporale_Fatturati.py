import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator, YearLocator
from PySide2.QtWidgets import (QApplication, QStyleFactory, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
                               QPushButton, QComboBox, QMessageBox, QFileDialog, QLabel, 
                               QDialog)
from PySide2.QtGui import QPalette, QColor, QFont, QIcon
from PySide2.QtCore import QSize
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import mplcursors

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafico Temporale Fatturati")
        self.setWindowIcon(QIcon("Plot.png"))
        self.init_ui()
        self.df = pd.DataFrame()
        self.filtered_df = pd.DataFrame()  
        self.date_col = None
        self.value_col = None

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        abbreviazioni_mesi = {
            1: 'Gen', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mag', 6: 'Giu', 7: 'Lug', 8: 'Ago',
            9: 'Set', 10: 'Ott', 11: 'Nov', 12: 'Dic'
        }

        # Inizializza PlotCanvas
        self.canvas = PlotCanvas(parent=self, abbreviazioni_mesi=abbreviazioni_mesi, width=12, height=6)
        main_layout.addWidget(self.canvas)

        # Aggiunge la barra degli strumenti per lo zoom
        toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(toolbar)

        # Layout per pulsanti e menu a tendina
        combined_layout = QHBoxLayout()

        # Pulsante di download CSV centrato
        self.download_button = QPushButton("Fatturati", self)
        self.download_button.setIcon(QIcon("CSV.png"))
        self.download_button.setIconSize(QSize(30, 30))
        self.download_button.setFont(QFont('Arial', 12))
        self.download_button.setFixedSize(110, 40)
        self.download_button.clicked.connect(self.download_csv)
        combined_layout.addStretch()
        combined_layout.addWidget(self.download_button)
        combined_layout.addStretch()

        # Menu a tendina per la selezione dell'anno
        self.year_dropdown = QComboBox(self)
        self.year_dropdown.setIconSize(QSize(24, 24))
        self.year_dropdown.setFixedSize(150, 40)
        self.year_dropdown.addItem(QIcon("tratta.png"), "Seleziona Anno")
        self.year_dropdown.currentTextChanged.connect(self.filter_by_year)
        combined_layout.addWidget(self.year_dropdown)

        # Aggiunge il pulsante "Mostra Tutto"
        self.show_all_button = QPushButton()
        self.show_all_button.setIcon(QIcon("annulla_filtro.png"))
        self.show_all_button.setIconSize(QSize(50, 50))
        self.show_all_button.setFixedSize(40, 40)
        self.show_all_button.setAutoDefault(True)
        self.show_all_button.clicked.connect(self.show_all_years)
        combined_layout.addWidget(self.show_all_button)

        # Aggiunge il pulsante "Carica Fonte"
        self.load_source_button = QPushButton()
        self.load_source_button.setIcon(QIcon("dato.png"))
        self.load_source_button.setIconSize(QSize(40, 40))
        self.load_source_button.setFixedSize(40, 40)
        self.load_source_button.setAutoDefault(True)
        self.load_source_button.clicked.connect(self.load_data_source)
        combined_layout.addWidget(self.load_source_button)

        main_layout.addLayout(combined_layout)

    def filter_by_year(self, selected_year):
        if selected_year.isdigit() and not self.df.empty:
            self.filtered_df = self.df[self.df[self.date_col].dt.year == int(selected_year)]
            self.canvas.update_plot(self.filtered_df, self.date_col, self.value_col)

    def show_all_years(self):
        self.year_dropdown.setCurrentIndex(0)  
        self.filtered_df = self.df
        self.canvas.update_plot(self.df, self.date_col, self.value_col)

    def download_csv(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Salva Dati", "", "CSV Files (*.csv)")
        if file_path and not self.df.empty:
            # Usa i dati filtrati se disponibili, altrimenti usa l'intero dataset
            data_to_use = self.filtered_df if not self.filtered_df.empty else self.df
            # Calcola i fatturati totali per mese e anno
            monthly_totals = data_to_use.resample('M', on=self.date_col).sum()[self.value_col]
            monthly_totals.index = monthly_totals.index.to_period('M')
            monthly_totals = monthly_totals.reset_index()
            monthly_totals.columns = ['Data', 'Fatturato Totale']
            # Salva in CSV
            monthly_totals['Fatturato Totale'] = monthly_totals['Fatturato Totale'].astype(int)
            monthly_totals.to_csv(file_path, index=False)
            self.show_message("I dati dei fatturati totali per mese e anno sono stati scaricati correttamente!", "Download Completato")
        else:
            self.show_message("Il download è stato annullato.", "Download Annullato")

    def load_data_source(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Carica Fonte Dati", "", "Files (*.csv *.xlsx)")
        if file_path:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                self.show_message("Formato di file non supportato.", "Errore")
                return

            # Mostra i dialoghi di selezione delle colonne
            self.show_column_selection_dialog(df)

    def show_column_selection_dialog(self, df):
        dialog = ColumnSelectionDialog(df, self)
        if dialog.exec_() == QDialog.Accepted:
            self.date_col = dialog.date_column
            self.value_col = dialog.value_column
            df[self.date_col] = pd.to_datetime(df[self.date_col], errors='coerce')
            self.df = df.dropna(subset=[self.date_col, self.value_col])
            self.filtered_df = self.df  
            self.canvas.load_external_data(self.df, self.date_col, self.value_col)
            self.populate_year_dropdown(self.df)

    def populate_year_dropdown(self, df):
        self.year_dropdown.clear()
        self.year_dropdown.addItem(QIcon("tratta.png"), "Seleziona Anno")
        years = df[self.date_col].dt.year.unique()
        for year in sorted(years):
            self.year_dropdown.addItem(str(year))

    def show_message(self, message, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QIcon("Plot.png"))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

class ColumnSelectionDialog(QDialog):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Seleziona Colonne")
        self.df = df
        self.date_column = None
        self.value_column = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.date_label = QLabel("Seleziona la colonna della data:")
        self.date_combobox = QComboBox()
        self.date_combobox.addItems(self.df.columns)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_combobox)

        self.value_label = QLabel("Seleziona la colonna dei valori:")
        self.value_combobox = QComboBox()
        self.value_combobox.addItems(self.df.columns)
        layout.addWidget(self.value_label)
        layout.addWidget(self.value_combobox)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Annulla")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def accept(self):
        self.date_column = self.date_combobox.currentText()
        self.value_column = self.value_combobox.currentText()
        super().accept()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, abbreviazioni_mesi=None, width=5, height=4, dpi=100):
        self.abbreviazioni_mesi = abbreviazioni_mesi
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)
        self.totali_lordi_per_mese = pd.Series(dtype='float64')

        # Imposta il colore di sfondo solo per l'area degli Assi
        self.ax.set_facecolor('#E6EAF0')

        # Inizialmente mostra tutti i dati
        self.update_plot(pd.DataFrame(), None, None)

    def update_plot(self, df, date_col, value_col):
        if not df.empty and date_col and value_col:
            try:
                df.set_index(pd.to_datetime(df[date_col], errors='coerce'), inplace=True)
                df.dropna(subset=[date_col, value_col], inplace=True)
                self.totali_lordi_per_mese = df[value_col].resample('M').sum()

                # Pulisce e ri-disegna
                self.ax.clear()
                self.ax.fill_between(self.totali_lordi_per_mese.index, self.totali_lordi_per_mese.values, color='Navy', alpha=0.5)

                # Aggiunge marcatori solo per i valori non zero
                non_zero_mask = self.totali_lordi_per_mese > 0
                scatter = self.ax.plot(self.totali_lordi_per_mese.index[non_zero_mask], self.totali_lordi_per_mese.values[non_zero_mask], 'o', color='Navy', markersize=3.4)

                # Aggiunge il cursore con etichette
                cursor = mplcursors.cursor(scatter, hover=True, multiple=True)
                @cursor.connect("add")
                def on_add(sel):
                    sel.annotation.set_text(f'€{sel.target[1]:.2f}')
                    sel.annotation.draggable(True)  

                self.ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
                self.ax.xaxis.set_minor_locator(MonthLocator())
                self.ax.xaxis.set_major_formatter(DateFormatter("%Y"))
                self.ax.xaxis.set_major_locator(YearLocator())
                self.ax.spines['top'].set_visible(False)
                self.ax.spines['right'].set_visible(False)
                self.ax.spines['left'].set_visible(False)
                self.ax.spines['bottom'].set_visible(False)

                # Aggiunge le etichette dei mesi in italiano sopra l'asse x
                self.ax.xaxis.set_tick_params(pad=15)
                for label in self.ax.get_xticklabels(minor=True):
                    label.set_rotation(0)
                    label.set_verticalalignment('bottom')
                    label.set_horizontalalignment('center')

                # Aggiunge le etichette dei mesi in italiano sopra l'asse x
                for date in self.totali_lordi_per_mese.index:
                    month_name = self.abbreviazioni_mesi[date.month]
                    self.ax.text(date, -0.05, month_name, ha='center', va='bottom', fontsize=6.6, fontweight='bold', color='black', rotation=45, transform=self.ax.get_xaxis_transform())

                # Distanzia le etichette degli anni verso il basso
                self.ax.xaxis.set_tick_params(which='major', pad=20)

                # Aggiorna il canvas
                self.draw()
            except KeyError as e:
                QMessageBox.critical(self, "Errore", f"Errore nell'aggiornare il grafico: {str(e)}")
                return

    def load_external_data(self, df, date_col, value_col):
        self.update_plot(df, date_col, value_col)

# Avvia l'applicazione
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MyMainWindow()
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(119, 136, 153))
    palette.setColor(QPalette.Highlight, QColor(176, 196, 222))
    palette.setColor(QPalette.HighlightedText, QColor(64, 64, 64))
    palette.setColor(QPalette.WindowText, QColor(64, 64, 64))
    palette.setColor(QPalette.Button, QColor(200, 200, 200))
    palette.setColor(QPalette.ButtonText, QColor(64, 64, 64))
    palette.setColor(QPalette.AlternateBase, QColor(240, 248, 255))
    window.setPalette(palette)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
