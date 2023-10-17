# Import the requests library, which allows making HTTP requests
import requests

# Store the API key from OpenWeatherMap
api_key = 'YOUR_API_KEY'

# Prompt the user to enter a city and store the input
user_input = input("Enter City: ")

# Make an HTTP GET request to the OpenWeatherMap API to retrieve weather data for the user-inputted city
# Construct the API URL with the user-inputted city and the API key
weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

# Check if the request was successful (status code 200)
if weather_data.status_code == 200:
    # Parse the response data as JSON
    weather_json = weather_data.json()
    
    # Extract the main weather description
    weather = weather_json['weather'][0]['main']
    
    # Extract the temperature in Kelvin and convert it to Celsius
    temp = weather_json['main']['temp']
    celsius_temp = round(temp - 272)  # Convert from Kelvin to Celsius
    
    # Print the weather and temperature for the user-inputted city
    print(f"Weather in {user_input}: {weather}")
    print(f"Temperature in {user_input}: {celsius_temp}°C")
else:
    # If the request was not successful, print an error message with the status code
    print(f"Failed to retrieve weather data for {user_input}. Status code: {weather_data.status_code}")
