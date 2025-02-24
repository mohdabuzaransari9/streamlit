
#session 
#think of it as a dictionary


import streamlit as st

st.title('session')



#session is a python object 


if 'counter' not in st.session_state:

    st.session_state['counter']=0

else:
    st.session_state.counter+=1
    
    
#session ki state    
st.write(st.session_state)

#display counter value
st.write(f'counter : {st.session_state.counter}')


#press r on keyboard to rrun and increment the counter

# creating button
button=st.button('update state')

#putting clicks in session_state
if 'clicks' not in st.session_state:

    st.session_state['clicks']=0

#button action
if button:
    st.session_state['clicks']+=1
    f'{st.session_state}'


    #creating slider

number=st.slider('value',1,10,key='my_slider')
st.write(f'{st.session_state}')
st.write(number)