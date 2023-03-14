# Day 92: Weather API
from urllib.parse import urlunsplit, urlencode

import requests


def get_weather_code(code: int) -> str:
    """Interpret the weather code and return its description

    Weather interpretation codes: https://open-meteo.com/en/docs
    """
    if code == 0:
        return 'Clear sky'
    elif code in [1, 2, 3]:
        return 'Mainly clear, partly cloudy, and overcast'
    elif code in [45, 48]:
        return 'Fog and depositing rime fog'
    elif code in [51, 53, 55]:
        return 'Drizzle: Light, moderate, and dense intensity'
    elif code in [56, 57]:
        return 'Freezing Drizzle: Light and dense intensity'
    elif code in [61, 63, 65]:
        return 'Rain: Slight, moderate and heavy intensity'
    elif code in [66, 67]:
        return 'Freezing Rain: Light and heavy intensity'
    elif code in [71, 73, 75]:
        return 'Snow fall: Slight, moderate, and heavy intensity'
    elif code == 77:
        return 'Snow grains'
    elif code in [80, 81, 82]:
        return 'Rain showers: Slight, moderate, and violent'
    elif code in [85, 86]:
        return 'Snow showers slight and heavy'
    elif code == 95:
        return 'Thunderstorm: Slight or moderate'
    elif code in [96, 99]:
        return 'Thunderstorm with slight and heavy hail'


def get_weather_data(timezone: str, lat: float, long: float) -> dict:
    """Extract weather data from a free weather API

    Documentation page: https://open-meteo.com/en/docs
    """
    scheme = 'https'
    weather_api = 'api.open-meteo.com'
    path = '/v1/forecast'
    query = {
        'latitude': lat,
        'longitude': long,
        'daily': 'weathercode,temperature_2m_max,temperature_2m_min',
        'timezone': timezone,
    }
    query = urlencode(query)
    fragment = ''
    url = urlunsplit((scheme, weather_api, path, query, fragment))
    response = requests.get(url)
    if response.status_code == 200:
        # print('Successful response')
        return response.json()
    else:
        print(f'Got an unexpected http status code {response.status_code}'
              f'from the URL: {url}')
        return dict()


def main() -> None:
    # timezone = 'GMT'
    timezone = 'Europe/Zurich'
    latitude = 47.36667
    longitude = 8.55
    weather_data = get_weather_data(timezone, latitude, longitude)
    if weather_data:
        weather_code = weather_data.get('daily', {}).get('weathercode', [])
        min_temp = weather_data.get('daily', {}).get('temperature_2m_min', [])
        max_temp = weather_data.get('daily', {}).get('temperature_2m_max', [])
        try:
            weather_code_today = weather_code[0]
            min_temp_today = min_temp[0]
            max_temp_today = max_temp[0]
        except IndexError:
            print('Got an IndexError while extracting the '
                  'weather code and temperatures.')
        else:
            print(
                f'{get_weather_code(weather_code_today)}',
                f'🥵: {max_temp_today}\t🥶: {min_temp_today}',
                sep='\n'
            )


if __name__ == '__main__':
    main()
