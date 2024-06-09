import streamlit as st
import pandas as pd
from space import get_coordinates, get_satellites

DEFAULT_LOCATION= "Torino"

def satellites():
    print (f"Call API with location {location}")
    if 'location' not in st.session_state:
        st.session_state.location = DEFAULT_LOCATION
    else:
        if (len(st.session_state.location) == 0):
            #using default location if user done an empty search
            location= DEFAULT_LOCATION
    address,lat,lng = get_coordinates(st.session_state.location)
    satellites_info = get_satellites(lat,lng)
    n_of_satellites = satellites_info['info']['satcount']
    df = pd.json_normalize(satellites_info['above'])
    df['satid'] = df['satid'].apply(str)
    df['info'] = 'https://www.n2yo.com/satellite/?s='+ df['satid']
    st.write("Your (more detailed) location:", address)
    st.subheader(f":satellite: Number of satellites over your head: {n_of_satellites}")
    st.write("Complete list of satellites")
    st.dataframe(
        df,
        column_config={
            'info': st.column_config.LinkColumn('info'),
        },
        hide_index=True,
)


st.header(f":milky_way: Space over your head")
st.text_input("Enter your location to know the list of satellites over your head in this moment", placeholder="Torino", max_chars=30, on_change= satellites, key='location')