import streamlit as st
from streamlit_modal import Modal
import matplotlib.pyplot as plt

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
    but1 = st.button(label1, key="01", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col2:
    but2 = st.button(label2, key="02", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col3:
    but3 = st.button(label3, key="03", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

col1, col2, col3 = st.columns([2,2,2])

with col1:
    but4 = st.button(label4, key="04", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col2:
    but5 = st.button(label5, key="05", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
with col3:
    but6 = st.button(label6, key="06", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

modal = Modal(key="popup_text",title="button text")
if but1:
    with modal.container():
        st.markdown(":black[one]")

if but2:
    with modal.container():
        st.markdown('two')
if but3:
    with modal.container():
        st.markdown('three')
if but4:
    with modal.container():
        st.markdown('four')
if but5:
    with modal.container():
        st.markdown('five')
if but6:
    with modal.container():
        st.markdown('six')

# Create some data
data = [10, 20, 30]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)