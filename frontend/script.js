async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    document.getElementById("chatbox").innerHTML += `<p><strong>Você:</strong> ${userInput}</p>`;

    let response = await fetch("https://pattech-backend.up.railway.app/chat", {  // Substitua pelo link do Railway
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pergunta: userInput })
    });

    let data = await response.json();
    document.getElementById("chatbox").innerHTML += `<p><strong>PatTech:</strong> ${data.resposta}</p>`;
    document.getElementById("userInput").value = "";
}
