import streamlit
import pandas
import requests

streamlit.title('My Parents new healthy dinner!')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Bluebery Oatmeal')
streamlit.text('🥗Kale, spinach, & Rocket smoothie')
streamlit.text('🐔Hard-boiled free-range egg')
streamlit.text('🥑🍞Avocado toast')

streamlit.header('🏋️‍♀️Fitness Menu (an extra portion of protein!)')
streamlit.text('🍗🥗chicken with salad')
streamlit.text('🥩🍚 meat and rice')

streamlit.header('🍇🍈🍉Build your own smoothie🍒🥝🍎')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!')


fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
streamlit.text(fruityvice_response)
