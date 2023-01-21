# Day 40: Contact Card

def main() -> None:
    msg = '🌟 Contact Card 🌟'
    print(msg, end='\n\n')
    data = dict()
    data['name'] = input('Input your name: ')
    data['birthdate'] = input('Input your date of birth: ')
    data['phone'] = input('Input your telephone number: ')
    data['email'] = input('Input your email: ')
    data['address'] = input('Input your address: ')

    contact_card = (
        f"\nHi {data.get('name')}. "
        f"Our dictionary says that you were born on {data.get('birthdate')}, "
        f"we can call you on {data.get('phone')}, email {data.get('email')}, "
        f"or write to {data.get('address')}"
    )
    print(contact_card)


if __name__ == '__main__':
    main()
