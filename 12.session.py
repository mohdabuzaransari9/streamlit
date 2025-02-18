#session 
#think of it as a dctonary


import streamlit as st

st.title('session')

st.write(st.session_state)

#session is a python object


if 'counter' not in st.session_state:

    st.session_state['counter']=0

else:
    st.session_state.counter+=1
    


    
st.write(f'counter : {st.session_state.counter}')