window.addEventListener("load", (event) => {
	console.log("Attempting to connect to chat socket");
});

const socket = new WebSocket("ws://127.0.0.1:8000/api/chat");

socket.addEventListener("open", (event) => {
	console.log("Connected to chat backend");
});
