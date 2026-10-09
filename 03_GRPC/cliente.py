import grpc
import servicio_pb2
import servicio_pb2_grpc

def ejecutar():
    canal = grpc.insecure_channel("localhost:50051")
    stub = servicio_pb2_grpc.SaludoStub(canal)
    respuesta = stub.DecirHola(servicio_pb2.Solicitud(nombre="Ruth"))
    print("Respuesta recibida del servidor gRPC:")
    print(respuesta.mensaje)

if __name__ == "__main__":
    ejecutar()

