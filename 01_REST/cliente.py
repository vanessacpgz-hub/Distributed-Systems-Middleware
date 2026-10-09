import requests  #[cite: 6]

respuesta = requests.get("http://localhost:5000/saludo")  #[cite: 6]
print(respuesta.json())  #[cite: 6]
