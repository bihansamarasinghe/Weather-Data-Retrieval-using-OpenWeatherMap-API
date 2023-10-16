---

# OpenWeatherMap Weather Fetcher

This Python script allows users to fetch weather data for a specified city using the OpenWeatherMap API. The script uses the `requests` module to make HTTP requests and obtain weather information, including the weather condition and temperature in degrees Celsius.

## How it Works

1. The user is prompted to enter a city.

2. The script constructs a URL to the OpenWeatherMap API with the specified city and the API key.

3. A GET request is sent to the OpenWeatherMap API using `requests.get(url)`.

4. The API response, containing weather information in JSON format, is processed.

5. The weather condition (e.g., sunny, rainy) and temperature are extracted from the response.

6. The weather condition and temperature (in degrees Celsius) are displayed to the user.

## Usage

1. Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key in the `api_key` variable.

2. Run the script using a Python interpreter.

3. Enter the desired city when prompted.

4. View the weather condition and temperature for the specified city.

## Dependencies

- `requests`: Used to make HTTP requests to the OpenWeatherMap API.

## Configuration

Replace `'YOUR_API_KEY'` in the `api_key` variable with your actual OpenWeatherMap API key.

```python
api_key = 'YOUR_API_KEY'
```

## Example

```python
Enter City: London
Weather: Clouds
Temperature: 12°C
```

## Contributing

Contributions and feedback are welcome! If you'd like to contribute or have suggestions, please open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
