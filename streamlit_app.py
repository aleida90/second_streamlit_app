import streamlit
import pandas

streamlit.title('My Parents new healthy dinner!')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Bluebery Oatmeal')
streamlit.text('🥗Kale, spinach, & Rocket smoothie')
streamlit.text('🐔Hard-boiled free-range egg')
streamlit.text('🥑🍞Avocado toast')

streamlit.header('🏋️‍♀️Fitness Menu (an extra portion of protein!)')
streamlit.text('🍗🥗chicken with salad')
streamlit.text('🥩🍚 meat and rice')

streamlit.header('🍇🍈🍉Build your own smoothie🍒🥝🍎🍍')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
