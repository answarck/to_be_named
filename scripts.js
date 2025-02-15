const pickupLines = [
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a name, or can I call you mine?",
    "Is your name Google? Because you have everything I’m searching for.",
    "Are you a parking ticket? Because you’ve got FINE written all over you.",
    "Do you believe in love at first sight, or should I walk by again?",
    "If you were a vegetable, you’d be a cute-cumber!",
    "Are you a campfire? Because you’re hot and I want s’more.",
    "Is your dad a baker? Because you’re a cutie pie!",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a fruit, you’d be a fine-apple!"
];

document.getElementById('generate-button').addEventListener('click', function() {
    const randomIndex = Math.floor(Math.random() * pickupLines.length);
    document.getElementById('pickup-line').innerText = pickupLines[randomIndex];
});
