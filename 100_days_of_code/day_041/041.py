# Day 41: Website Rating

def main() -> None:
    print('🌟Website Rating🌟')
    website = {
        'website name': None,
        'URL': None,
        'description': None,
        'star rating out of 5': None
    }
    result = []
    for field in website.keys():
        print()
        website[field] = input(f'Enter {field}: ')
        result.append(f'{field}: {website.get(field)}')
    print()
    print(', '.join(result))


if __name__ == '__main__':
    main()
