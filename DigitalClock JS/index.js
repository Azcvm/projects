//Digital clock


function updateClock() {
    const timeNow = new Date();
    let hours = timeNow.getHours();
    const meridien = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12;
    hours = hours.toString().padStart(2, 0);       // pad two digit with 0
    const minutes = timeNow.getMinutes().toString().padStart(2, 0);
    const seconds = timeNow.getSeconds().toString().padStart(2, 0);
    const timeString = `${hours}:${minutes}:${seconds}:${meridien}`;
    document.getElementById("clock").textContent = timeString;
}

setInterval(updateClock, 33.33);