import streamlit as st
import pandas as pd
from space import get_coordinates, get_satellites

DEFAULT_LOCATION= "Torino"
loc= DEFAULT_LOCATION

def satellites(location):
    if (len(location) == 0):
        #using default location
        location= DEFAULT_LOCATION
    address,lat,lng = get_coordinates(location)
    st.write("Your (more detailed) location:", address)
    satellites_info= get_satellites(lat,lng)
    st.subheader(f":satellite: Number of satellites over your head: {satellites_info['info']['satcount']}")
    df = pd.json_normalize(satellites_info['above'])
    st.write("Complete list of satellites")
    df['satid']= df['satid'].apply(str)
    df['info']= 'https://www.n2yo.com/satellite/?s='+ df['satid']
    st.dataframe(
    df,
    column_config={
        'info': st.column_config.LinkColumn('info'),
    },
    hide_index=True,
)

st.header(f":milky_way: Space over your head")
loc = st.text_input("Enter your location to know the list of satellites over your head in this moment", placeholder="Torino", max_chars=50, on_change= satellites(loc))