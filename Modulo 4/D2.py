# 1

nome_scuola = "Epicode"
print(nome_scuola)

# 2

nome_scuola = "Epicode"
print(nome_scuola[0])

# 3

nome_scuola = "Epicode"
print(nome_scuola[0:3])

# 4

nome_scuola = "Epicode"
print(nome_scuola.upper())

# 5

#METODO 1
x = 10  # Assegna il valore 10 a x
x += 2  # Incrementa x di 2
x *= 3  # Moltiplica x per 3
print(x)

#METODO 2
x = 10  # Assegna il valore 10 a x
x = (x + 2) * 3  # Incrementa x di 2 e moltiplica il risultato per 3
print(x)

# 6

# Input dei dati
print("LT Benzina (SERBATOIO)")
Benzina_LT_serb = float(input())

print("KM per LT")
km_lt = float(input())

print("PREZZO al LT")
prezzo_lt = float(input())

# Calcolo del costo per 100 KM
consumo_100km = 100 / km_lt
costo_100KM = consumo_100km * prezzo_lt

# Stampare il risultato
print(f"Il costo per percorrere 100 chilometri è di {costo_100KM} euro.")

# 7

print("INSERISCI UNA STRINGA DI CARATTERI")
stringa = str(input())
modif_str = stringa[:3]+"..."+stringa[-3:]
print(str(modif_str))

# 8

a = "Epicode"
b = "Windows"
c = "Excel"
d = "Powerpoint"
e = "Word"

if len(a) >= 5 and len(a) <= 8:
    print("la variabile 'a' ha più di 5 caratteri e meno di 8")
else:
    print("la variabile 'a' NON ha più di 5 caratteri e meno di 8\n")

if len(b) >= 5 and len(b) <= 8:
    print("la variabile 'b' ha più di 5 caratteri e meno di 8")
else:
    print("la variabile 'b' NON ha più di 5 caratteri e meno di 8\n")

if len(c) >= 5 and len(c) <= 8:
    print("la variabile 'c' ha più di 5 caratteri e meno di 8")
else:
    print("la variabile 'c' NON ha più di 5 caratteri e meno di 8\n")

if len(d) >= 5 and len(d) <= 8:
    print("la variabile 'd' ha più di 5 caratteri e meno di 8")
else:
    print("la variabile 'd' NON ha più di 5 caratteri e meno di 8\n")

if len(e) >= 5 and len(e) <= 8:
    print("la variabile 'e' ha più di 5 caratteri e meno di 8")
else:
    print("la variabile 'e' NON ha più di 5 caratteri e meno di 8\n")

# 9

codici = ["knt-S1","cba-G9","qtr-Z8"]

cod_1 = codici[0][-3:]
cod_2 = codici[1][-3:]
cod_3 = codici[2][-3:]

print(cod_1)
print(cod_2)
print(cod_3)

# 10

codici = ["knt-S1","cba-G9","qtr-Z8"]

cod_1 = codici[0][-3:]
cod_2 = codici[1][-3:]
cod_3 = codici[2][-3:]

print(cod_1)
print(cod_2)
print(cod_3)

lista = []

lista.append(cod_1)
lista.append(cod_2)
lista.append(cod_3)

print(lista)

# 11

# Abbiamo un insieme (set) di titoli di azioni "growth" (cioè che hanno una crescita dei
# ricavi maggiore della media):

growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre",
          "Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

# Abbiamo un insieme di titoli "value" (cioè titoli che offrono agli investitori un elevato
# ritorno sull’investimento, garantendo al contempo stabilità e sicurezza):

value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.",
         "Wells Fargo & Co.", "Verizon Communications", "BP PLC",
         "LyondellBasell Industries", "MetLife", "Interactive Brokers Group",
         "Intel"}

# Abbiamo un insieme di titoli di aziende ad alta tecnologia:
tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms",
         "Tesla", "Alibaba", "Salesforce", "Advanced Micro Devices",
           "Intel", "PayPal", "Activision Blizzard", "Electronic Arts",
             "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

# Abbiamo un insieme di titoli di aziende nell'healthcare:
healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.",
               "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer",
                "Thermo Fisher Scientific", "Abbott Laboratories"}


# ESERCIZIO 3/3

# punto 1-2        in questo caso usiamo un piccolo script che ci da la possibilità di stampare i set a video

while True:
    print("Scegli tipologia del titolo:\n\n 1-GROWTH    2-VALUE     3-TECH      4-HEALTHCARE")
    titolo = input()
    
    if titolo in ['1', '2', '3', '4']:
        titolo = int(titolo)
        break  # Esci dal loop se l'input è uno dei valori validi
    else:
        print("INSERISCI UNA DELLE OPZIONI VALIDE (1, 2, 3 o 4)\n")

# Ora puoi gestire l'input dell'utente
if titolo == 1:
    print("I titoli Growth sono:\n")
    for i in growth:
        print(i)
elif titolo == 2:
    print("I titoli Value sono:\n")
    for i in value:
        print(i)
elif titolo == 3:
    print("I titoli Tech sono:\n")
    for i in tech:
        print(i)
elif titolo == 4:
    print("I titoli Healthcare sono:\n")
    for i in healthcare:
        print(i)

# punto 3

# investire su INTEL

# punto 4

# TITOLI HEALTHCARE CHE NON SONO VALUE: UnitedHealth Group, Eli Lilly & Co., Novo Nordisk,Merck & Co.,
# Roche Holding, Thermo Fisher Scientific, Abbott Laboratories

# punto 5

# non ci sono aziende sia tech che healthcare

# punto 6

# TECH-GROWTH : Alphabet, Amazon, Tesla, Salesforce

# TECH-VALUE : Intel