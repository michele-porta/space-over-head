# Space-over-head

A simple web application useful for seeing the number and information on satellites over your head.

![example](images/result%20example.png)

## How it works

The app has a python backend, with a call of [N2YO API](https://www.n2yo.com/api/).
It use the Pandas library to define a dataframe based on the json response of the interrogation of API.

You can insert your location and the app retrieve the latitude and the longitude using the [Nominatim](https://nominatim.org/) geocoder of OpenStreetMap.

The application is based on [Streamlit](https://streamlit.io/), an interesting open-source Python framework useful for creating interactive web applications based on data.

Here the link to access to the interactive web page demo: https://space-over-your-head.streamlit.app/

## How to use in local
You can clone the repo, install all the dependencies in *requirements.txt* file and create an *.env* file with your API key obtained from N2Y0.

You obviously have to decomment the coding part relative to the readings of the env variable from os and comment the coding part relative to the reading of the env variable from streamlit environment.