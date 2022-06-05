import requests
from datetime import datetime
import smtplib
MY_LAT = 28.759050 # found using latlong.net
MY_LNG = -81.317810

# Check if ISS is overhead or not
def is_iss_overhead():
    # get the ISS position
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # TODO: Our current position is within +5 or -5 degrees of the ISS position
    if MY_LAT-1 <= iss_latitude <= MY_LAT+5 and MY_LNG-1 <= iss_longitude <= MY_LNG+5:
        return True

# Check if it is night time
def is_night():
    # this api requires parameters
    # parameters are passed using a dictionary
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0, #optional # gives a 24 hour format time
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    # We can also pass parameters as below , below can also be used directly on search engine
    # response = requests.get(url="https://api.sunrise-sunset.org/json?lat=28.759050&lng=-81.317810")
    # raise exception if there is an error
    response.raise_for_status()

    # we get back data from api as a json file
    data = response.json()
    sunrise = data["results"]["sunrise"] # gives 12 hour format
    sunset = data["results"]["sunset"]

    # separating the output to get the hour from e.g 2022-06-04T10:25:33+00:00
    # to get the actual hour from the 24 hour clock
    sunrise_in_24_hr = int(sunrise.split("T")[1].split(":")[0])
    sunset_in_24_hr = int(sunset.split("T")[1].split(":")[0])

    # Calculate the current clock time in terms of 24 hr clock
    time_now = datetime.now().hour

    if time_now >= sunset_in_24_hr or time_now <= sunrise_in_24_hr:
        # It's dark
        return True


# Send a mail if it is night time and iss is overhead
if is_night() and is_iss_overhead():
    connection = smtplib.SMTP('smtp.gmail.com')
    # make connection secure
    connection.starttls()
    # login
    connection.login("sass@gmail.com",password="absbs")
    connection.sendmail(
        from_addr="sass@gmail.com",
        to_addrs="sass@gmail.com",
        msg="Subject:look Up\n\n The ISS is above you in the sky."
    )

