from flask import Flask,render_template,redirect,request
import requests
from webscraping import Web_Scraping
import pandas as pd
import urllib
import json

app= Flask(__name__)

cities=['kolkata','agartala','bangalore','bhubaneswar','chennai',
        'delhi','hyderabad','indore','jaipur','kanpur','lucknow','mumbai','nagpur','nainital','noida','pune','surat','visakhapatnam']


@app.route('/')
def home():
    return render_template('index.html',cities=cities)


@app.route('/worldweather')
def worldweather():
    weatherinfo = Web_Scraping()
    countries, temp = weatherinfo.world_wide_scraping()
    sl_no=[]
    for i in range(1,len(countries)+1):
        sl_no.append(i)
    return render_template('worldweather.html',countries_temp=zip(sl_no,countries,temp))


@app.route('/cityreport')
def city_report():

    return redirect('https://weatherinfo-ssm.herokuapp.com/')

@app.route('/getdata/<string:city_name>')
def get_data(city_name):
    data_url = 'https://weatherinfo-ssm.herokuapp.com/static/data/{}.csv'.format(city_name)
    return redirect(data_url)

if __name__=="__main__":
    app.run(debug=True)




