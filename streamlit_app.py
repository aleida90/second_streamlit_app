import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

try:
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi');
 if not fruit_choice:
   streamlit.error("Please select a fruit to get info")
 else:
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

streamlit.write('The user entered',fruit_choice)




streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur2 = my_cnx.cursor()
my_cur2.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
my_data_rows=my_cur2.fetchall();
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_rows)

add_a_fruit=streamlit.text_input('What fruit would you like to add to the list?');
my_cur3 = my_cnx.cursor()
my_cur3.execute(" INSERT INTO pc_rivery_db.public.fruit_load_list VALUES( '"+add_a_fruit+"')")
streamlit.write('Thanks for adding',add_a_fruit)

