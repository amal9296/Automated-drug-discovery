# df_techniques.py

# importing libraries
import pandas as pd
import numpy as np


# creating class for manipulating data frame
class table():
    def __init__(self,df):
        self.df = df # change it as inputting method
        self.df_copy = self.df.copy(deep = True)

    # visualize dataframe
    def df_show(self):
        print(self.df) 

    # null checking
    def null(self):
        
        null_val = pd.DataFrame({'column':[i for i in self.df.columns],
                                 'null_val (num , %)':[(self.df[i].isnull().sum(), round( ((self.df[i].isnull().sum()/len(self.df[i])) *100) ,2) ) for i in self.df.columns],
                                 
                                 'unique_val (num , %)':[ ( len(self.df[i].unique()),  round( ( ( len(self.df[i].unique()) / len(self.df[i]) ) * 100 ),2 ) ) for i in self.df.columns ]})
        
        return null_val

    # handling duplicated value by subset
    def dup_remove(self,column_name):
        self.df = self.df.drop_duplicates( subset = column_name, keep = 'first' ).reset_index(drop = True)
        return self.df
    
    # data type handling - complete after basic structure build
    # def type_converter(self):
        #self.lst_str_index = [i ]

    # calculating and dropping null columns
    def drop_nul_col(self,percent):
        drop_lst = []
        for i in self.df.columns:
            
            if (self.df[i].isnull().sum()/len(self.df[i]))*100 >= percent:
                drop_lst.append(i)
        self.df = self.df.drop(columns = drop_lst)   

    # filling missing values
    def fill(self):
        self.df = self.df.ffill() 
        self.df = self.df.bfill()

    # round values
    def rounder(self):
        for i in self.df.columns:
            if self.df[i].dtype != object:
                self.df[i] = round(self.df[i],2)        
    

    # function to return final data frame
    def ret(self):
        return self.df  

q = table(pd.read_csv('input.csv'))  
print(q.df_show())
q.drop_nul_col(50)
q.fill()
q.rounder()
print(q.ret())   
print(q.null())


