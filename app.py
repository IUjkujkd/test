from flask import Flask, render_template, request
import requests
from datetime import datetime
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route('/')
def home():
    x_time = [0, 1, 2, 3, 4, 5, 6]
    y_temp = [18, 15, 13, 9, 8, 8, 11]
    plt.plot(x_time, y_temp)
    plt.savefig("test_chart")
    return render_template('home.html')


@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = "290808586775338600ff6149740938ac"
    form_city = request.form.get("city")
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&appid=" + api_key
    response = requests.get(url).json()
    print(url)
    print(response)
    return render_template('results.html', response=response)


@app.route('/process', methods=["GET", "POST"])
def process():
    api_key = "290808586775338600ff6149740938ac"
    form_city = request.form.get("city")
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&appid=" + api_key
    response = requests.get(url).json()
    weather_list = response.get("weather", [{}])
    first_weather_dict = weather_list[0]
    description = first_weather_dict.get("description")
    city_name = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    timestamp_local = datetime.fromtimestamp(timestamp)
    temp_k = response.get("main", {}).get("temp")
    temp_c = int(temp_k) - 273.15
    wind_speed = response.get("wind").get("speed")
    dt = datetime.fromtimestamp(timestamp)
    temp_celcius = round(temp_c)
    country = response.get("sys", {}).get("country")
    dt_object = datetime.fromtimestamp(timestamp)
    info = [city_name, timezone, timestamp, timestamp_local, temp_k, temp_c, wind_speed]
    my_dict = {

    }
    print(my_dict)
    return render_template('process.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
