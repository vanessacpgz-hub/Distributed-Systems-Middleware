import asyncio
import websockets

async def eco(websocket):
    print("[Servidor] Cliente conectado.")
    try:
        async for mensaje in websocket:
            print(f"[Servidor] Recibido: {mensaje}")
            respuesta = f"Eco desde el servidor: '{mensaje}'"
            await websocket.send(respuesta)
    except websockets.exceptions.ConnectionClosedOK:
        print("[Servidor] Cliente desconectado.")

async def main():
    async with websockets.serve(eco, "localhost", 8765):
        print("Servidor WebSocket corriendo en ws://localhost:8765...")
        await asyncio.Future()  # Mantiene el servidor activo

if __name__ == "__main__":
    asyncio.run(main())
