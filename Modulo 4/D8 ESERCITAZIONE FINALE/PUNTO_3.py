# punto 3

import pandas as pd

# Imposta le opzioni di formattazione per Pandas per visualizzare interi
pd.options.display.float_format = '{:,.0f}'.format

def confronto_statistiche_continenti():

    continenti = ['Africa', 'Asia', 'Europe', 'North america', 'Oceania', 'South america']

    dataset = input("\nInserisci il nome del dataset (PER L'ESERCITAZIONE EPICODE INSERIRE IL FILE ==> covid.csv): ").lower()
    continente1 = input('\nInserisci il nome del primo continente (Africa <> Asia <> Europe <> North america <> Oceania <> South america): ').capitalize()
    continente2 = input('\nInserisci il nome del secondo continente (Africa <> Asia <> Europe <> North america <> Oceania <> South america): ').capitalize()
    

    if dataset == 'covid.csv' and continente1 in continenti and continente2 in continenti:

        # Carica il dataset da un file CSV
        df = pd.read_csv('covid.csv')

        # Filtra solo le righe per i continenti specificati
        continente_data1 = df[df['continent'] == continente1].copy()
        continente_data2 = df[df['continent'] == continente2].copy()

        # Filtra solo la colonna 'total_cases'
        casi_totali1 = continente_data1['total_cases']
        casi_totali2 = continente_data2['total_cases']
        mondo_data = df['total_cases']
        massimi_casi_per_continente = df.groupby('continent')['total_cases'].max()
        somma_massimi_casi = massimi_casi_per_continente.sum()


        # Calcola e stampa solo il valore minimo, massimo, media per entrambi i continenti
        statistica1 = casi_totali1.describe()[['min', 'max', 'mean', '75%']]
        statistica2 = casi_totali2.describe()[['min', 'max', 'mean', '75%']]
        statistica_mondo = mondo_data.describe()[['min', 'max', 'mean', '75%']]


        # Calcola le somme dei casi per i continenti
        somma_casi1 = casi_totali1.max()
        somma_casi2 = casi_totali2.max()
        somma_mondo = somma_massimi_casi

        # Calcola le percentuali rispetto ai casi mondiali
        percentuale1 = (somma_casi1 / somma_mondo) * 100
        percentuale2 = (somma_casi2 / somma_mondo) * 100

        print(f"\n\nSTATISTICHE PER {continente1}:\n\n{statistica1}\n")
        print(f"STATISTICHE PER {continente2}:\n\n{statistica2}\n")
        print(f"STATISTICHE MONDO:\n\n{statistica_mondo}\n")

        print(f"Percentuale dei casi di {continente1} rispetto al mondo: {percentuale1:.2f}%")
        print(f"Percentuale dei casi di {continente2} rispetto al mondo: {percentuale2:.2f}%\n\n")
        print(f"TOTALE CASI MONDO: {'{:,.0f}'.format(somma_mondo)}")



        
    else:
        print('ERRORE! INSERIRE I DATI CORRETTI')

confronto_statistiche_continenti()
