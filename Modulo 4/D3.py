# 1

nome_scuola = "Epicode"

indice = 0  # Inizializziamo un indice per scorrere la stringa

while indice < len(nome_scuola):
    print(nome_scuola[indice])
    indice += 1

# 2

numero = 0

while numero <= 20:
    print(numero)
    numero += 1

# 3

numero = 2  # Il numero di cui vogliamo calcolare le potenze
potenza = 1  # L'esponente iniziale è 1
contatore = 1  # Iniziamo dal primo valore

while contatore <= 10:
    risultato = numero ** potenza
    print(f"{numero}^{potenza} = {risultato}")
    
    # Incrementa l'esponente e il contatore
    potenza += 1
    contatore += 1

# 4

# Il numero di cui vogliamo calcolare le potenze
potenza = 1  # L'esponente iniziale è 1
contatore = 1  # Iniziamo dal primo valore

print("Inserisci un numero:\n")
numero = int(input())

while contatore <= 10:
    risultato = numero ** potenza
    print(f"{numero}^{potenza} = {risultato}")
    
    # Incrementa l'esponente e il contatore
    potenza += 1
    contatore += 1

# 5

# Abbiamo due liste, una di studenti e una di corsi:
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith",
            "Grace", "Henry"]

corsi = ["Cybersecurity", "Data Analyst", "Backend",
         "Frontend", "Data Analyst", "Backend", "Frontend"]

# Verificare che entrambe le liste abbiano la stessa lunghezza, e stampare a video
# una frase che ci dica se è così o meno.

if len(studenti) == len(corsi):
    print("Le liste hanno la stessa lunghezza")
else:
    print("Le liste NON hanno la stessa lunghezza")

# 6

# Abbiamo due liste, una di studenti e una di corsi:

studenti = ["Alex", "Bob", "Cindy", "Dan", "Faith",
"Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst",
"Frontend", "Data Analyst", ]

# Aggiungere i dati mancanti alla lista corsi, sapendo che
        
        # Emma segue Data Analyst
        # Faith segue Backend
        # Grace segue Frontend
        # Henry segue Cybersecurity

# Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in
# coda alle liste, poi verificheremo che sono della stessa lunghezza e se lo sono
# stamperemo la lista corsi.

studenti.append("Emma")
corsi.append("Backend")

if len(studenti) == len(corsi):
     print("CORSI:")
     for i in corsi:
          print(i)
else:
     print("Le liste NON hanno la stessa lunghezza")



# 8

# Scriviamo un programma che chiede in input all'utente una stringa e visualizza i
# primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.
# Attenzione a tutti i casi particolari, ovvero implementare soluzioni ad hoc per
# stringhe di lunghezza inferiore a 6 caratteri.

print("Inserisci una stringa:")
stringa = str(input())

if len(stringa) >= 6:
    print(stringa[:3]+"..."+stringa[-3:])
elif len(stringa) >= 5:
    print(stringa[:2]+"."+stringa[-2:])
elif len(stringa) >= 4:
    print(stringa[:1]+"."+stringa[-2:])
elif len(stringa) >= 3:
    print(stringa[:1]+"."+stringa[-1:])
else:
    print("Stringa inferiore ai 3 caratteri:", stringa)


#9
# Memorizza e stampa tutti i fattori di un numero dato in input.
# Esempio:
# input: 150
# output: [2, 3, 5, 5]


numero = int(input("Inserisci un numero: "))

print(f"I fattori di {numero} sono:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
