import requests

# Probar login exitoso
print("=== Probando login exitoso ===")
r = requests.post('https://reqres.in/api/login', json={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
print(f'Status: {r.status_code}')
print(f'Response: {r.json()}')

# Probar login sin password
print("\n=== Probando login sin password ===")
r2 = requests.post('https://reqres.in/api/login', json={'email': 'eve.holt@reqres.in'})
print(f'Status: {r2.status_code}')
print(f'Response: {r2.json()}')

