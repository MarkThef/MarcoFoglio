# 1

# Esercizio
# Abbiamo una lista di numeri:

numeri = [4, 10, 50, 100, 128, 71, 46]

# creare una nuova lista i cui elementi siano gli stessi di numeri incrementati di 10,
# mediante comprehension.


nuova_lista = [n + 10 for n in numeri]

print(nuova_lista)

# 2

# Esercizio
# Abbiamo una lista di numeri:

numeri = [4, 10, 50, 100, 128, 71, 46]

# creare una nuova lista i cui elementi siano gli stessi di numeri ma raddoppiati,
# mediante comprehension.

nuova_lista = [n * 2 for n in numeri]

print(nuova_lista)

# 3

# Esercizio
# Abbiamo una lista di nomi:

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry"]

# creare una nuova lista i cui elementi siano le iniziali dei nomi, mediante
# comprehension.

nuova_lista = [n[0] for n in nomi]

print(nuova_lista)

# 4

# Esercizio
# Abbiamo una lista di nomi:

nomi = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry"]

# creare una nuova lista i cui elementi siano le iniziali dei nomi seguite da punto,
# mediante comprehension.

nuova_lista = [n[0] + '.' for n in nomi]

print(nuova_lista)

# 5

# Esercizio
# Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

# Creare una lista che contenga (per ogni CF) solo i caratteri relativi al nome,
# mediante comprehension

nuova_lista = [n[0:6] for n in lista_cf]

print(nuova_lista)

# 6

# Esercizio
# Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

# Creare due liste, una che contenga (per ogni CF) solo i caratteri relativi al nome,
# e una che contenga (per ogni CF) solo i caratteri relativi al cognome; entrambe
# mediante comprehension

lista1 = [n[0:3] for n in lista_cf]
lista2 = [n[3:6] for n in lista_cf]

print(lista1)
print(lista2)

# 7

# Esercizio
# Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

# Creare una lista che contenga solo i codici fiscali dei nati nel '95, tramite
# comprehension


nuova_lista = [n for n in lista_cf if '95' in n]

print(nuova_lista)

# 8

# Esercizio
# Abbiamo una lista di codici fiscali:

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

# Creare una lista che contenga gli ultimi cinque caratteri dei soli codici fiscali di
# persone nate nel '95, tramite comprehension


nuova_lista = [n[-5:] for n in lista_cf if '95' in n]

print(nuova_lista)

# 9

# Esercizio
# Abbiamo una lista di stringhe di prezzi in dollari, che erroneamente sono stati
# scritti con il simbolo dell'euro:

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

# cambiare il simbolo dell'euro (€) in quello del dollaro ($) per ogni stringa nella
# lista, usando la comprehension.

nuova_lista = [n.replace('€','$') for n in prezzi]

print(nuova_lista)

# 10

# Esercizio
# Abbiamo una lista di studenti:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry", "Isabelle", "John"]

# vogliamo dividere gli studenti in due squadre per un campionato di Uno nel
# seguente modo: la prima metà per un squadra, e la seconda metà per l'altra.
# Creiamo due liste per ogni squadra, e alla fine visualizziamole.

squadra1 = studenti[0:5]
squadra2 = studenti[5:10]
print("Squadra 1:", squadra1)
print("Squadra 2:", squadra2)

# 11

# Esercizio
# Abbiamo una lista di studenti:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
"Grace", "Henry", "Isabelle", "John"]

# vogliamo dividere gli studenti in due squadre per un campionato di Uno nel
# seguente modo: selezioneremo i nomi in posizione pari per un squadra, e i nomi
# in posizione dispari per l'altra.
# Creiamo due liste per ogni squadra, e alla fine visualizziamole.

squadra1 = [n for i, n in enumerate(studenti) if i % 2 == 0]
squadra2 = [n for i, n in enumerate(studenti) if i % 2 == 1]

print("Squadra 1:", squadra1)
print("Squadra 2:", squadra2)

# 12

# Esercizio
# Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio a
# Dicembre):

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

# dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con la media
# dei guadagni precedenti
# Esempio di un possibile output:

# Mese 1: 100 €
# Mese 2: 90 € (media prec: 100 €)
# Mese 3: 70 € (media prec: 95 €)


# Calcola il guadagno medio iniziale (per il mese 1)
media_prec = guadagni[0]

# Itera attraverso la lista dei guadagni
for i in range(len(guadagni)):
    guadagno_mese = guadagni[i]
    print(f'Mese {i + 1}: {guadagno_mese} €', end=' ')

    # Calcola la media dei guadagni precedenti
    if i > 0:
        media_prec = sum(guadagni[:i]) / i
        print(f'(media prec: {media_prec:.2f} €)')
    else:
        print()

# 13

# Esercizio
# Abbiamo una lista con i guadagni degli ultimi 12 mesi (supponiamo da Gennaio
# a Dicembre):

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

# dobbiamo confrontare, stampando tutto a video, il guadagno di ogni mese con
# la media dei guadagni precedenti, e specificare nell'output se è maggiore o
# minore


media_prec = guadagni[0]

# Itera attraverso la lista dei guadagni
for i in range(len(guadagni)):
    guadagno_mese = guadagni[i]
    print(f'Mese {i + 1}: {guadagno_mese} €', end=' ')

    # Calcola la media dei guadagni precedenti
    if i > 0:
        media_prec = sum(guadagni[:i]) / i
        print(f'(media prec: {media_prec:.2f} €)')
        if guadagno_mese > media_prec:
            print('Il GUADAGNO DEL MESE è maggiore alla MEDIA precedente')
        else:
            print('Il GUADAGNO DEL MESE è minore alla MEDIA precedente')
    else:
        print()


# 14 

# Esercizio
# Scrivere una funzione che, data una lista di numeri, fornisca in output il
# maggiore di tutti, senza utilizzare la funzione max()

lista = [12,167,23,1,56,90,345,2]

def maggiore():
    for i in lista:
        if i >= 345:
            print(i)
        else:
            print()


maggiore()

# 15

# Esercizio
# Scrivere una funzione che, data una lista di numeri, fornisca in output il minimo e
# il massimo (possiamo usare o meno le funzioni min() e max())

lista = [12,167,23,1,56,90,345,2]

def min_e_max():
    print('Elemento MAX di lista: '+ str(max(lista)))
    print('Elemento MIN di lista: '+ str(min(lista)))

min_e_max()

# 16

# Esercizio
# Scrivere una funzione che, data una lista di numeri, fornisca in output i due
# numeri più grandi

lista = [12,167,23,1,56,90,345,2]




def i_due_numeri():
    massimo1 = max(lista)
    lista.remove(massimo1)  # Rimuovi il primo massimo dalla lista
    massimo2 = max(lista)
    print('Elemento MAX di lista:', massimo1)
    print('Secondo elemento più grande di lista:', massimo2)

i_due_numeri()

# 17

# Esercizio
# Scrivere una funzione che in input acquisisce una lista di numeri e un numero K;
# in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a
# K; se non ce ne dovesse essere nessuno, dovrà stampare a schermo un
# messaggio adeguato

def funzione():
    lista_numeri = []
    

    while len(lista_numeri) < 6:
        print('Inserisci il numero da aggiungere alla lista: ')
        elemento = int(input())
        lista_numeri.append(elemento)
    
    print('Inserisci K: ')
    K = int(input())
    

    media = str(sum(lista_numeri) / len(lista_numeri))

    for i in lista_numeri:
        if i >= K:
            print('Elemento della lista maggiore di K: ' + str(i) +' <<<>>> ' +'Media: ' + media)
        else:
            print("Nessun numero di 'lista numeri' è più grande di 'k'")

funzione()

# 18

# Esercizio
# Scrivere una funzione che, data una lista di numeri, come output stamperà lo
# stesso numero di asterischi su righe diverse, ottenendo una semplice
# visualizzazione grafica
# Esempio, supponendo di chiamare la funzione aster():

numeri = [5, 2, 3, 4]


# Output:
# *****
# **
# ***
# ****

def aster():
    for numero in numeri:
        print('*' * numero)

aster()


# 19

# Esercizio
# Abbiamo un testo, ad esempio:

racconto = """Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite."""

# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare.
# Esempio, se il testo è

testo = """Ciao a tutti!"""

# l'output sarà:
# {"C": 1, "i": 2, "a": 2, "o": 1, " ": 2, "t": 3, "u": 1, "!": 1}

def conta_car():
    dizionario = {}
    for i in racconto:
        dizionario.update({i:racconto.count(i)})
    print(dizionario)

conta_car()

# 20

# Esercizio
# Abbiamo un testo, ad esempio:

racconto = """Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite."""

# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare, esclusi punteggiatura e spazi.
# Esempio, se il testo è

testo = """Ciao a tutti!"""

# l'output sarà:
# {"C": 1, "i": 2, "a": 2, "o": 1, "t": 3, "u": 1}

def conta_car(testo):
    dizionario = {}
    
    for carattere in testo:
        # Escludi punteggiatura e spazi
        if carattere.isalpha():
            # Converti il carattere in maiuscolo per trattare maiuscole e minuscole allo stesso modo
            
            
            # Aggiorna il dizionario o inizializza il conteggio a 1 se il carattere non esiste nel dizionario
            dizionario[carattere] = dizionario.get(carattere, 0) + 1
    
    return dizionario


risultato = conta_car(racconto)

# Stampa il dizionario risultante
print(risultato)


# 21

# Esercizio
# Abbiamo un testo, ad esempio:

racconto = """Lisetta va a passeggio in campagna; è felice di
raccogliere i fiori che crescono sulle rive, ai bordi della strada.
Ha già un bel mazzetto di ranuncoli e margherite."""

# Creiamo una funzione che prenda il testo in input, e in output ci dia un dizionario che
# contiene ogni tipo di carattere e quante volte appare, senza fare differenza tra maiuscole e
# minuscole.

def conta_car(testo):
    dizionario = {}
    
    for carattere in testo:
        # Escludi punteggiatura e spazi
        if carattere.isalpha():
            # Converti il carattere in maiuscolo per trattare maiuscole e minuscole allo stesso modo
            carattere = carattere.lower()
            
            # Aggiorna il dizionario o inizializza il conteggio a 1 se il carattere non esiste nel dizionario
            dizionario[carattere] = dizionario.get(carattere, 0) + 1
    
    return dizionario


risultato = conta_car(racconto)

# Stampa il dizionario risultante
print(risultato)


# 22


# Andiamo su

# http://www.datiopen.it/it/opendata/Mappa_dei_pub_circoli_locali_in_Italia

# e scarichiamo la mappa dei pub, circoli e locali in Italia

# Nota: per leggerlo nella funzione open() dovremo aggiungere il parametro
# encoding="latin1", ad esempio:

# f = open(file_path, "r", encoding="latin1")


# Esaminiamo il dataset:
# quanti dati ci sono in totale?    --22.473 ----> 2497 righe , 9 colonne--
# quali sono i metadati?            --L'unico metadato che abbiamo è solo il nome del file .xlsx--
# stampiamo il primo elemento
# stampiamo l'ultimo elemento
# riusciamo a stampare un elemento a caso?
# quali sono gli anni di inserimento presenti?  dalla 2007 alla 2016
# quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?  --303 attività--
# quante attività ci sono nella provincia di Vicenza?   --73 attività--
# quante enoteche ci sono, e come si chiamano?  --nessuna enoteca, perchè è un file .xlsx riguardante i pub
# quante attività ci sono in Lazio e Abruzzo assieme?   --237 attività--

import pandas as pd

df = pd.read_excel('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\mappa_pub.xlsx')

print(df.count())   # quanti dati ci sono in totale?
print(df.head(1))   # stampiamo il primo elemento
print(df.tail(1))   # stampiamo l'ultimo elemento
print(df.iloc[125]) # riusciamo a stampare un elemento a caso?

colonna_ordinata_unica = df["Anno inserimento"].unique()    # quali sono gli anni di inserimento presenti?
colonna_ordinata_unica.sort()
for data in colonna_ordinata_unica:
    print(data)


# quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
attivita_nel_quadrato = df[(df['Longitudine'] >= 9) & (df['Longitudine'] <= 10) & (df['Latitudine'] >= 45) & (df['Latitudine'] <= 46)]
numero_di_attivita = len(attivita_nel_quadrato)
print(f"Numero di attività nel quadrato di longitudine 9-10 e latitudine 45-46: {numero_di_attivita}")

# quante attività ci sono nella provincia di Vicenza?
attivita_vicenza = df[(df['Provincia'] == 24)]
numero_di_attivita = len(attivita_vicenza)
print(f"attività in provincia di Vicenza: {numero_di_attivita}")


# quante attività ci sono in Lazio e Abruzzo assieme?
attivita_lazio_abruzzo = df[(df['Regione'] == 12) | (df['Regione'] == 13)]
numero_di_attivita = len(attivita_lazio_abruzzo)
print(f"attività del lazio e abruzzo: {numero_di_attivita}")