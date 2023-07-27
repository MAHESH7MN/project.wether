import requests

from datetime import datetime


user_api=("b7378003383b8833cc007339bcc8119d")
location=input("\nEnter the city name\n")

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

complete_apilink="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link=requests.get(complete_apilink)
api_data=api_link.json()


if api_data['cod']=="404":
    print("Invalid City: {},please check your City name".format(location))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    #wether_description=api_data['wether'][0]['description']
     
    date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


    print("--------------------------------------------------------------------")
    print("wether Stats for-{}  || {}".format(location.upper(),date_time))
    print('---------------------------------------------------------------------')


    print("Current temprature is:{:.2f} deg c".format(temp_city))
    #dprint("Current wether description:",wether_description)