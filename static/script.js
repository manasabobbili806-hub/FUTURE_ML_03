function sendMessage() {
    let msg = document.getElementById("msg").value;

    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "msg=" + encodeURIComponent(msg)
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("chatbox").innerHTML +=
        "<p><b>You:</b> " + msg + "</p>";

        document.getElementById("chatbox").innerHTML +=
        "<p><b>Bot:</b> " + data + "</p>";

        document.getElementById("msg").value = "";
    });
}