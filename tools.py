import requests


def get_coordinates(city):


    url = "https://geocoding-api.open-meteo.com/v1/search"


    params = {


        "name": city,

        "count": 1,

        "language": "en",

        "format": "json"


    }



    response = requests.get(

        url,

        params=params

    )


    data = response.json()



    if "results" not in data:


        return None



    location = data["results"][0]



    return {

        "name":
        location["name"],


        "latitude":
        location["latitude"],


        "longitude":
        location["longitude"]

    }







def get_weather(city):


    print(
        "Weather tool called:",
        city
    )



    try:


        location = get_coordinates(city)



        if location is None:


            return "City not found."




        latitude = location["latitude"]


        longitude = location["longitude"]





        url = (

        "https://api.open-meteo.com/v1/forecast"

        )





        params = {


            "latitude":
            latitude,


            "longitude":
            longitude,


            "current_weather":
            "true"

        }





        response = requests.get(

            url,

            params=params

        )



        data = response.json()





        weather = data["current_weather"]






        return f"""

Weather Report


City:
{location["name"]}


Temperature:
{weather["temperature"]} °C


Wind Speed:
{weather["windspeed"]} km/h


Weather Code:
{weather["weathercode"]}


"""



    except Exception as e:


        return str(e)