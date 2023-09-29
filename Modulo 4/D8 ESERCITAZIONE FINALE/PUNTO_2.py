# punto 2

import pandas as pd

# Carica il file CSV in un DataFrame
df = pd.read_csv('covid.csv')

# Raggruppa il DataFrame per continente e trova il massimo valore di total_cases in ciascun gruppo
massimo_per_continente = df.groupby('continent')['total_cases'].max()
massimo_per_continente = massimo_per_continente.apply(lambda x: "{:,.0f}".format(x))  # Formatta il numero senza decimali e con separatore delle migliaia

# Stampa il massimo valore di total_cases per ciascun continente
print('\nTOTALE CASI PER CONTINENTE\n')
print(massimo_per_continente)
