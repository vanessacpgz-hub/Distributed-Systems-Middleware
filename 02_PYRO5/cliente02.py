import Pyro5.api

uri = input("Pega el URI del servidor: ")
calculadora = Pyro5.api.Proxy(uri)

resultado = calculadora.sumar(5, 3)
print("\n[Éxito] El servidor respondió a la suma.")
print("Resultado:", resultado)
