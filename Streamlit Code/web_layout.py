import streamlit as st
from streamlit_option_menu import option_menu



# Set page title
st.set_page_config(page_title='MY WEBSITE', layout='wide')

# Create a sidebar
with st.sidebar:    #Creates a sidebar for User-Interaction 
    selected = option_menu("Menu", ["Home","About Us", 'Data'], #set options and add icons to the menu bar
    icons=['house','person', 'gear'], menu_icon="cast", default_index=1,orientation= 'vertical')
    selected

# Create the main content area
if selected == "Home":
    st.title('Welcome to My Webpage')
    

  
