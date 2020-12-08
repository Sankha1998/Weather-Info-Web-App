from flask import Flask,render_template,request,make_response,redirect,Response
from webscraping import Web_Scraping
import pandas as pd



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
    time, temp_d, humidity, precipitation = city_weather_info.city_scraping(
        city=city_name)
    data = {'time': time,'temperature': temp_d,'humidity':humidity,'precipitation':precipitation}

    df = pd.DataFrame(data)
    filename = city_name + '.csv'
    return Response(
        df.to_csv(index=False),
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename={}".format(filename)})


if __name__=="__main__":
    app.run(debug=True)




