import streamlit as st

#header
st.header('callback example')

#subheader
st.subheader('distance converter')

#function defingfor on_change
def km_to_miles():
 st.session_state.miles=st.session_state.km*1.609

def miles_to_km():
  st.session_state.km=st.session_state.miles*0.621


#defining columns
col1,buffer,col2 =st.columns([2,1,2])

with col1:
 km=st.number_input('Km',key='km',on_change=km_to_miles)

with col2:
 miles=st.number_input('Miles',key='miles',on_change=miles_to_km)


 