import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from df_techniques import table
from descriptor_generator import descriptor

# Title
st.title("Drug discovery on your Finger Tip")

# Header
st.header("A platform analysing and generating descriptors") 
 
# Subheader
st.subheader("a padel based approach")


# Text
st.text("Hello chem aspirants!!!")

img = Image.open("intro.gif")
st.image(img, width=800)
st.write('Upload the data (.csv formats only)')
file = st.file_uploader("upload file", type={"csv", "txt"})
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.style.highlight_max(axis=0))
    st.write('The shape of the dataframe is',df.shape)
    data = table(df)                                     # initialised dataframe
    #print(data.df_show())                                # visualising dataframe
    
    if(st.button("Find dataframe status")):
        st.dataframe(data.null())
    if st.checkbox("Show/Hide additional settings"):
 
    # display the text if the checkbox returns True value    
        

        if(st.checkbox("Press me to avoid duplicates in smily string")):
            df = data.dup_remove('Ligand SMILES')
            st.dataframe(df)
            st.write('The shape of the dataframe is',df.shape)
    st.header('Descriptor generation')
    #st.dataframe(df)
    #st.write('The shape of the dataframe is',df.shape)
    
    #data1 = data.dup_remove('Ligand SMILES')

    gen = descriptor(df)
    gen.smily_sort()
    low_limit = int(st.text_input('enter the starting value','0'))
    up_limit = int(st.text_input('enter the end value','10'))
    if(st.checkbox('proceed descriptor generation')):
       gen.des(low_limit,up_limit)
       descr = gen.des_df(low_limit,up_limit)
       st.dataframe(descr)
       st.write('The shape of the dataframe is',descr.shape)
       #desc.to_csv('a.csv')
       file_name = st.text_input('enter the file name','file_name.csv')
       
    if (st.checkbox('Download csv')):
        descr.to_csv(file_name)
    


    des_data = table(pd.read_csv('file_name.csv'))
    print(des_data.null())
    des_data.drop_nul_col(10)
    des_data.fill()
    data3 = des_data.ret()
    print(data3)
    
    
    
    
    
    
    
    
    if(st.checkbox('proceed with whole dataframe')):
       gen.des(0,len(df['Ligand SMILES']))
       desc = gen.des_df(low_limit,up_limit) 
       st.dataframe(desc)
       st.write('The shape of the dataframe is',desc.shape)
 
    
     
    
       

