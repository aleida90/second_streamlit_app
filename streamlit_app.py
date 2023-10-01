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

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  

streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice=streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
   streamlit.error("Please select a fruit to get info")
  else:
   from_back_function:get_fruitvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.write('The user entered',fruit_choice)

streamlit.header("The fruit list contains:")

#fucntion to get fruits from db
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   streamlit.dataframe(my_data_rows)



def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list_values values('"+new_fruit+"')")
      return "Thanks for adding "+new_fruit;
      
add_a_fruit=streamlit.text_input('What fruit would you like to add?')

if(streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_snowflake(add_a_fruit)
   streamlit.text(back_from_function)

streamlit.stop()
