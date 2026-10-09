import Pyro5.api  #

@Pyro5.api.expose  #[cite: 8, 9]
class Calculadora:  #[cite: 8, 9]
    def sumar(self, a, b):  #[cite: 8, 9]
        return a + b  #[cite: 8, 9]

daemon = Pyro5.api.Daemon()  #[cite: 8, 9]
uri = daemon.register(Calculadora)  #[cite: 8, 9]
print("URI del objeto remoto:")  #[cite: 8, 9]
print(uri)  #[cite: 8, 9]
print("\nServidor de Calculadora esperando llamadas...")  #[cite: 8, 9]
daemon.requestLoop()  #[cite: 8, 9]
