# 1

# Abbiamo una lista di liste:

mat = [[0, 1, 2, 3, 4],
[5, 6, 7, 8, 9],
[10, 11, 12, 13, 14]]

# Che tipo di struttura dati o matematica potrebbe rappresentare? Notare che
# tutte le liste "interne" sono della stessa dimensione
# Come facciamo per accedere ad un elemento in particolare?
print(mat)
print(type(mat))        # vedere tipologia di struttura dati

accedere = mat[0][2]    # esempio accesso alla lista
print(accedere)

# 2

# Trasformiamo la lista dell'esercizio precedente

mat = [[0, 1, 2, 3, 4],
[5, 6, 7, 8, 9],
[10, 11, 12, 13, 14]]

# in un array NumPy:
# mat = np.array(mat)
# Come facciamo per accedere ai singoli elementi?

import numpy as np

mat = np.array(mat)     # trasformazione in array
print(mat)

accedere = mat[0,2:5]   # accesso agli elementi
print(accedere)

# 3

# Abbiamo il seguente array NumPy:

import numpy as np

linear_data = np.array([x for x in range(27)])

# Lo ridimensioniamo mediante il metodo .reshape():

reshaped_data = linear_data.reshape((3, 3, 3))

# Quante dimensioni ha il nuovo array?
# Come facciamo per accedere ai singoli elementi?

print(np.shape(reshaped_data))      # numero righe,colonne e numero elementi all'interno
print(reshaped_data)

accedere = reshaped_data[0,:,:]
print(accedere)

# 4

# Abbiamo un territorio cittadino diviso in quattro quadranti; in ognuno di essi c'è
# uno store:

# Vogliamo contare quanti clienti vengono serviti dai diversi store: creiamo una
# struttura dati adeguata con un array NumPy, dove il conteggio di ogni store
# parta da zero.

import numpy as np
import pandas as pd

clienti = np.zeros((4,1), dtype=int)
print(clienti)

df = pd.DataFrame(clienti, index=['UL','UR','LL','LR'],columns=['CLIENTI'])
print(df)

# 5 

import numpy as np
import pandas as pd

# Creazione del DataFrame iniziale con tutti gli store inizialmente a zero clienti
clienti = np.zeros((4, 1), dtype=int)
df = pd.DataFrame(clienti, index=['UL', 'UR', 'LL', 'LR'], columns=['CLIENTI'])

# Simulazione di 100 iterazioni
for _ in range(100):
    # Genera un numero casuale tra 0 e 3 per selezionare uno dei quattro quadranti
    quadrante_scelto = np.random.randint(0, 4)
    
    # Incrementa il conteggio di clienti in quel quadrante di 1
    df.iloc[quadrante_scelto] += 1

# Stampa il conteggio di clienti per ogni store
print("Numero di clienti per ogni store:")
print(df)

# Valore dello store UR e LL
valore_store_UR = df.loc['UR', 'CLIENTI']
valore_store_LL = df.loc['LL', 'CLIENTI']
print("\nValore dello store UR:", valore_store_UR)
print("Valore dello store LL:", valore_store_LL)

# Store con più di 25 clienti
store_piu_di_25_clienti = df[df['CLIENTI'] > 25]
print("\nStore con più di 25 clienti:")
print(store_piu_di_25_clienti)

# Numero di clienti che hanno avuto gli store con più di 25 clienti
numero_clienti_store_piu_di_25 = store_piu_di_25_clienti['CLIENTI'].sum()
print("\nNumero di clienti degli store con più di 25 clienti:", numero_clienti_store_piu_di_25)

# Somma totale dei clienti
somma_totale_clienti = df['CLIENTI'].sum()
print("\nSomma totale dei clienti in tutti gli store:", somma_totale_clienti)

# 6

import numpy as np
import pandas as pd

# Creazione del DataFrame iniziale con tutti gli store inizialmente a zero clienti
clienti = np.zeros((9, 1), dtype=int)
df = pd.DataFrame(clienti, index=['UL', 'UC', 'UR', 'ML','MC','MR','LL','LC','LR'], columns=['CLIENTI'])

# Simulazione di 200 iterazioni
for _ in range(200):
    # Genera un numero casuale tra 0 e 3 per selezionare uno dei quattro quadranti
    quadrante_scelto = np.random.randint(0, 9)
    
    # Incrementa il conteggio di clienti in quel quadrante di 1
    df.iloc[quadrante_scelto] += 1

# Stampa il conteggio di clienti per ogni store
print("Numero di clienti per ogni store:")
print(df)

# Valore dello store UR e LL
valore_store_UR = df.loc['UR', 'CLIENTI']
valore_store_LL = df.loc['LL', 'CLIENTI']
print("\nValore dello store UR:", valore_store_UR)
print("Valore dello store LL:", valore_store_LL)

# Store con più di 25 clienti
store_piu_di_25_clienti = df[df['CLIENTI'] > 25]
print("\nStore con più di 25 clienti:")
print(store_piu_di_25_clienti)

# Numero di clienti che hanno avuto gli store con più di 25 clienti
numero_clienti_store_piu_di_25 = store_piu_di_25_clienti['CLIENTI'].sum()
print("\nNumero di clienti degli store con più di 25 clienti:", numero_clienti_store_piu_di_25)

# Somma totale dei clienti
somma_totale_clienti = df['CLIENTI'].sum()
print("\nSomma totale dei clienti in tutti gli store:", somma_totale_clienti)

# 7

# Chiediamo all'utente di inserire un numero, dividiamolo per 5 e poi stampiamo
# il risultato a video.
# Gestiamo correttamente le eccezioni nel caso l'utente immetta un input errato.

try:
    numero_utente = float(input("Inserisci un numero: "))
    risultato = numero_utente / 5
    print("Il risultato della divisione per 5 è:", risultato)
except ValueError:
    print("Errore: Devi inserire un numero valido.")
except ZeroDivisionError:
    print("Errore: Non puoi dividere per zero.")


# 8

import numpy as np

lunghezza_struttura = 28.75  # Lunghezza della struttura in cm
numero_rivetti = 15  # Numero totale di rivetti

# Calcolare la distanza tra i rivetti
distanza_tra_rivetti = lunghezza_struttura / (numero_rivetti - 1)

# Calcolare i punti esatti in cui inserire i rivetti
punti_di_inserimento = np.arange(0, lunghezza_struttura + 1e-10, distanza_tra_rivetti)

# Arrotondare i punti di inserimento ai decimali desiderati
punti_di_inserimento_arrotondati = np.around(punti_di_inserimento, decimals=2)

# Stampa i punti di inserimento
print(punti_di_inserimento_arrotondati)


# 9

import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\iris.csv')

df = pd.DataFrame(file)
print(df)
print(df.head())
print(df.columns.to_list())

# 10

# Dal dataset di prima:
# • Leggiamo il file e carichiamolo in un DataFrame, aggiungendo i nomi di
# colonna — che si trovano nel file .names — come parametro di
# pd.read_csv()
# • Stampiamo le prime cinque righe e le ultime dieci
# • Stampiamo un riepilogo dei descrittori statistici del dataset

import pandas as pd
import csv

# Apri il file CSV e leggi le righe
with open('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\iris.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Crea un DataFrame dai dati letti
df = pd.DataFrame(rows, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(df.head())
print(df.tail(10))
print(df.describe())

# 11


# Andiamo a questo link e scarichiamo una serie di dataset:
# https://www.kaggle.com/datasets/ahmettezcantekin/beginner-datasets
# Tra i vari dataset presenti, ce n'è uno che contiene diverse qualità di vini e le
# misure di diverse proprietà organolettiche, wine.csv;
# Leggiamo quindi il dataset wine.csv, e visualizziamone le prime e le ultime
# righe;
# Leggiamo nuovamente il dataset, ma stavolta considerando soltanto le ultime 6
# colonne, ricordandoci che in totale il dataset ha 13 colonne;
# Visualizziamo un resoconto dei descrittori statistici di questa versione

import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\wine.csv')

df = pd.DataFrame(file)
print(df.head())
print(df.tail())
print(df[['density', 'pH', 'sulphates', 'alcohol', 'quality', 'type']])
print(df.describe())

# 12

# Consideriamo il seguente dizionario:

import pandas as pd

fatturati_dict = {1997: 12_000, 1998: 15_000,
1999: 20_000, 2000: 23_000, 2001: 25_000,
2002: 17_000, 2003: 14_000, 2004: 21_000}

# Consideriamo ora la seguente Series:

fatturati_series = pd.Series([12_000, 15_000, 20_000,
23_000, 25_000, 17_000, 14_000, 21_000],
index=range(1997, 2005))

# Possiamo accedere alle stesse informazioni nello stesso modo:

# fatturati_dict[1997]
# fatturati_series[1997]

# Dunque qual è la differenza tra i due tipi di dato?   # differenze tra uno e l'altro è che una è una series e l'altra un dizionario
# Cosa potremmo fare con la Series che non possiamo fare con il dizionario?     # nelle series posso accedere a più valori in una volta sola, con i dict no

print(fatturati_series)
print(fatturati_dict)

print(fatturati_dict[1997])
print(fatturati_series[1997])

# 13

# Abbiamo la seguente matrice:
# Creiamo un ndarray con gli stessi valori.
# Ci sono due modalità: inizializzare un array e poi inserire i valori nelle posizioni
# adatte, oppure creare una lista di liste e poi effettuare un casting.

import numpy as np

array = np.array([[1,1,1,1],[5,1,1,1],[20,-4,0,42]])
print(array)

# 14

# Creiamo il seguente ndarray 5×5:
# Per ogni valore, sottraiamo il minimo (2) e poi dividiamo il risultato per il
# massimo (42) meno il minimo. 


import numpy as np

array = np.array([[10,22,21,8,9],[9,42,3,18,11],[5,4,30,12,29],[37,31,7,2,26],[8,6,4,33,15]])
print(array)

# Trova il minimo e il massimo nell'array
valore_minimo = np.min(array)
valore_massimo = np.max(array)

# Sottrai il minimo da ciascun elemento e poi divide per la differenza tra massimo e minimo
array_normalizzato = (array - valore_minimo) / (valore_massimo - valore_minimo)

print(array_normalizzato)