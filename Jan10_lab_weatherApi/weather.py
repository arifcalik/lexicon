import requests
import json
from urllib.request import urlopen


def get_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    MY_CITY = data['city']
    print(data['city'])
    return data


def collect_weather_data(loc):
    api_key = "Enter your API key here"
    
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    #retrieve latitude and longtitude from location
    location = [float(coord) for coord in loc['loc'].split(',')]
    lat = location[0]
    lng = location[1]
    units = 'metric'

    complete_url = f"https://api.openweathermap.org/data/2.5/weather?&units={units}&lat={lat}&lon={lng}&appid={api_key}"
    # print(complete_url)

    #send request to weatherapi and get reply
    response = requests.get(complete_url)
    result = response.json()
    return result    


def display_report(res):
    # Result contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # location is not found
    if res["cod"] != "404":
        report_main = res["main"]

        current_temperature = report_main["temp"]
        current_pressure = report_main["pressure"]
        current_humidity = report_main["humidity"]
        report_desc = res["weather"]
        weather_description = report_desc[0]["description"]
    
        print("Temperature (in celcius unit) = " +
                        str(current_temperature) +
            "\nAtmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\nHumidity (in percentage) = " +
                        str(current_humidity) +
            "\nDescription = " +
                        str(weather_description))
    else:
        print("Location Not Found or Communication error with the server")


def main():
    reply = collect_weather_data(get_location())
    display_report(reply)

    
if __name__=="__main__":
    main()