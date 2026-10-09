import time
from kafka import KafkaProducer

# Conexión al broker de Kafka en localhost
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: str(v).encode('utf-8')
)

topic = 'tema1'

print("Enviando mensajes al tópico de Kafka...")
for i in range(5):
    mensaje = f"Evento #{i+1} enviado a Kafka"
    producer.send(topic, value=mensaje)
    print(f"[Productor] Enviado: {mensaje}")
    time.sleep(1)

producer.flush()
producer.close()
print("Finalizó el envío de mensajes.")
