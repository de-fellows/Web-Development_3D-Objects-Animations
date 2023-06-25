import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import codecs

def design_3d(design_html, width = 600, height= 400):
    d_file = codecs.open(design_html,'r')
    page = d_file.read()
    html(page, width = width, height = height, scrolling = True)


st.set_page_config(page_title='MY WEBSITE', layout='wide')

# Create a sidebar
with st.sidebar:    #Creates a sidebar for User-Interaction 
    selected = option_menu("Menu", ["Home","About Us", 'Data'], #set options and add icons to the menu bar
    icons=['house','person', 'gear'], menu_icon="cast", default_index=1,orientation= 'vertical')
    selected

# Create the main content area
if selected == "Home":
    st.title('3D Objects and Animation')
    design_3d('index2.html')

