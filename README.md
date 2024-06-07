# Space-over-head

A simple web application based on Streamlit, useful to see the number of satellites over your head.

## How it work

The app have a python backend, with a call of [N2YO API](https://www.n2yo.com/api/).
It use Pandas to define a dataframe based on the json response of the Interrogation of API.
You can insert your location and the app retrive the latitide and the longitude using the [Nominatim](https://nominatim.org/) geocoder of OpenStreetMap.