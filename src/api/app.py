#!/usr/bin/env python3
import connexion

def get_weather(location):
    mock_weather_data = {"New York": "Sunny, 25C", "London": "Cloudy, 18C", "Tokyo": "Rainy, 22C"}
    weather = mock_weather_data.get(location, "Weather data not available for this location.")
    return { "weather": weather }

def get_controller_function(operation_id):
    match operation_id:
        case 'getWeatherForecast':
            return get_weather
        case _:
            raise ValueError(f"Operation ID '{operation_id}' not found in controllers")

connex_app = connexion.App(__name__, specification_dir='./')

connex_app.add_api('api.json', 
                   validate_responses=True,
                   resolver=connexion.Resolver(get_controller_function))
