# punto 3

import pandas as pd

# Imposta le opzioni di formattazione per Pandas per visualizzare interi
pd.options.display.float_format = '{:,.0f}'.format

def confronto_statistiche_continenti():
    continenti_validi = ['Africa', 'Asia', 'Europe', 'North america', 'Oceania', 'South america']

    dataset = input("\nInserisci il nome del dataset (per l'esercitazione, inserire il file 'covid.csv'): ").strip().lower()
    continente1 = input('\nInserisci il nome del primo continente tra ==> Africa, Asia, Europe, North America, Oceania, South America: ').strip().capitalize()
    continente2 = input('\nInserisci il nome del secondo continente tra  ==> Africa, Asia, Europe, North America, Oceania, South America: ').strip().capitalize()
    
    if dataset != 'covid.csv' or continente1 not in continenti_validi or continente2 not in continenti_validi:
        print('ERRORE! Inserire dati corretti.')
        return

    # Carica il dataset da un file CSV
    df = pd.read_csv('covid.csv')

    # Filtra solo le righe per i continenti specificati
    continente_data1 = df[df['continent'] == continente1].copy()
    continente_data2 = df[df['continent'] == continente2].copy()

    # Reimposta le opzioni di formattazione per Pandas per visualizzare interi
    pd.options.display.float_format = '{:,.0f}'.format

    # Filtra solo la colonna 'total_cases'
    casi_totali1 = continente_data1.groupby('location')['total_cases'].max()
    casi_totali2 = continente_data2.groupby('location')['total_cases'].max()

    # Calcola e stampa solo il valore minimo, massimo, media per entrambi i continenti
    statistica1 = casi_totali1.describe()[['min', 'max', 'mean', '75%']]
    statistica2 = casi_totali2.describe()[['min', 'max', 'mean', '75%']]
    statistica_mondo = df['total_cases'].describe()[['min', 'max', 'mean', '75%']]

    # Calcola la somma dei casi per il continente 1
    somma_casi_continente1 = casi_totali1.sum()

    # Calcola la somma dei casi per il continente 2
    somma_casi_continente2 = casi_totali2.sum()

    # Calcola la somma dei casi mondiali
    somma_casi_mondo = df.groupby('location')['total_cases'].max().sum()

    # Calcola le percentuali rispetto ai casi mondiali
    percentuale1 = (somma_casi_continente1 / somma_casi_mondo) * 100
    percentuale2 = (somma_casi_continente2 / somma_casi_mondo) * 100

    # Stampa le statistiche
    print(f"\nSTATISTICHE PER {continente1}:\n\n{statistica1}\n")
    print(f"STATISTICHE PER {continente2}:\n\n{statistica2}\n")
    print(f"STATISTICHE MONDO:\n\n{statistica_mondo}\n")

    # Stampa percentuali
    print(f"\nPercentuale dei casi di {continente1} rispetto al mondo: {percentuale1:.2f}%")
    print(f"Percentuale dei casi di {continente2} rispetto al mondo: {percentuale2:.2f}%\n\n")
    print(f"TOTALE CASI MONDO: {'{:,.0f}'.format(somma_casi_mondo)}")

confronto_statistiche_continenti()




