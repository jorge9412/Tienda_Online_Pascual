function createBubble() {
    const section = 
        document.getElementById("otraCosa");
    const createElement = 
        document.createElement("span");
    var size = Math.random() * 60;

    createElement.style.animation = 
    "animation 6s linear infinite";
    createElement.style.width = 180 + size + "px";
    createElement.style.height = 180 + size + "px";
    createElement.style.left = 
    Math.random() * innerWidth + "px";
    section.appendChild(createElement);

    setTimeout(() => {
        createElement.remove();
    }, 4000);
}
setInterval(createBubble, 100);
