import asyncio
import websockets
import json

# Store connected clients with their usernames
connected_clients = {}

async def broadcast_message(message):
    """Broadcast a message to all connected clients, including the sender."""
    for client_socket in connected_clients:
        await client_socket.send(message)

async def handle_client(websocket):
    """Handle connection, receiving and broadcasting messages."""
    # Wait for the client to send their username
    try:
        username_message = await websocket.recv()
        username_data = json.loads(username_message)
        username = username_data["username"]

        # Add client and their username to the connected clients dictionary
        connected_clients[websocket] = username

        # Broadcast that the user has joined
        join_message = json.dumps({"system": True, "message": f"{username} has joined the chat."})
        await broadcast_message(join_message)

        # Handle receiving and broadcasting messages from the user
        async for message in websocket:
            await broadcast_message(message)

    finally:
        # Remove client from connected clients on disconnection
        if websocket in connected_clients:
            username = connected_clients.pop(websocket)
            # Broadcast that the user has left
            leave_message = json.dumps({"system": True, "message": f"{username} has left the chat."})
            await broadcast_message(leave_message)

# Start the server
async def start_server():
    async with websockets.serve(handle_client, "localhost", 12345):
        print("Chat server started on ws://localhost:12345")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(start_server())
