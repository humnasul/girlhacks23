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

holder = 0
time1 = 0
time2 = 0
time3 = 0
time4 = 0
time5 = 0
time6 = 0

# modal = Modal(key="popup_text",title="button text")

if but1:
    with st.form(key = "Form 1"):
        st.markup("Goal #1")
        holder = 1
        name1 = st.text_input(":black[Enter a name for your goal :: ]")
        saved1 = st.number_input("Enter the amount of money saved for this goal :: ")
        # float
        time1 = st.number_input("Enter a timeframe for this goal in months :: ")
        # float

if but2:
    # with modal.container():
    holder = 2
    name2 = st.text_input(":black[Enter a name for your goal :: ]")
    saved2 = st.number_input("Enter the amount of money saved for this goal :: ")
    # float
    time2 = st.number_input("Enter a timeframe for this goal in months :: ")
    # float
if but3:
    holder = 3
    name3 = st.text_input(":black[Enter a name for your goal :: ]")
    saved3 = st.number_input("Enter the amount of money saved for this goal :: ")
    # float
    time3 = st.number_input("Enter a timeframe for this goal in months :: ")
    # float
if but4:
    holder = 4
    name4 = st.text_input(":black[Enter a name for your goal :: ]")
    saved4 = st.number_input("Enter the amount of money saved for this goal :: ")
    # float
    time4 = st.number_input("Enter a timeframe for this goal in months :: ")
    # float
if but5:
    holder = 5
    name5 = st.text_input(":black[Enter a name for your goal :: ]")
    saved5 = st.number_input("Enter the amount of money saved for this goal :: ")
    # float
    time5 = st.number_input("Enter a timeframe for this goal in months :: ")
    # float
if but6:
    holder = 6
    name6 = st.text_input(":black[Enter a name for your goal :: ]")
    saved6 = st.number_input("Enter the amount of money saved for this goal :: ")
    # float
    time6 = st.number_input("Enter a timeframe for this goal in months :: ")
    # float

# Create some data
sum = time1 + time2 + time3 + time4 + time5 + time6
# data = [10, 20, 30]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'goal1', 'goal2', 'goal3', 'goal4', 'goal5', 'goal6'
sizes = [1,1,1,1,1,1]
if sum != 0:
    sizes = [time1/sum, time2/sum, time3/sum, time4/sum, time5/sum, time6/sum]

explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)