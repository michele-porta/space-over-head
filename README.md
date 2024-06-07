# Space-over-head

A simple web application useful to see the number and the information of satellites over your head.

## How it work

The app have a python backend, with a call of [N2YO API](https://www.n2yo.com/api/).
It use Pandas library to define a dataframe based on the json response of the interrogation of API.

You can insert your location and the app retrive the latitide and the longitude using the [Nominatim](https://nominatim.org/) geocoder of OpenStreetMap.

The application is based on [Streamlit](https://space-over-head.streamlit.app/), an interesting open-source Python framework useful to create interactive web application based on data.

Here the link to access to the interactive web page demo: https://space-over-head.streamlit.app/

## How to use in local
You can clone the repo, install all the dependencies in *requirements.txt* file and create an *.env* file with your API key obtained from N2Y0.

You have obviously to decomment the coding part relative to the readings of the env variable from os and comment the coding part relative to the reading of the env variable from streamlit environment.