# importing libraries
import pandas as pd
from padelpy import from_smiles
import streamlit as st
import time



class descriptor():
    def __init__(self,df):
        self.df = df

    # solving complexity of smily string generation by sorting dataframe according to the complexity of smily
    def smily_sort(self):
        self.df['smile_len']  = [len(self.df['Ligand SMILES'][i]) for i in range(len(self.df['Ligand SMILES']))]
        self.df = self.df.sort_values(by = 'smile_len', ascending = 1).reset_index(drop = True)
        self.df = self.df.drop(columns = 'smile_len')
        print(self.df)

    # descriptor generation
    def des(self,low_limit,up_limit):
        'Starting a long computation...'

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)
        k = 0
        for i in range(low_limit,up_limit):
            # Update the progress bar with each iteration.
            
            self.id_with_no_descriptor = []
            try:
                a = from_smiles(self.df['Ligand SMILES'][i], output_csv = 'out_'+str(i)+'_.csv' )
                print(i,'----- try -----')
            except RuntimeError:
                print(i,'----- except -----',df['Ligand SMILES'][i])
                self.id_with_no_descriptor.append([i,self.df['BindingDB Reactant_set_id'][i]])
            
            bar.progress(k* int(100/(up_limit-low_limit))+ int(100/(up_limit-low_limit)))
            latest_iteration.text(f'completed task - {k+1}')
            time.sleep(0.1)
            k = k +1
    

    # creating dataframe using gnerated .csv files
    def des_df(self,low_limit,up_limit):
        self.csv_collection = [pd.read_csv('out_'+str(i)+'_.csv') for i in range(low_limit,up_limit)]
        #st.write(self.csv_collection)
        self.df1 = self.df.drop([i[0] for i in self.id_with_no_descriptor]).reset_index(drop = True)
        #st.write(self.df1)
        desdf = pd.concat(self.csv_collection).reset_index(drop = True)
        #st.write(desdf)
        df_out = pd.concat([self.df1[['BindingDB Reactant_set_id', 'Ligand SMILES']][low_limit:up_limit].reset_index(drop = True),desdf],axis = 1)  
        return df_out        
        

