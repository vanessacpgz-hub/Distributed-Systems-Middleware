import pika

conexion = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
canal = conexion.channel()
canal.queue_declare(queue="cola")

canal.basic_publish(exchange="", routing_key="cola", body="Hola desde cliente")
print("Mensaje enviado a la cola")
conexion.close()

