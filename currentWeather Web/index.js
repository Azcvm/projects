//Weather app



const weatherForm = document.querySelector(".weatherForm");
const cityInput = document.querySelector(".cityInput");
const card = document.querySelector(".card");
const APIkey = "1aa249fa5db39a050bd91b16177ae5a1";

weatherForm.addEventListener("submit", async event => {
    event.preventDefault();
    const city = cityInput.value;
    if (city) {
        try {
            const weatherData = await getWeatherData(city);
            displayWeatherInfo(weatherData);
            console.log(weatherData);
        }
        catch (error) {
            console.error(error);
            displayError(error);
        }
    }
    else {
        displayError("please enter city");
    }
});

async function getWeatherData(city) {
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${APIkey}`;
    const response = await fetch(apiUrl);

    if (!response.ok) {
        throw new Error("cant fetch data");
    }
    return await response.json();

}

function displayWeatherInfo(data) {
    const { name: city, 
            main: { temp, humidity }, 
            weather: [{ description, id }] } = data;

    card.textContent="";
    card.style.display="flex";

    const cityDisplay= document.createElement("h1");
    const tempDisplay= document.createElement("p");
    const humidityDisplay= document.createElement("p");
    const discDisplay= document.createElement("p");
    const weatherEmoji=document.createElement("p");

    cityDisplay.textContent=city;
    cityDisplay.classList.add("cityDisplay");
    card.appendChild(cityDisplay);
    
    tempDisplay.textContent=`${(temp-273.15).toFixed(2)}°C`;
    tempDisplay.classList.add("temp");
    card.appendChild(tempDisplay);
    
    humidityDisplay.textContent=`humidity: ${humidity}%`;
    humidityDisplay.classList.add("humidity");
    card.appendChild(humidityDisplay);
    
    discDisplay.textContent=description;
    discDisplay.classList.add("discDisplay");
    card.appendChild(discDisplay);

    weatherEmoji.textContent=getWeatherEmoji(id);
    weatherEmoji.classList.add("weatherEmoji");
    card.appendChild(weatherEmoji);
    

}
function getWeatherEmoji(weatherId) {
    switch(true){
        case(weatherId>=200 && weatherId<300):
            return "⛈️";
        case(weatherId>=300 && weatherId<400):
            return "🌧️";   
        case(weatherId>=400 && weatherId<600):
            return "🌧️";   
        case(weatherId>=600 && weatherId<700):
            return "❄️";
        case(weatherId>=700 && weatherId<800):
            return "🌫️";
        case(weatherId>=800 ):
            return "☀️";
        default:
            return"🤦‍♂️ unknown";
            
    } 
}

function displayError(message) {
    const errorDisplay = document.createElement("p");
    errorDisplay.textContent = message;
    errorDisplay.classList.add("errorDisplay");

    card.textContent = "";
    card.style.display = "flex";
    card.appendChild(errorDisplay);
}

