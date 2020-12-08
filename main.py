from flask import Flask,redirect
from flask import render_template,request,make_response
from webscraping import Web_Scraping
import pandas as pd
import time
import lxml


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
    city_weather_info = Web_Scraping()
    new_time, temp_d, wind_speed, humidity, precipitation = city_weather_info.city_scraping(
        city=city_name)
    df = pd.DataFrame()
    df['time'] = new_time
    df['temperature'] = temp_d
    df['wind speed'] = wind_speed
    df['humidity'] = humidity
    df['precipitation'] = precipitation
    filename = city_name + '.csv'
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    resp.headers["Content-Type"] = "text/csv"
    return resp



if __name__=="__main__":
    app.run(debug=True)




