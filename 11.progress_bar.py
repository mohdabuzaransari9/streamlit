import streamlit as st

st.write('starting computing.............')


#single element container to store latest iteration
latest_iteration=st.empty()

#text to see when progress bar initialize
progress_text='in progress.............'

#creating bar
#means zero se start karo aur text yeh rakho
my_bar=st.progress(0,text=progress_text)

#using import time for sleep

import time

# sleep for showing in progesss how much time in progress will show
time.sleep(4)


#creating a for loop to update progress bar
# from 0 to the defined range
#also we already sart from zero our progress bar


for i in range(100):
    my_bar.progress(i+1)
    #empty container ke andar jo text value h iteration ki woh bhi
    #increment kar lo yeh as a parameter hoti h
    latest_iteration.text(f'iteration loading {i+1}%')
    time.sleep(0.2)

st.write('done :+1:')


