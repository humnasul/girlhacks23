import streamlit as st

st.set_page_config(page_title="testing webpage", page_icon=":tada:", layout="wide")

st.subheader("testing")

label1 = "button1"
label2 = "button2"
label3 = "button3"
label4 = "button4"
label5 = "button5"
label6 = "button6"

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.button(label1, key="01", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col2:
    st.button(label2, key="02", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col3:
    st.button(label3, key="03", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

col1, col2, col3 = st.columns([2,2,2])

with col1:
    st.button(label4, key="04", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col2:
    st.button(label5, key="05", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col3:
    st.button(label6, key="06", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)