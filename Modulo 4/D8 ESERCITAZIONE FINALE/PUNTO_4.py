# punto 4

import pandas as pd

df = pd.read_csv('covid.csv')

# Imposta le opzioni di formattazione per Pandas per visualizzare interi
pd.options.display.float_format = '{:,.0f}'.format


def confronto_vaccini_continenti():

    dataset = input("Inserisci il nome del dataset (PER L'ESERCITAZIONE EPICODE INSERIRE IL FILE ==> covid.csv): ").lower()  

    if dataset == 'covid.csv':

        # Carica il dataset da un file CSV
        df = pd.read_csv('covid.csv')

        
        vaccinazioni_per_continente = df.groupby('continent')['total_vaccinations'].max()
        vaccinazioni_per_continente = vaccinazioni_per_continente.copy()
        statistica_vaccini = vaccinazioni_per_continente.describe().loc[['min', 'max', 'mean', '75%']]

        print('\n\nTOTALE VACCINAZIONI PER CONTINENTE\n')
        print(vaccinazioni_per_continente)
        print('\n\nSTATISTICHE TOTALI VACCINI MONDO\n')
        print(statistica_vaccini)

    else:
        print('ERRORE! INSERIRE I DATI CORRETTI')

confronto_vaccini_continenti()