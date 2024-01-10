function updateCities() {
    var countrySelect = document.getElementById('country');
    var citySelect = document.getElementById('city');
    var selectedCountry = countrySelect.value;

    // Clear existing cities
    citySelect.innerHTML = '<option value="" disabled selected>Select City</option>';

    // Define cities based on selected country (you can replace this with actual data)
    var citiesByCountry = {
        'usa': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami', 'Seattle'],
        'canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Edmonton', 'Ottawa'],
        'turkey': ['Istanbul', 'Ankara', 'Izmir', 'Antalya', 'Bursa', 'Adana']
        // Add more countries and cities as needed
    };

    // Populate cities based on selected country
    if (selectedCountry in citiesByCountry) {
        citiesByCountry[selectedCountry].forEach(function(city) {
            var option = document.createElement('option');
            option.value = city;
            option.text = city;
            citySelect.appendChild(option);
        });
    }
}
