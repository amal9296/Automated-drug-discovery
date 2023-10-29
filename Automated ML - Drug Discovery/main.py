# import libraries
import pandas as pd
from df_techniques import table
from descriptor_generator import descriptor



# load data

df = pd.read_csv('input.csv')
data = table(df)                                     # initialised dataframe
print(data.df_show())                                # visualising dataframe
print(data.null())                                   # give basic deatils on null,unique values
data1 = data.dup_remove('Ligand SMILES')
print(data1)
print('---------------------------------------------------------------------------------------------------------------------')



# descriptor generator

gen = descriptor(data1)
gen.smily_sort()                                    # sorting data frame based on smily string
gen.des()                                           # generating descriptor
data2 = gen.des_df()                                # creating final dataframe
print(data2)
print('---------------------------------------------------------------------------------------------------------------------')



# cleaning generated data

des_data = table(data2)
print(des_data.null())
des_data.drop_nul_col(10)
des_data.fill()
data3 = des_data.ret()
print(data3)
