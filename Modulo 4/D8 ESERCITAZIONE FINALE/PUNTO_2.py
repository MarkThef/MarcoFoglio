# punto 2

import pandas as pd

# Carica il file CSV in un DataFrame
df = pd.read_csv('covid.csv')

# Raggruppa il DataFrame per continente e location, quindi trova il massimo valore di total_cases in ciascun gruppo
massimo_per_continente_location = df.groupby(['continent', 'location'])['total_cases'].max().reset_index()

# Poi, raggruppa nuovamente per continente e somma i massimi valori di total_cases per ciascun continente
somma_massimi_per_continente = massimo_per_continente_location.groupby('continent')['total_cases'].sum().reset_index()

# Formatta il numero senza decimali e con separatore delle migliaia
somma_massimi_per_continente['total_cases'] = somma_massimi_per_continente['total_cases'].apply(lambda x: "{:,.0f}".format(x))

# Rinomina la colonna per la somma
somma_massimi_per_continente = somma_massimi_per_continente.rename(columns={'total_cases': 'Totale Casi'})

# Stampa il risultato
print('\nTOTALE CASI PER CONTINENTE\n')
print(somma_massimi_per_continente)


