import pika

conexion = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
canal = conexion.channel()
canal.queue_declare(queue="cola")

def callback(ch, method, properties, body):
    print("Mensaje recibido:", body.decode())

canal.basic_consume(queue="cola", on_message_callback=callback, auto_ack=True)
print("Esperando mensajes en la cola...")
canal.start_consuming()
