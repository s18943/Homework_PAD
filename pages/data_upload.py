import imp
import streamlit as st
import plotly.figure_factory as ff
from io import StringIO
import pandas as pd
import numpy as np
from time import sleep

DATE_COLUMN = 'sales'

@st.cache
def load_data(file):
    data = pd.read_csv(file, index_col=0)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

def Simple_bar_chart(data):
    st.subheader('Simple bar chart')

    st.bar_chart(data)

def Overlaping_hist(data):
    st.subheader('Overlaping hist')
    # Create distplot with custom bin_size
    fig = ff.create_distplot(data.T.values, data.columns)

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

def Line_chart(data):
    st.line_chart(data)

bar_options ={'Simple bar chart': Simple_bar_chart, 'Overlaping hist': Overlaping_hist, 'Line chart': Line_chart}

def app():
    global data
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Create a text element and let the reader know the data is loading.
        data_load_state = st.text('Loading data...')

        # Can be used wherever a "file-like" object is accepted:
        data = load_data(uploaded_file)
        # st.write(data)

        # Load 10,000 rows of data into the dataframe.
        # data = load_data(10000)

        # Notify the reader that the data was successfully loaded.
        data_load_state.text('Loading data...done!')

        data_load_state.text("Done! (using st.cache)")

        st.subheader('Raw data')
        st.write(data)

        option = st.selectbox(
            'How would you like to be contacted?',
            bar_options.keys())
        
        bar_options.get(option)(data)

       


       
