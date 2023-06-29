window.addEventListener("load", (event) => {
	console.log("Initializing chat engine.");
	const socket = new WebSocket("ws://127.0.0.1:8000/api/chat");
	const test_socket = new WebSocket("ws://127.0.0.1:8000/api/ws/test");

	socket.addEventListener("open", (event) => {
		console.log("Connected to chat engine");
		const sendChat = document.getElementById("send-chat");

		sendChat.addEventListener("click", (event) => {
			const userMessage = document.getElementById("chat").value;
			console.log(`Sending user message to chat core: ${userMessage}`);
			socket.send(userMessage);
		});

		let chatBox;

		socket.addEventListener("message", (event) => {
			message = event.data;

			if (message === "/~~")
				chatBox = addChatBox();

			console.log(message);
			chatBox.innerHTML += (message === "/~~" || message === "~~/") ? "" : message;
		});
	});

	test_socket.addEventListener("open", (event) => {
		console.log("Sending test message to API");
		test_socket.send("The grass is greener on the other side.");
	});

	test_socket.addEventListener("message", (event) => {
		console.log(`Received test confirmation: ${event.data}`);
	});
});

function addChatBox() {
	chatBox = document.createElement("div");
	document.getElementById("chat-history").appendChild(chatBox);
	return chatBox;
}


