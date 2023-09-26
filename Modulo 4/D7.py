import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\amazon.csv')

df = pd.DataFrame(file)

# Esercizio 1 1/2

print(df.shape)
print(df.sample(n=10))      # Estrai 10 righe casuali dal DataFrame
print(df.columns)           # per vedere nomi delle colonne

positive = (df['Positive'] == 1).sum()      # commenti positivi 15233
negative = (df['Positive'] == 0).sum()      # commenti negativi 4767
print(positive)
print(negative)

# Esercizio 1 2/2

applicazioni =['app','App','application','Application']
gioco = ['game','Game','GAME','gaming','Gaming','GAMING','gamer','Gamer','GAMER']
raccomanadare = ['Recommend','recommend','RECOMMEND']
non_raccomandare = ["i don't recommend","i don't recommend downloading","don't download the product"]
kindle = ['Kindle','kindle','KINDLE']

condizione1 = df['reviewText'].str.contains('|'.join(applicazioni), case=False)     
condizione2 = df['reviewText'].str.contains('|'.join(gioco), case=False)            
condizione3 = df['reviewText'].str.contains('|'.join(raccomanadare), case=False) & (df['Positive'] == 1)      
condizione4 = df['reviewText'].str.contains('|'.join(non_raccomandare), case=False) & (df['Positive'] == 0)   
condizione5 = df['reviewText'].str.contains('|'.join(kindle), case=False) & (df['Positive'] == 1)      
condizione6 = df['reviewText'].str.contains('|'.join(kindle), case=False) & (df['Positive'] == 0)


print(df[condizione1])      # 9608 recensioni parlano di app
print(df[condizione2])      # 4763 recensioni parlano di game
print(df[condizione3])      # 1090 recensioni raccomandano il prodotto
print(df[condizione4])      # 11 recensioni non raccomandano il prodotto
print(df[condizione5])      # 2032 recensioni positive menzionano kindle
print(df[condizione6])      # 655 recebsioni negative menzionano kindle


# Esercizio 2

import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\diabetes.csv')

df = pd.DataFrame(file)

print(df.shape)
print(df.head(5))       # stampo prime 5 righe
print(df.columns)       # stampo metadati colonne
print(df.describe())    # stampo descrittori statici dataset

min_20 = (df['Age (years)'] < 20).sum()    # < 20 risulta 0
magg_20_min_30 = ((df['Age (years)'] >= 20) & (df['Age (years)'] <= 30)).sum()      # tra 20 e 30 compresi risulta 417
magg_30_min_40 = ((df['Age (years)'] >= 30) & (df['Age (years)'] <= 40)).sum()      # tra 30 e 40 compresi risulta 178
magg_40_min_50 = ((df['Age (years)'] >= 40) & (df['Age (years)'] <= 50)).sum()      # tra 40 e 50 compresi risulta 126
magg_50 = (df['Age (years)'] > 50).sum()    # > 50 risulta 81
print(min_20)
print(magg_20_min_30)
print(magg_30_min_40)
print(magg_40_min_50)
print(magg_50)


media_20 = df[df['Age (years)'] < 20]['Diastolic blood pressure (mm Hg)'].mean()    # < 20 media nan
media_20_30 = df[(df['Age (years)'] >= 20) & (df['Age (years)'] <= 30)]['Diastolic blood pressure (mm Hg)'].mean()     # tra 20 e 30 compresi media 65.32
media_30_40 = df[(df['Age (years)'] >= 30) & (df['Age (years)'] <= 40)]['Diastolic blood pressure (mm Hg)'].mean()      # tra 30 e 40 compresi media 69.63
media_40_50 = df[(df['Age (years)'] >= 40) & (df['Age (years)'] <= 50)]['Diastolic blood pressure (mm Hg)'].mean()      # tra 40 e 50 compresi media 74.21
media_50 = df[df['Age (years)'] > 50]['Diastolic blood pressure (mm Hg)'].mean()   # > 50 media 78.38
print(media_20)
print(media_20_30)
print(media_30_40)
print(media_40_50)
print(media_50)

# Raggruppa il DataFrame per la colonna 'Age (years)' e calcola la media della pressione per ogni anno di età
media_per_anno = df.groupby('Age (years)')['Diastolic blood pressure (mm Hg)'].mean()

# Stampa il risultato
print(media_per_anno)

# Esercizio 3

import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\insurance.csv')

df = pd.DataFrame(file)

print(df.shape)
print(df.columns)

media_regioni = df.groupby('region')['charges'].mean()      # southeast= 14735.411438 - northeast= 13406.384516 - northwest= 12417.575374 - southwest= 12346.937377 
print(media_regioni)

media_fumatori = df.groupby('smoker')['charges'].mean()      # non fumatori = 8434.268298 - fumatori = 32050.231832  
print(media_fumatori)

media_sesso = df.groupby('sex')['charges'].mean()      # male = 13956.751178 - donne = 12569.578844  
print(media_sesso)

print(df['bmi'].describe())     # stampo descrittori statici 'bmi'
print(df['charges'].describe())     #   min= 1121.873900 - mean= 13270.422265 - max= 63770.428010

# Esercizio 4

import pandas as pd

file = pd.read_csv('C:\\Users\\markt\\Desktop\\NewProject\\Modulo 4\\pokemon_modific.csv')

df = pd.DataFrame(file)

print(df.shape)

# df.drop('#',axis=1, inplace=True)   # ho dovuto droppare la prima colonna perchè L'ID non era univoco
# print(df)

# df.to_csv('pokemon_modific.csv', index_label='ID')  # salvo nuovo file csv modificato con ID univoco 

print(df.duplicated().to_string())      # no duplicati

tipo = df.groupby('Type 1')['Type 1'].count()   # quanti per ogni tipo
print(tipo)

leggendari = (df['Legendary'] == True).sum()    # pokemon leggendary sono 65
print(leggendari)

leggendari_grass = df[(df['Type 1'] == 'Grass') & (df['Legendary'] == True)].shape[0]   # tipo 1 grass leggendari
print(leggendari_grass)

leggendari_grass = df[(df['Type 1'] == 'Ice') | (df['Type 1'] == 'Fire') & (df['Legendary'] == True)].shape[0]  # tipo 1 ice o fire leggendari
print(leggendari_grass)

print(df.sort_values('Name'))   # ordinaro per la colonna Name

# df = df.set_index('Name')   # trasformo il name in indice
# print(df)

D_in_Name = df['Name'].str.contains('D', case=False)
print(D_in_Name)

generazione1 = df[(df['Generation'] == 1)&(df['Attack'] > 50) & (df['HP'] < 60)].shape[0]  # genrazione 1 con attacco > 50 e HP < 60
print(generazione1)

valori_nulli = df.isnull().sum()
print(valori_nulli)