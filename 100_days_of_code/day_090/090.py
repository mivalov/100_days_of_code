# Day 90: JSON
import requests


def main() -> None:
    url = 'https://randomuser.me/api/?results=10'
    # API docs: https://randomapi.com/documentation
    # it's essential to use as few requests as possible for most optimal effect
    response = requests.get(url)
    if response.status_code == 200:
        print('Successful response!')
        response_json = response.json()
        results = response_json.get('results', {})
        for user in results:
            first_name = user.get('name', {}).get('first', '')
            second_name = user.get('name', {}).get('last', '')
            output_file = f'{first_name}_{second_name}.jpg'
            picture_url = user.get('picture', {}).get('medium', '')
            if 'https://' in picture_url:
                picture = requests.get(picture_url)
                with open(output_file, 'wb') as file:
                    # store as bytes
                    file.write(picture.content)
                print(f'Successfully downloaded {output_file}')
    else:
        print(f'{url} delivers {response.status_code} as status code..')


if __name__ == '__main__':
    main()
