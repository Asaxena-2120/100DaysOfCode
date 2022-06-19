import requests
from datetime import datetime
import os

# Store your keys, tokens and password in environment variables
nutritionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("sheet_endpoint")
NUTRIONIX_API_KEY = os.environ.get("NUTRIONIX_API_KEY")
NUTRITIONIX_API_ID = os.environ.get("NUTRITIONIX_API_ID")
SHEET_USERNAME = os.environ.get("SHEET_USERNAME")
SHEET_PASSWORD = os.environ.get("SHEET_PASSWORD")
GENDER = "Female"
WEIGHT_KG = 67
HEIGHT_CM = 160
AGE = 31

nutritionix_headers = {
    "x-app-id":NUTRITIONIX_API_ID,
    "x-app-key": NUTRIONIX_API_KEY,

}
text = input("Tell me which exercises you did: ")
nutritionix_params = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=nutritionix_api_endpoint,json=nutritionix_params,headers=nutritionix_headers)
result=response.json()
print(result)
############Connecting with Sheety API to update our google sheet ###################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            SHEET_USERNAME,SHEET_PASSWORD
        )
    )

    print(sheet_response.text)

