import streamlit as st
import pandas as pd
import numpy as np
import time

### Title
st.title("Drug discovery on your Finger Tip")

# Header
st.header("A platform analysing and generating descriptors") 
 
# Subheader
st.subheader("a padel based approach")


# Text
st.text("Hello chem aspirants!!!")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write text
st.write("Text with write")
 
# Writing python inbuilt function range()
st.write(range(10))

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("logo.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
 
    # display the text if the checkbox returns True value
    st.text("Showing the widget")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")    


# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby) 

# multi select box
 
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
 
# write the selected options
st.write("You selected", len(hobbies), 'hobbies')


# Create a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")


# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)    

# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)
 
# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))

spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    st.dataframe(spectra_df.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

'''st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.balloons()
st.snow()
st.warning('This is a warning', icon="⚠️")'''