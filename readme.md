# Python WebSocket Live Chat App  

This repository contains the source code for a live chat application built using Python and WebSockets. This app was developed during a live coding session on Twitch and later uploaded to YouTube.  
You can watch the replay of the session on [YouTube](https://www.youtube.com/watch?v=p7W-nXRcwe4).  

## Features  

- Real-time messaging using WebSockets.
- Lightweight and simple architecture.
- Easy to set up and run locally.
- Beginner-friendly Python implementation.

## Requirements  

- Python 3.8 or later.
- The `websockets` library.
- Any modern web browser (for testing).

## Install Dependencies  

Make sure Python is installed and available in your terminal. Then, install the required library:

```bash
pip install websockets
```

## Run the Server  
To start the WebSocket server, run the following command in your terminal:  
```bash
python live_chat.py
```
## Open the Client  
Open the provided `index.html` file in your browser to test the live chat functionality.

## Overview  
**live_chat.py**: The WebSocket server that handles real-time message broadcasting.  
**index.html**: A simple HTML/JavaScript client for testing the chat app.  

##  How It Works  
The `live_chat.py` script creates a WebSocket server using Python.
The server broadcasts messages to all connected clients in real-time.
Clients connect to the server and send/receive messages via WebSockets.  


##  Contributing  
Feel free to fork the repository and submit pull requests with improvements, new features, or bug fixes.