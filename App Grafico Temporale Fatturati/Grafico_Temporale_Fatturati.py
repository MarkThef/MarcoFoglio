import sys
import pandas as pd
import matplotlib.pyplot as plt
from PySide2.QtWidgets import (QApplication, QStyleFactory, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
                               QPushButton, QComboBox, QMessageBox, QFileDialog, QLabel, 
                               QDialog, QFrame)
from PySide2.QtGui import QPalette, QColor, QFont, QIcon, QLinearGradient, QBrush
from PySide2.QtCore import QSize, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class CustomButton(QPushButton):
    def __init__(self, text="", icon=None, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont('Segoe UI', 10))
        self.setFixedSize(130, 40)
        self.setIconSize(QSize(24, 24))
        if icon:
            self.setIcon(QIcon(icon))
        self.setStyleSheet("""
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #3a7abd;
            }
            QPushButton:pressed {
                background-color: #2a5a9d;
            }
        """)

class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont('Segoe UI', 10))
        self.setFixedSize(150, 40)
        self.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #4a90e2;
                border-radius: 5px;
                padding: 5px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left-width: 1px;
                border-left-color: #4a90e2;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            QComboBox::down-arrow {
                image: url(dropdown_arrow.png);
            }
        """)

class CustomNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent, coordinates=True):
        NavigationToolbar.__init__(self, canvas, parent, coordinates)
        self.setStyleSheet("""
            QToolBar {
                background-color: transparent;
                border: none;
            }
            QToolButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 5px;
                margin: 2px;
            }
            QToolButton:hover {
                background-color: #3a7abd;
            }
            QToolButton:pressed {
                background-color: #2a5a9d;
            }
        """)
        
        # Rimuovi tutti i pulsanti esistenti
        for action in self.actions():
            self.removeAction(action)
        
        # Aggiungi solo i pulsanti necessari
        self.addAction(self._actions['home'])
        self.addAction(self._actions['back'])
        self.addAction(self._actions['forward'])
        self.addSeparator()
        self.addAction(self._actions['pan'])
        self.addAction(self._actions['zoom'])
        self.addSeparator()
        self.addAction(self._actions['save_figure'])

        # Personalizza le icone
        self._actions['home'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//reset.png'))
        self._actions['back'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//sinistra.png'))
        self._actions['forward'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//destra.png'))
        self._actions['pan'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//trascina.png'))
        self._actions['zoom'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//zoom.png'))
        self._actions['save_figure'].setIcon(QIcon('App Grafico Temporale Fatturati//immagini//fotografia.png'))

    def set_message(self, s):
        pass

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grafico Temporale Fatturati")
        self.setWindowIcon(QIcon("App Grafico Temporale Fatturati//immagini//Plot.png"))
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

        # Add a title label
        title_label = QLabel("Grafico Temporale Fatturati")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Segoe UI', 18, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50; margin: 10px 0;")
        main_layout.addWidget(title_label)

        abbreviazioni_mesi = {
            1: 'Gen', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mag', 6: 'Giu', 7: 'Lug', 8: 'Ago',
            9: 'Set', 10: 'Ott', 11: 'Nov', 12: 'Dic'
        }

        # Create a frame for the plot
        plot_frame = QFrame()
        plot_frame.setFrameShape(QFrame.StyledPanel)
        plot_frame.setStyleSheet("background-color: white; border-radius: 10px;")
        plot_layout = QVBoxLayout(plot_frame)

        self.canvas = PlotCanvas(parent=self, abbreviazioni_mesi=abbreviazioni_mesi, width=12, height=6)
        plot_layout.addWidget(self.canvas)

        self.toolbar = CustomNavigationToolbar(self.canvas, self)
        plot_layout.addWidget(self.toolbar)

        main_layout.addWidget(plot_frame)

        # Control panel
        control_panel = QFrame()
        control_panel.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
        control_layout = QHBoxLayout(control_panel)

        # Left side - Download CSV button
        left_layout = QHBoxLayout()
        self.download_button = CustomButton("Fatturati", "App Grafico Temporale Fatturati//immagini//CSV.png")
        self.download_button.clicked.connect(self.download_csv)
        left_layout.addWidget(self.download_button)
        left_layout.addStretch()  # This pushes the button to the left

        # Right side - Year dropdown, Show all button, Load source button
        right_layout = QHBoxLayout()
        self.year_dropdown = CustomComboBox(self)
        self.year_dropdown.addItem(QIcon("App Grafico Temporale Fatturati//immagini//tratta.png"), "Seleziona Anno")
        self.year_dropdown.currentTextChanged.connect(self.filter_by_year)
        right_layout.addWidget(self.year_dropdown)

        self.show_all_button = CustomButton("", "App Grafico Temporale Fatturati//immagini//annulla_filtro.png")
        self.show_all_button.setFixedSize(40, 40)
        self.show_all_button.clicked.connect(self.show_all_years)
        right_layout.addWidget(self.show_all_button)

        self.load_source_button = CustomButton("", "App Grafico Temporale Fatturati//immagini//dato.png")
        self.load_source_button.setFixedSize(40, 40)
        self.load_source_button.clicked.connect(self.load_data_source)
        right_layout.addWidget(self.load_source_button)

        # Add left and right layouts to the main control layout
        control_layout.addLayout(left_layout)
        control_layout.addStretch()  # This creates space between left and right sides
        control_layout.addLayout(right_layout)

        main_layout.addWidget(control_panel)

    def filter_by_year(self, selected_year):
        if selected_year.isdigit() and not self.df.empty:
            self.filtered_df = self.df[self.df[self.date_col].dt.year == int(selected_year)]
            self.canvas.update_plot(self.filtered_df, self.date_col, self.value_col)

    def show_all_years(self):
        self.year_dropdown.setCurrentIndex(0)  # Reset dropdown selection
        self.filtered_df = self.df
        self.canvas.update_plot(self.df, self.date_col, self.value_col)

    def download_csv(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Salva Dati", "", "CSV Files (*.csv)")
        if file_path and not self.df.empty:
            data_to_use = self.filtered_df if not self.filtered_df.empty else self.df
            monthly_totals = data_to_use.resample('M', on=self.date_col).sum()[self.value_col]
            monthly_totals.index = monthly_totals.index.to_period('M')
            monthly_totals = monthly_totals.reset_index()
            monthly_totals.columns = ['Data', 'Fatturato Totale']
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
        self.year_dropdown.addItem(QIcon("App Grafico Temporale Fatturati//immagini//tratta.png"), "Seleziona Anno")
        years = df[self.date_col].dt.year.unique()
        for year in sorted(years):
            self.year_dropdown.addItem(str(year))

    def show_message(self, message, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QIcon("App Grafico Temporale Fatturati//immagini//Plot.png"))
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

        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
                color: #2c3e50;
            }
            QComboBox {
                background-color: white;
                border: 1px solid #4a90e2;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #3a7abd;
            }
        """)

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

        self.fig.patch.set_facecolor('#f0f0f0')
        self.ax.set_facecolor('#ffffff')

        # Colori per gli anni (palette più adatta per distinguere gli anni)
        self.colors = [
            '#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6', 
            '#1abc9c', '#e67e22', '#34495e', '#16a085', '#c0392b'
        ]

        self.update_plot(pd.DataFrame(), None, None)

    def update_plot(self, df, date_col, value_col):
        if not df.empty and date_col and value_col:
            try:
                # Crea una copia del DataFrame all'inizio
                working_df = df.copy()
            
                # Prepara i dati
                working_df[date_col] = pd.to_datetime(working_df[date_col])
                working_df['Year'] = working_df[date_col].dt.year
                working_df['Month'] = working_df[date_col].dt.month
            
                # Pivot dei dati con mesi come indice e anni come colonne
                pivot_df = working_df.pivot_table(
                    values=value_col,
                    index='Month',
                    columns='Year',
                    aggfunc='sum',
                    fill_value=0
                )

                # Assicurati che tutti i mesi siano presenti
                for month in range(1, 13):
                    if month not in pivot_df.index:
                        pivot_df.loc[month] = 0
                pivot_df = pivot_df.sort_index()

                # Clear the axis
                self.ax.clear()

                # Crea il grafico ad aree impilate
                x = range(1, 13)  # Mesi da 1 a 12
                years = sorted(pivot_df.columns)
            
                # Disegna le aree impilate
                self.ax.stackplot(
                    x,
                    [pivot_df[year] for year in years],
                    labels=years,
                    colors=self.colors[:len(years)],
                    alpha=0.7
                )

                # Personalizza il grafico
                self.ax.set_facecolor('#ffffff')
                self.ax.grid(True, linestyle='--', linewidth=0.5, color='#bdc3c7', alpha=0.5)
            
                # Nascondi i bordi
                for spine in self.ax.spines.values():
                    spine.set_visible(False)

                # Imposta i label dei mesi sull'asse X
                self.ax.set_xticks(range(1, 13))
                self.ax.set_xticklabels(
                    [self.abbreviazioni_mesi[i] for i in range(1, 13)],
                    rotation=0,
                    fontsize=10
                )

                # Formatta gli assi
                self.ax.set_xlabel('Mese', fontsize=12, color='#2c3e50', fontweight='bold')
                self.ax.set_ylabel('Fatturato', fontsize=12, color='#2c3e50', fontweight='bold')

                # Aggiungi la legenda degli anni
                legend = self.ax.legend(
                    title='Anni',
                    loc='upper left',
                    bbox_to_anchor=(1, 1),
                    fontsize=9,
                    title_fontsize=10
                )
                legend.get_frame().set_facecolor('#ffffff')
                legend.get_frame().set_alpha(0.9)
                legend.get_frame().set_edgecolor('#bdc3c7')

                # Formatta i valori sull'asse y
                def format_func(value, _):
                    if value >= 1e6:
                        return f'€{value/1e6:.1f}M'
                    elif value >= 1e3:
                        return f'€{value/1e3:.0f}K'
                    else:
                        return f'€{value:.0f}'

                self.ax.yaxis.set_major_formatter(plt.FuncFormatter(format_func))

                # Aggiungi titolo
                self.ax.set_title(
                    'Fatturati Mensili per Anno', 
                    fontsize=16, 
                    fontweight='bold', 
                    color='#2c3e50', 
                    pad=20
                )

                # Aggiusta il layout per la legenda
                self.fig.tight_layout()

                # Funzione per gestire l'interattività
                def on_motion(event):
                    if event.inaxes == self.ax:
                        x_val = event.xdata
                        if x_val is not None and 1 <= x_val <= 12:
                            # Trova il mese più vicino
                            month_idx = int(round(x_val)) - 1
                            month = month_idx + 1
                        
                            # Rimuovi le annotazioni precedenti
                            for artist in self.ax.texts:
                                if hasattr(artist, 'is_tooltip'):
                                    artist.remove()
                        
                            # Calcola i valori per ogni anno
                            monthly_values = []
                            total = 0
                            for year in years:
                                value = pivot_df.loc[month, year]
                                total += value
                                if value > 0:  # Mostra solo gli anni con valori positivi
                                    monthly_values.append(f"{year}: €{value:,.2f}")
                        
                            # Crea il testo del tooltip
                            tooltip_text = f"Mese: {self.abbreviazioni_mesi[month]}\n"
                            tooltip_text += "\n".join(monthly_values)
                            tooltip_text += f"\nTotale: €{total:,.2f}"
                        
                            # Posiziona il tooltip
                            y_pos = pivot_df.loc[month].sum() / 2
                            tooltip = self.ax.annotate(
                                tooltip_text,
                                xy=(month, y_pos),
                                xytext=(10, 10),
                                textcoords='offset points',
                                bbox=dict(
                                    boxstyle='round,pad=0.5',
                                    fc='white',
                                    alpha=0.9,
                                    ec='#bdc3c7'
                                ),
                                zorder=5,
                                fontsize=9
                            )
                            tooltip.is_tooltip = True
                        
                            # Aggiorna il canvas
                            self.draw_idle()

                # Connetti l'evento di movimento del mouse
                self.mpl_connect('motion_notify_event', on_motion)

                # Aggiorna il canvas
                self.draw()

            except Exception as e:
                QMessageBox.critical(
                    self.parent(),
                    "Errore",
                    f"Errore nell'aggiornare il grafico: {str(e)}"
                )
                return

    def load_external_data(self, df, date_col, value_col):
        self.update_plot(df, date_col, value_col)

# Start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MyMainWindow()
    
    # Set a gradient background for the main window
    gradient = QLinearGradient(0, 0, 0, window.height())
    gradient.setColorAt(0, QColor("#ecf0f1"))
    gradient.setColorAt(1, QColor("#bdc3c7"))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(gradient))
    
    window.setPalette(palette)
    window.show()
    sys.exit(app.exec_())