import asyncio
import websockets

async def enviar_mensajes():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("[Cliente] Conectado al servidor WebSocket.")
        
        mensajes = ["Hola Servidor", "Probando WebSockets", "Mensaje final"]
        for msg in mensajes:
            print(f"[Cliente] Enviando: {msg}")
            await websocket.send(msg)
            respuesta = await websocket.recv()
            print(f"[Cliente] Respuesta: {respuesta}\n")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(enviar_mensajes())
