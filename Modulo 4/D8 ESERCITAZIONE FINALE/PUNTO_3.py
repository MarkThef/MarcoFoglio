# punto 3

import pandas as pd

# Imposta le opzioni di formattazione per Pandas per visualizzare interi
pd.options.display.float_format = '{:,.0f}'.format

def confronto_statistiche_continenti():

    dataset = input('Inserisci il nome del dataset: ').lower()
    continente1 = input('Inserisci il nome del primo continente(INSERIRE IL DATO IN LINGUA INGLESE): ')
    continente2 = input('Inserisci il nome del secondo continente(INSERIRE IL DATO IN LINGUA INGLESE): ')

    if dataset == 'covid.csv':

        # Carica il dataset da un file CSV
        df = pd.read_csv('covid.csv')

        # Filtra solo le righe per i continenti specificati
        continente_data1 = df[df['continent'] == continente1].copy()
        continente_data2 = df[df['continent'] == continente2].copy()

        # Filtra solo la colonna 'total_cases'
        casi_totali1 = continente_data1['total_cases']
        casi_totali2 = continente_data2['total_cases']
        mondo_data = df['total_cases']

        # Calcola e stampa solo il valore minimo, massimo, media per entrambi i continenti
        statistica1 = casi_totali1.describe().loc[['min', 'max', 'mean', '75%']]
        statistica2 = casi_totali2.describe().loc[['min', 'max', 'mean', '75%']]
        statistica_mondo = mondo_data.describe().loc[['min', 'max', 'mean', '75%']]

        # Calcola le somme dei casi per i continenti
        somma_casi1 = casi_totali1.sum()
        somma_casi2 = casi_totali2.sum()
        somma_mondo = mondo_data.sum()

        # Calcola le percentuali rispetto ai casi mondiali
        percentuale1 = (somma_casi1 / somma_mondo) * 100
        percentuale2 = (somma_casi2 / somma_mondo) * 100

        print(f"\n\nSTATISTICHE PER {continente1}:\n\n{statistica1}\n")
        print(f"STATISTICHE PER {continente2}:\n\n{statistica2}\n")
        print(f"STATISTICHE MONDO:\n\n{statistica_mondo}\n")

        print(f"Percentuale dei casi di {continente1} rispetto al mondo: {percentuale1:.2f}%")
        print(f"Percentuale dei casi di {continente2} rispetto al mondo: {percentuale2:.2f}%\n\n")

        print(f"Totale casi di {continente1}: {somma_casi1:,.0f}")
        print(f"Totale casi di {continente2}: {somma_casi2:,.0f}")
        print(f"Totale casi nel mondo: {somma_mondo:,.0f}")

        
    else:
        print('ERRORE! INSERIRE I DATI CORRETTI')

confronto_statistiche_continenti()
