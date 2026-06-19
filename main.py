import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPENWEATHER_API_KEY")
MY_EMAIL = "aldrinfrades8@gmail.com"
MY_PASSWORD = os.environ.get("EMAIL_PASSWORD")
OWM_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 12.879721,
    "lon": 121.774017,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_END_POINT, params=parameters)
response.raise_for_status()
status = response.status_code
data = response.json()
status_code = [code["weather"][0]["id"] for code in data["list"]]


def notify_user()-> bool:
    for code in status_code:
        if code < 700:
            return True
    return False

if notify_user():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="buzzaldrinastro08@gmail.com",
                            msg="Subject: IT WILL RAIN TODAY!\n\nplease bring an umbrella today")
