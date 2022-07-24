from matplotlib import image
import streamlit as st
import streamlit as st
import webbrowser
import pandas as pd


st.image(image="image.jpg")
st.title(" StreamLit Test App ")

st.header("Q&A")
st.write("""
---------------------------------------------------------------------------------
# What is StreamLit Test App?
Well as I am trying streamlit for the very first time so i created a test app to get the better understanding of it.
# What does StreamLit Test App do?
As I am making this app for my better understanding I just added a bunch of random stuff to it. The add (nothing very complecated) stuff stays only in the domain of the streamlit
# What are your thoughts on streamlit?
It is a very good framework. As I do projects in machine learning and deep learning it certainly help me to build a effective and well functioning app quickly which allows me to work more on the core of the project.  
# Will you recommend using streamlit?
Without a dought. It is one of the best framework out there and it make it easier to build machine learning apps and most importantely it is very easy to get started with. 
""")
st.write("""-----------------------------------------------------------------""")


st.header("Selection Box")
selectionvalue = st.selectbox("Select a catagory", ("Space","Computer Science","Robotics","Biology"))
st.write("""Selected Catagory """,selectionvalue)


st.write("""--------------------------------------------------------------------""")

st.header("Look at the left side it is a sidebar having a selction box")
st.write("We can add multiple and different types of widgets there.")
st.sidebar.selectbox("Select a value", ("1","2","3","4"))

st.write("""--------------------------------------------------------------------""")

st.header("Sliders")

slidervalue = st.slider("Slider Demo 1")
st.write("Slider value is",slidervalue)

slidervalue2 = st.slider("Slider Demo 2",1,50)
st.write("Slider value is(custom min max value):",slidervalue2)

slidervalue3 = st.slider("Slider Demo 3",1,200,50)
st.write("Slider value is(it have a default value of 50):",slidervalue3)

st.header("Selct_Slider")
color = st.select_slider('Select a color ',options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('Selected color is:', color)

st.write("""--------------------------------------------------------------------""")

st.header("Text Input and Number Input")

ti1 = st.text_input("Text Input1")
st.write('Entered text is:', ti1)

ti2 = st.text_input("Text Input2",placeholder="Hello there")
st.write('Entered text is(this have place holding text):', ti2)

ti3 = st.text_input("Text Input2",max_chars=5,placeholder="Hello there")
st.write('Entered text is(this have a max char length of 5):', ti3)

ni1 = st.number_input("Number Input1")
st.write('Entered number is:', ni1)

ni2 = st.number_input("Number Input2",min_value=10,max_value=99)
st.write('Entered number is(this have a min max value limit):', ni2)

ni3 = st.number_input("Number Input3",min_value=0,max_value=1000,step=100)
st.write('Entered number is(this have a stepping interval of 100):', ni3)

st.write("""--------------------------------------------------------------------""")

st.header("Buttons")

st.write("Normal Button nothing new")
b1 = st.button("Button1")

st.write("Button with help/tip hover on it")
b2 = st.button("Button2",help="help or tip will displayed here")

st.write("Buttons with a action")
b3 = st.button("Button3")

if b3:
    st.write("The purpoes of my existence is to pass butter :-(")

url = 'https://docs.streamlit.io/'

b4 = st.button('Documentation')
if b4:
    webbrowser.open_new_tab(url)


st.write("""--------------------------------------------------------------------""")

st.header("Camera")

st.write("Say Hello to the camera")
st.warning("!You have to allow the camera access to view this feature!")

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)

st.write("""--------------------------------------------------------------------""")

st.header("Media")

st.write("An Image")
st.image("https://images.immediate.co.uk/production/volatile/sites/4/2020/08/GettyImages-91354007-768e5d8.jpg?quality=90&webp=true&crop=3px,170px,934px,402px&resize=940,400")

st.write("An Video")
st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw")


st.write("""--------------------------------------------------------------------""")


st.header("Data Display")

DataFrame = pd.DataFrame({
     'first column': [1, 2, 3, 4, 5],
     'second column': [10, 20, 30, 40, 50],
 })
st.experimental_show(DataFrame)

st.write("""--------------------------------------------------------------------""")

st.write("# YAY!! You reached here .I have got a Surprise for you.")

Surprise = st.button('Surprise')
if Surprise:
    st.balloons()
    st.write("That all for the steamlit test app. Please remember this app is made up for understanding the streamlit framework and its components(only the limited amount/most used features are presented here.")
    st.write("I hope you got some idea how streamlit feels and work. I recommend you to go throught the official streamlit documentation by your self for more understanding.")
    st.write("See you around Traveller.")