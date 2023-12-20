import sys
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget, QStyleFactory
from PySide2.QtGui import QIcon, QPalette, QColor, QFont



class Applicazione(QWidget):
    def __init__(self):
        super().__init__()

        app_icon = QIcon("python.jpg")
        self.setWindowIcon(app_icon)

        self.setWindowTitle('APP-ASSET')
        self.setGeometry(890, 40, 400, 500)

        self.labely = QLabel('\n')
        self.labely.setIndent(150)

        # Aggiungi label e combobox per SFRUTTABILE DA PARTE DEGLI UTENTI
        self.label1 = QLabel('SCEGLIERE ASSET')
        font1 = QFont('Courier New', 9)
        self.label1.setFont(font1)
        self.label1.setIndent(280)
        self.comboBox1 = QComboBox()
        fontA = QFont('Comic Sans MS', 8)
        self.comboBox1.setFont(fontA)
        self.comboBox1.addItem('CRITICAL')
        self.comboBox1.addItem('SENSITIVE')
        self.comboBox1.addItem('RELEVANT')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox1.setPalette(palette)

        # Aggiungi label e combobox per SFRUTTABILE DA PARTE DEGLI UTENTI
        self.label2 = QLabel('SCEGLIERE SEVERITY')
        font2 = QFont('Courier New', 9)
        self.label2.setFont(font2)
        self.label2.setIndent(280)
        self.comboBox2 = QComboBox()
        fontB = QFont('Comic Sans MS', 8)
        self.comboBox2.setFont(fontB)
        self.comboBox2.addItem('CRITICAL')
        self.comboBox2.addItem('MEDIUM')
        self.comboBox2.addItem('HIGH')
        self.comboBox2.addItem('LOW')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox2.setPalette(palette)

        # Aggiungi label e combobox per SFRUTTABILE DA PARTE DEGLI UTENTI
        self.label3 = QLabel('SFRUTTABILE DA PARTE DEGLI UTENTI')
        font3 = QFont('Courier New', 9)
        self.label3.setFont(font3)
        self.comboBox3 = QComboBox()
        fontC = QFont('Comic Sans MS', 8)
        self.comboBox3.setFont(fontC)
        self.comboBox3.addItem('SOLO DA DIPENDENTI')
        self.comboBox3.addItem('ANCHE DA PARTNER')
        self.comboBox3.addItem('CLIENTE')
        self.comboBox3.addItem('IMPROBABILE')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox3.setPalette(palette)

        # Aggiungi label e combobox per EPSS'
        self.label4 = QLabel("EPSS")
        font4 = QFont('Courier New', 9)
        self.label4.setFont(font4)
        self.comboBox4 = QComboBox()
        fontD = QFont('Comic Sans MS', 8)
        self.comboBox4.setFont(fontD)
        self.comboBox4.addItem('<= 3 %')
        self.comboBox4.addItem('3 - 20 %')
        self.comboBox4.addItem('> 20 %')
        self.comboBox4.addItem('N/A')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox4.setPalette(palette)

        # Aggiungi label e combobox per SFRUTTABILITA'
        self.label5 = QLabel("SFRUTTABILITA' NEL CONTESTO")
        font5 = QFont('Courier New', 9)
        self.label5.setFont(font5)
        self.comboBox5 = QComboBox()
        fontE = QFont('Comic Sans MS', 8)
        self.comboBox5.setFont(fontE)
        self.comboBox5.addItem('ALTO')
        self.comboBox5.addItem('BASSO')
        self.comboBox5.addItem('NULLO')
        self.comboBox5.addItem('SCONOSCIUTO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox5.setPalette(palette)

        # Aggiungi label e combobox per EXPLOIT
        self.label6 = QLabel('EXPLOIT PUBBLICO')
        font6 = QFont('Courier New', 9)
        self.label6.setFont(font6)
        self.comboBox6 = QComboBox()
        fontF = QFont('Comic Sans MS', 8)
        self.comboBox6.setFont(fontF)
        self.comboBox6.addItem('SI')
        self.comboBox6.addItem('PoC')
        self.comboBox6.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox6.setPalette(palette)

        # Aggiungi label e combobox per fix
        self.label7 = QLabel('FIX UFFICIALI O RICONOSCIUTE')
        font7 = QFont('Courier New', 9)
        self.label7.setFont(font7)
        self.comboBox7 = QComboBox()
        fontG = QFont('Comic Sans MS', 8)
        self.comboBox7.setFont(fontG)
        self.comboBox7.addItem('SI')
        self.comboBox7.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox7.setPalette(palette)

        # Aggiungi label e combobox per MITIGAZIONE
        self.label8 = QLabel('MITIGAZIONE')
        font8 = QFont('Courier New', 9)
        self.label8.setFont(font8)
        self.comboBox8 = QComboBox()
        fontH = QFont('Comic Sans MS', 8)
        self.comboBox8.setFont(fontH)
        self.comboBox8.addItem('EFFICACE')
        self.comboBox8.addItem('PARZIALMENTE EFFICACE')
        self.comboBox8.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox8.setPalette(palette)

        # Aggiungi label e combobox per RISCHIO FRODE
        self.label9 = QLabel('RISCHIO FRODE')
        font9 = QFont('Courier New', 9)
        self.label9.setFont(font9)
        self.comboBox9 = QComboBox()
        fontI = QFont('Comic Sans MS', 8)
        self.comboBox9.setFont(fontI)
        self.comboBox9.addItem('SI')
        self.comboBox9.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox9.setPalette(palette)

         # Aggiungi label e combobox per EVENTI SICUREZZA
        self.label10 = QLabel('EVENTI DI SICUREZZA RILEVATI')
        font10 = QFont('Courier New', 9)
        self.label10.setFont(font10)
        self.comboBox10 = QComboBox()
        fontL = QFont('Comic Sans MS', 8)
        self.comboBox10.setFont(fontL)
        self.comboBox10.addItem('SI')
        self.comboBox10.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox10.setPalette(palette)

         # Aggiungi label e combobox per EVENTI SICUREZZA
        self.label11 = QLabel('TENTATIVI DI SFRUTTAMENTO PASSATI')
        font11 = QFont('Courier New', 9)
        self.label11.setFont(font11)
        self.comboBox11 = QComboBox()
        fontM = QFont('Comic Sans MS', 8)
        self.comboBox11.setFont(fontM)
        self.comboBox11.addItem('SI')
        self.comboBox11.addItem('NO')
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 191, 255))
        self.comboBox11.setPalette(palette)


        # Aggiungi bottone per confermare le scelte
        self.button = QPushButton('Conferma')
        font10 = QFont('Impact', 12)
        self.button.setFont(font10)
        self.button.setDefault(True) # Imposta il pulsante come predefinito
        self.button.clicked.connect(self.calcola_applicazione)

        # Aggiungi label per il risultato del questionario
        self.label_result = QLabel()
        self.label_risultato = QLabel()

        # Aggiungi i widget al layout
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.comboBox1)
        layout.addWidget(self.label2)
        layout.addWidget(self.comboBox2)
        layout.addWidget(self.label3)
        layout.addWidget(self.comboBox3)
        layout.addWidget(self.label4)
        layout.addWidget(self.comboBox4)
        layout.addWidget(self.label5)
        layout.addWidget(self.comboBox5)
        layout.addWidget(self.label6)
        layout.addWidget(self.comboBox6)
        layout.addWidget(self.label7)
        layout.addWidget(self.comboBox7)
        layout.addWidget(self.label8)
        layout.addWidget(self.comboBox8)
        layout.addWidget(self.label9)
        layout.addWidget(self.comboBox9)
        layout.addWidget(self.label10)
        layout.addWidget(self.comboBox10)
        layout.addWidget(self.label11)
        layout.addWidget(self.comboBox11)
        layout.addWidget(self.labely)
        layout.addWidget(self.button)
        layout.addWidget(self.label_result)
        layout.addWidget(self.label_risultato)
        
        self.setLayout(layout)

    def calcola_applicazione(self):
    # Ottieni il valore selezionato per ogni combobox
        asset = self.comboBox1.currentText()
        severity = self.comboBox2.currentText()
        tipo_utente = self.comboBox3.currentText()
        epss = self.comboBox4.currentText()
        sfruttabilita = self.comboBox5.currentText()
        exploit = self.comboBox6.currentText()
        fix = self.comboBox7.currentText()
        mitigazione = self.comboBox8.currentText()
        rischio_frode = self.comboBox9.currentText()
        eventi_sicurezza = self.comboBox10.currentText()
        tentativi_passati = self.comboBox11.currentText()
    # Esegui la logica di calcolo del risultato del questionario
    # In questo esempio, calcoliamo il punteggio come la somma dei valori numerici
    # assegnati alle risposte date alle domande
        punteggio = 0
        
        if asset == 'CRITICAL':
            punteggio += 3
        elif asset == 'SENSITIVE':
            punteggio += 2
        elif asset == 'RELEVANT':
            punteggio += 0

        if severity == 'CRITICAL':
            punteggio += 3
        elif severity == 'HIGH':
            punteggio += 2
        elif severity == 'MEDIUM':
            punteggio += 1
        elif severity == 'LOW':
            punteggio += 0

        #   QUESTIONARIO

        if tipo_utente == 'SOLO DA DIPENDENTI':
            punteggio += 0
        elif tipo_utente == 'ANCHE DA PARTNER':
            punteggio += 0.5
        elif tipo_utente == 'CLIENTE':
            punteggio += 0.5
        elif tipo_utente == 'IMPROBABILE':
            punteggio += -0.5

        if epss == '<= 3 %':
            punteggio += -1.5
        elif epss == '3 - 20 %':
            punteggio += 0.5
        elif epss == '> 20 %':
            punteggio += 1
        elif epss == 'N/A':
            punteggio += 0

        if sfruttabilita == 'ALTO':
            punteggio += 1
        elif sfruttabilita == 'BASSO':
            punteggio += -0.5
        elif sfruttabilita == 'NULLO':
            punteggio += -1.5
        elif sfruttabilita == 'SCONOSCIUTO':
            punteggio += 0

        if exploit == 'SI':
            punteggio += 1
        elif exploit == 'PoC':
            punteggio += 0.5
        elif exploit == 'NO':
            punteggio += 0

        if fix == 'SI':
            punteggio += 0
        elif fix == 'NO':
            punteggio += 1

        if mitigazione == 'EFFICACE':
            punteggio += -1
        elif mitigazione == 'PARZIALMENTE EFFICACE':
            punteggio += -0.5
        elif mitigazione == 'NO':
            punteggio += 0

        if rischio_frode == 'SI':
            punteggio += 0.5
        elif rischio_frode == 'NO':
            punteggio += 0

        if eventi_sicurezza == 'SI':
            punteggio += 0.5
        elif eventi_sicurezza == 'NO':
            punteggio += 0

        if tentativi_passati == 'SI':
            punteggio += 1
        elif tentativi_passati == 'NO':
            punteggio += 0

        risultato = ''

        if asset == 'CRITICAL':
            if punteggio <= 3 or punteggio == 3.5:
                risultato += "CRITICAL-LOW -----> INTERVENTO 90 GIORNI"
            elif punteggio == 4 or punteggio == 4.5:
                risultato += "CRITICAL-MEDIUM -----> INTERVENTO 45 GIORNI"
            elif punteggio == 5 or punteggio == 5.5:
                risultato += "CRITICAL-HIGH -----> INTERVENTO 15 GIORNI"
            elif punteggio >= 6:
                risultato += "CRITICAL-CRITICAL -----> INTERVENTO 7 GIORNI"
        elif asset == 'SENSITIVE':
            if punteggio == 2.5 or punteggio < 2:
                risultato += "SENSITIVE-LOW -----> ACCEPTANCE OR DELAYED PLANNING OR BEST-EFFORT"
            elif punteggio == 3 or punteggio == 3.5:
                risultato += "SENSITIVE-MEDIUM -----> INTERVENTO 70 GIORNI"
            elif punteggio == 4 or punteggio == 4.5:
                risultato += "SENSITIVE-HIGH -----> INTERVENTO 45 GIORNI"
            elif punteggio >= 5:
                risultato += "SENSITIVE-CRITICAL -----> INTERVENTO 15 GIORNI"
        elif asset == 'RELEVANT':
            if punteggio <= 0 or punteggio == 0.5:
                risultato += "RELEVANT-LOW -----> ACCEPTANCE OR DELAYED PLANNING OR BEST-EFFORT"
            elif punteggio == 1 or punteggio == 1.5:
                risultato += "RELEVANT-MEDIUM -----> ACCEPTANCE OR DELAYED PLANNING OR BEST-EFFORT"
            elif punteggio == 2 or punteggio == 2.5:
                risultato += "RELEVANT-HIGH -----> INTERVENTO 70 GIORNI"
            elif punteggio >= 3:
                risultato += "RELEVANT-CRITICAL -----> INTERVENTO 45 GIORNI"


       

    # Mostra il risultato del questionario nella label dedicata
        self.label_result.setText(f"RISULTATO RATING: {punteggio}")
        fontJ = QFont('Courier New', 9)
        self.label_result.setFont(fontJ)
        self.label_result.setIndent(125)

        self.label_risultato.setText(f"{risultato}")
        fontK = QFont('Courier New', 9)
        self.label_risultato.setFont(fontK)
        self.label_risultato.setIndent(1)

        #Crea l'applicazione e mostra la finestra del questionario
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = Applicazione()
    palette = QPalette()
# Impostazione del colore di sfondo della finestra
    palette.setColor(QPalette.Window, QColor(245, 245, 220)) 
    palette.setColor(QPalette.Highlight, QColor(255, 192, 203))
    palette.setColor(QPalette.HighlightedText, QColor(128, 0, 128))
    palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    palette.setColor(QPalette.Button, QColor(207, 181, 59))
    palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    palette.setColor(QPalette.AlternateBase, QColor(64, 64, 64))  
# Impostazione del palette della finestra
    window.setPalette(palette)
    
    
    window.adjustSize()
    window.button.setFocus() # Imposta il focus sul pulsante
    window.show()
    sys.exit(app.exec_())

