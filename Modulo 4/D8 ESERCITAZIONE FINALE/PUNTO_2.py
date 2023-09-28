# punto 2

import pandas as pd

df = pd.read_csv('covid.csv')

totale_casi_x_continente = df.groupby('continent')['total_cases'].sum()
totale_casi_x_continente = totale_casi_x_continente.apply(lambda x: "{:,.0f}".format(x))  # Formatta il numero senza decimali e con separatore delle migliaia

print('\nCASI TOTALI PER CONTINENTE\n')
print(totale_casi_x_continente)