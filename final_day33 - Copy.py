import requests
from datetime import datetime
from final_email_sender import Email_Notify

MY_LAT = #your address latitute 
MY_LONG = # you address longitute
email = Email_Notify(message="Subject:This is ISS notification message\n\n Look at the sky to see the ISS")

def is_iss_close():
    #getting api info from iss api
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # getting specific info from parced data
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= 42 <= MY_LAT+5 and MY_LONG-5 <= 74 <= MY_LONG+5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    #getting sunrise and sunset info from api
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Adjusting for local time (UTC+5)
    utc_offset = 5
    sunrise_local = (sunrise + utc_offset) % 24
    sunset_local = (sunset + utc_offset) % 24
    time_now = datetime.now()

    if time_now.hour >= sunset_local or time_now.hour <=sunrise:
        return True


if is_iss_close() and is_night_time():
    email.send_email()



# BONUS: run the code every 60 seconds.



