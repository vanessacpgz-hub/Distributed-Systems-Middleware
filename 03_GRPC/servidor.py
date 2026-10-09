import grpc
from concurrent import futures
import servicio_pb2
import servicio_pb2_grpc

class Servidor(servicio_pb2_grpc.SaludoServicer):
    def DecirHola(self, request, context):
        return servicio_pb2.Respuesta(mensaje="Hola " + request.nombre)

def iniciar():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicio_pb2_grpc.add_SaludoServicer_to_server(Servidor(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC escuchando en el puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    iniciar()

