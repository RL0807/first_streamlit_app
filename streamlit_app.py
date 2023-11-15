import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spainach & Rocket Smoothie')
streamlit.text('🐔Head-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_first_list = pandas.read_csv("https://uni-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.datafrme(my_first_list)
