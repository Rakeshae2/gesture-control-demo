async function startProgram() {
    await fetch("/start", {
        method: "POST"
    });
    alert("Gesture Recognition Started");
}

async function stopProgram() {
    await fetch("/stop", {
        method: "POST"
    });
    alert("Gesture Recognition Stopped");
}
