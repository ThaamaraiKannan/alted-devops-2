import requests
import json

def api_call():
    key = "475f71268bfe4af89fd65418242803"
    city = "karaikudi"
    data = f"http://api.weatherapi.com/v1/current.json?q={city}&aqi=yes&key={key}"
    response = requests.get(url=data)
    response_txt = response.text
    response_json = json.loads(response_txt)
    print("You are looking for the city : " , response_json["location"]["name"], "," ,response_json["location"]["region"])
    print("The Current Temp in Celcius : " , response_json["current"]["temp_c"])
    print("Current weather condition : " , response_json["current"]["condition"]["text"])
    return

api_call()