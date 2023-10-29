# importing libraries
import pandas as pd
import numpy as np
from padelpy import from_smiles

'''df = pd.read_csv('input.csv')
print(df)'''
#print(df)
#print(df['Ligand SMILES'].unique())

#[[len(df[i].unique()),(len(df[i].unique())/len(df[i]))] for i in df.columns]
#[[i,i+1] for i in range(5)]

#print( [ [ len(df[i].unique()),  round( ( ( len(df[i].unique()) / len(df[i]) ) * 100 ),2 ) ] for i in df.columns ] )
#print(df.drop_duplicates(subset='Ligand SMILES',keep='first'))

#for i in df['IC50 (nM)']:
    #print(type(i))

#[i for i in range(10) if i > 5] 
#[i for i in range(len(df['IC50 (nM)']))]   

#from df_techniques import table
#from padelpy import from_smiles
#from_smiles(df['Ligand SMILES'][2155:].to_list(), output_csv='a.csv')
#for i in range(15):
 #   try:
  #      print(10000000000000000000000000000000000**i)
#a = from_smiles(df['Ligand SMILES'][0],output_csv='b')
'''for i in [10,12,15,0,1,5,6]:
    try:
        b = 15/i
        print(i,'----- try -----',b)
    except ZeroDivisionError:
        print(i,'----- except -----',b)
        continue'''

'''for i in range(0,100):
    id_with_no_descriptor = []
    try:
        a = from_smiles(df['Ligand SMILES'][i], output_csv = 'out_'+str(i)+'_.csv' )
        print(i,'----- try -----')
    except RuntimeError:
        print(i,'----- except -----',df['Ligand SMILES'][i])
        id_with_no_descriptor.append([i,df['BindingDB Reactant_set_id'][i]])

a = from_smiles(df['Ligand SMILES'][0])
b = from_smiles(df['Ligand SMILES'][1])
c = from_smiles(df['Ligand SMILES'][2])
print(a)
print(len(a),len(b),len(c))'''

df = pd.read_csv('df_merg_eda.csv')
'''for i in df.columns:
    if df[i].dtype == object:
        print(i)'''

print(df)
num = []
for i in df.columns:
    if df[i].dtype != object:
        num.append(i)


a = df[num].corrwith(df['IC50 (nM)'])
print(a)
x = np.array([i for i in range(1,len(num)+1)])
for i in a:
    print(i)

print(df[num].describe())


