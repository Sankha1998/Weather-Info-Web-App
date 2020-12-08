

# Weather-Info-Web-App : [view](https://weather-info.herokuapp.com/ )

Weather Info,a web app buid in python flask, provides services related to the predictions of weather in different cities in India as well as in some foreign cities. And it's provides weather data in CSV format.


![Screenshot](webapp_view.gif)

## Part 1: Web scraping

Weather data has been scraped from [timeanddate](https://www.timeanddate.com) and this particular step is done every day to get the predicted weather data for the next 24 hours.
[webscraping.py](https://github.com/Sankha1998/Weather-Info-Web-App/blob/main/webscraping.py) contains all the required codes for scraping worldwide weather information data of famous cities.
On the other hand, Indian city-wise data is first getting stored in CSV format in a separate [dash app](https://weatherinfo-ssm.herokuapp.com/).

All the predicted weather data of popular Indian cities, stored in CSV format also available for download.

## Part 2: Web App Making 

World wide predicted weather report is getting scraped and visualized in a table when a user is requesting to view the data in the web app instantly. But in the case of Indian cities data, it's reading from a CSV file as mentioned above. Now, this web app is made in flask and dash [see]https://github.com/Sankha1998/weather-info-dash-app). The dashboard of Weather Prediction in Indian cities has built using Plotly-dash and deployed in Heroku separately. The remaining part of this web app is built in python-flask micro-framework.

## Part 3: Deployment

The entire web is again deployed in Heroku.


