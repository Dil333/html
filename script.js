// Define train data
const trains = [
    { id: 1, name: 'Express 1', seats: 50 },
    { id: 2, name: 'Local 1', seats: 100 },
    { id: 3, name: 'Superfast 1', seats: 75 }
];

// Function to display trains
function displayTrains() {
    const trainsDiv = document.getElementById('trains');
    trains.forEach(train => {
        const trainDiv = document.createElement('div');
        trainDiv.innerHTML = `
            <h2>${train.name}</h2>
            <p>Available seats: ${train.seats}</p>
            <button onclick="reserve(${train.id})">Reserve</button>
        `;
        trainsDiv.appendChild(trainDiv);
    });
}

// Function to reserve a seat
function reserve(trainId) {
    const train = trains.find(train => train.id === trainId);
    if (train && train.seats > 0) {
        train.seats--;
        alert('Seat reserved successfully!');
        // You can implement further logic here such as updating the UI or sending reservation details to a server
    } else {
        alert('No seats available for this train!');
    }
}

// Display trains when the page loads
window.onload = function() {
    displayTrains();
};
