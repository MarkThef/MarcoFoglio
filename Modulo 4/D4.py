# 1

nome_scuola = "Epicode"

for i in nome_scuola:
    print(i)

# 2

elementi = "NPKOHC"

for elemento in elementi:
    print(elemento)

# 3

elementi = "NPKOHC"

for elemento in elementi:
    print("Elemento_"+ elemento)

# 4

elementi = "NPKOHC"

for index,elemento in enumerate(elementi):
    print("Elemento - numero "+ str(index) + ": " +elemento)

# 5 

testo = "marmalade"

modifica = testo.replace('a','e')
modifica1 = modifica.replace('e','a')

testo = modifica1

print(testo)

for i in testo:
    print(i) 




index = 0

while len(testo) > index:  # Aggiungi una condizione di uscita
    print(testo)
    index += 1  # Incrementa l'indice

# 6

for contatore in range(10):
    risultato = 2 ** contatore
    print(f"2^{contatore} = {risultato}")

# 7

lista = []  # Inizializza una lista vuota

for contatore in range(10):
    risultato = 2 ** contatore
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)


lista = []  # Inizializza una lista vuota
contatore = 0

while contatore in range(10):
    risultato = 2 ** contatore
    contatore += 1
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)

# 8

lista = []  # Inizializza una lista vuota

for contatore in range(10):
    risultato = 3 ** contatore
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)


lista = []  # Inizializza una lista vuota
contatore = 0

while contatore in range(10):
    risultato = 3 ** contatore
    contatore += 1
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)

# 9

lista = []  # Inizializza una lista vuota

print("Inserisci un numero:")
k = int(input())

for contatore in range(10):
    risultato = k ** contatore
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)


lista = []  # Inizializza una lista vuota

print("Inserisci un numero:")
k = int(input())

contatore = 0

while contatore in range(10):
    risultato = 2 ** contatore
    contatore += 1
    lista.append(risultato)  # Aggiungi il risultato alla lista

print(lista)

# 10

for contatore in range(100000000000000000000):
    risultato = 2 ** contatore
    if risultato < 25000:
        print(risultato)
    else:
        break

# 11

N = 15000000

for contatore in range(100000000000000000000):
    risultato = 2 ** contatore
    if risultato < N:
        print(risultato)
    else:
        break 

# 12

for contatore in range(0,100,3):
    risultato = 2 ** contatore
    print(risultato)
    
# 13

numeri = [4, 9, 5, 1, 7, 10, 2, 3]

massimo = numeri[0]  # Inizializza il massimo con il primo elemento della lista

for numero in numeri:
    if numero > massimo:
        massimo = numero  # Aggiorna il massimo se il numero corrente è maggiore

print(massimo)  # Stampa il massimo valore

# 14

eta_studenti = [20, 30, 40, 50, 60]


somma = 0  # Inizializza la somma a zero

for i in eta_studenti:
    somma += i  # Aggiungi il numero corrente alla somma

media = somma / len(eta_studenti)  # Calcola la media

print("La media è:", media)

# 15

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]

somma = 0  # Inizializza la somma a zero

for i in guadagni:
    somma += i  # Aggiungi il numero corrente alla somma

media = somma / len(guadagni)  # Calcola la media

print("La media è:", media)

# 16

guadagni = [100, 90, 70, 40, 50, 80, 90, 120]
N = 8

somma = 0  # Inizializza la somma a zero

for guadagno in guadagni:
    somma += guadagno  # Aggiungi il numero corrente alla somma

media = somma / len(guadagni)  # Calcola la media

print(f"La media degli ultimi {N} mesi è: ", media)

# 17

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]

for nomi in studenti:
    print("- " + nomi)

# 18

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]

collezione = zip(studenti,corsi,edizioni)

for i in collezione:
    studente,corso,edizione = i
    print(studente+" segue "+corso+","+"edizione "+str(edizione))

# 19

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Belvedere", "Semestre", "Sosta", "Orpello", "Abete"]

conteggio = 0  # Inizializza il conteggio a zero

for elemento in parole:
    conteggio += elemento.count('e')  # Aggiungi al conteggio il numero di 'e' nell'elemento corrente

print(conteggio)

# 20

parole = ["Albergo", "Sedia", "Borgo", "Petalo", "Eremo", "Belvedere", "Semestre", "Esteta", "Sosta", "Orpello", "Abete", "Orologio", "Cesta", "Ermellino"]

for elemento in parole:
    conteggio_minuscola = elemento.count('e')  # Conta 'e' minuscola
    conteggio_maiuscola = elemento.count('E')  # Conta 'E' maiuscola

    conteggio_totale = conteggio_minuscola + conteggio_maiuscola  # Somma i conteggi

    print(f"{elemento} contiene {conteggio_totale} 'e' (minuscole e maiuscole) ")

# 21

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

lista =[]

for codice in lista_cf:
    if "95"in codice:
        lista.append(codice)
        print("IL "+codice+" CONTIENE LA DICITURA '95'")
    else:
        pass

print(lista)

# 22

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C",
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F",
"DEFGHI95J06A987G"]

for codice in lista_cf:
    print("Questi sono i caratteri relativi al nome e cognome: "+codice[:6])

# 23

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace",
"Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend",
"Data Analyst", "Backend", "Frontend", "Cybersecurity"]
edizioni = [1, 2, 3, 2, 2, 1, 3, 3]


collezione = zip(studenti,corsi,edizioni)

for i in collezione:
    studente,corso,edizione = i
    if edizione == 1:
        print("STUDENTE: "+studente+" CORSO: "+corso+" EDIZIONE: "+str(edizione))
    else:
        continue

# 24

# Creiamo un dizionario che assegni ad ogni proprietario la sua auto, sapendo
# che:
# • Ada guida una Punto
# • Ben guida una Multipla
# • Charlie guida una Golf
# • Debbie guida una 107 Poi stampiamo il dizionario per intero, e poi l'auto
#   associata a Debbie.

dizionario = {'Ada':'Punto', 'Ben':'MUltipla', 'Charlie':'Golf', 'Debbie':'107'}

for chiave, valore in dizionario.items():
    if valore == '107':
        print(chiave,valore)
    else:
        pass

# 25

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

# Aggiungere i proprietari Emily e Fred che posseggono rispettivamente una A1 e
# una Octavia; eliminare i dati relativi a Ben.
# Stampare il dizionario per controllare che sia tutto corretto.

del dizionario_auto["Ben"]
print(dizionario_auto)

dizionario_auto['Emily'] = 'A1'
dizionario_auto['Fred'] = 'Octavia'

print(dizionario_auto)

# 26

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia",
"Grace": "Yaris", "Hugh": "Clio"}

# Aggiornare il dizionario dizionario_auto con i dati contenuti in
# nuovi_proprietari e stamparlo. Cosa è successo a Ben?

dizionario_auto['Ben'] = 'Polo'
dizionario_auto['Fred'] = 'Octavia'
dizionario_auto['Grace'] = 'Yaris'
dizionario_auto['Hugh'] = 'Clio'

print(dizionario_auto)

# 27

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107", "Emily": "A1", "Fred":
"Octavia", "Grace": "Yaris", "Hugh": "Clio"}

# Viene richiesto di ricercare in questo dataset i dati di Hugh, Ada, Emily e
# Debbie, e visualizzare le auto relative.

# Chiavi da cercare
chiavi_da_cercare = ["Hugh", "Ada", "Emily", "Debbie"]

# Itera attraverso le coppie chiave-valore del dizionario
for k, v in dizionario_auto.items():
    if k in chiavi_da_cercare:
        print(f"{k}: {v}")

# 28

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie":
"Golf", "Debbie": "107", "Emily": "A1", "Fred": "Octavia", "Grace":
"Yaris", "Hugh": "Clio"}

chiavi_da_cercare = ["Ada", "Emily","Jade","Ben","Hugh","Kelly","Charlie"]


for k, v in dizionario_auto.items():
    if k in chiavi_da_cercare:
        print(f"{k}: {v}")
    else:
        print(f"{k} --> QUESTA CHIAVE NON ESISTE IN dizionario_auto")

# Viene richiesto di ricercare in questo dataset i dati di Ada, Emily, Jade, Ben, Hugh, Kelly e
# Charlie, e visualizzare le auto relative.
# Non tutti i dati potrebbero essere presenti nel dataset, quindi quando un nome non è
# presente visualizzeremo un messaggio adeguato.

# 29

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

# utilizzando il metodo .keys(), stampiamone tutte le chiavi.

print(diz.keys())

# 30

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

# utilizzando il metodo .values(), stampiamone tutte i valori.

print(diz.values())

# 31

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

# utilizzando il metodo dei dizionari .items() stampate le coppie chiave-valore
# presenti nel dizionario su righe diverse

vista = diz.items()

for k,v in vista:
    print(k+":"+str(v))

# 32

diz = {"a": 121, "zy": 3774, "qop": 147726, "ab": 328, "k":
12, "clap": 9}

# utilizzando il metodo dei dizionari .values(), calcolare il valore massimo, il
# valore minimo, la somma, e stampiamo i risultati.

massimo = max(diz.values())
minimo = min(diz.values())
somma = sum(diz.values())
print(massimo)
print(minimo)
print(somma)

# 33

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

# Con un ciclo for, e usando il metodo .items(), stampiamo ogni proprietario
# e la sua auto, formattandolo come:
# Ada guida una Punto
# Ben guida una Multipla
# ...

collezione = dizionario_auto.items()

for k,v in collezione:
    print(k+" guida una "+v)

# 34

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla",
"Charlie": "Golf", "Debbie": "107"}

# Con un ciclo, e usando il metodo .values(), stampiamo a video tutte le auto
# che non sono una Multipla.


for k, v in dizionario_auto.items():
    if v != "Multipla":  # Verifica se il valore non è "Multipla"
        print(f"{k}: {v}")

# 35

# Abbiamo i seguenti dati riguardo dei collezionisti e le loro collezioni:
# • Ada ha 10 Funko Pop, 5 action figures e 35 manga
# • Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels
# • Charlie ha 31 action figures e 18 graphic novels
# • Debbie ha 1 Funko Pop, 9 graphic novels, 25 manga e 2 action figures
# Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli

Funko_pop = {'Ada': 10,'Ben': 2,'Debbie': 1}
Action_figures = {'Ada': 5,'Ben': 6,'Charlie': 31,'Debbie': 2}
Manga = {'Ada': 35,'Ben': 40,'Debbie': 25}
Graphic_novels = {'Ben': 2,'Charlie': 18,'Debbie': 9}

Funko_pop['action figures'] = Action_figures
Action_figures['manga'] = Manga
Manga['graphic novels'] = Graphic_novels

print(Funko_pop)

# 36

# • Ada ha 10 Funko Pop, 5 action figures e 35 manga
# • Ben ha 2 Funko Pop, 6 action figures, 40 manga e 2 graphic novels (entrambe 
# della DC)
# • Charlie ha 31 action figures e 18 graphic novels (di cui 10 della Marvel e 8 
# della DC)
# • Debbie ha 1 Funko Pop, 9 graphic novels (di cui 4 della DC e 5 della Marvel), 
# 25 manga e 2 action figures

# Creare dei dizionari innestati che contengano questi dati, e quindi visualizzarli.

Funko_pop = {'Ada': 10,'Ben': 2,'Debbie': 1}
Action_figures = {'Ada': 5,'Ben': 6,'Charlie': 31,'Debbie': 2}
Manga = {'Ada': 35,'Ben': 40,'Debbie': 25}
Graphic_novels = {'Ben': {'DC': 2},'Charlie': {'MARVEL': 10,'DC': 8},'Debbie': {'MARVEL': 5,'DC': 4}}

print(Graphic_novels)

# 37

# Riguardo l'esercizio precedente, stampiamo le risposte a:

# 1. quanti Funko Pop ha Ada?
# 2. quanti manga ha Ben?
# 3. quante graphic novels della Marvel ha Debbie?
# 4. quanti Funko Pop hanno Ada e Ben in tutto?
# 5. quanti manga hanno in tutto i collezionisti?
# 6. quante graphic novel della DC hanno in tutto i collezionisti?
# 7. quante graphic novel hanno in tutto i collezionisti?

print(Funko_pop['Ada'])
print(Manga['Ben'])
print(Graphic_novels['Debbie']['MARVEL'])
print(Funko_pop['Ada']+Funko_pop['Ben'])
print(Manga['Ada']+Manga['Ben']+Manga['Debbie'])
print(Graphic_novels['Debbie']['DC']+Graphic_novels['Ben']['DC']+Graphic_novels['Charlie']['DC'])
print(Graphic_novels['Debbie']['DC']+Graphic_novels['Ben']['DC']+Graphic_novels['Charlie']['DC']+Graphic_novels['Charlie']['MARVEL']+Graphic_novels['Debbie']['MARVEL'])

