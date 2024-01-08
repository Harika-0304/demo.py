import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./Persian.jpeg",caption="Persian Cat",width=300,use_column_width=True)
  st.write("Persian Cats are Cute")

with col2:
  st.subheader("Rangdoll Cat")
  st.image("./rangdoll.jpeg",caption="Rangdoll Cat",width=300,use_column_width=True)
  st.write("Rangdoll Cats are proud")
