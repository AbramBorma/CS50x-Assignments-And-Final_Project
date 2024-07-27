const countrySelect = document.getElementById('country')
const stateSelect = document.getElementById('state')
const citySelect = document.getElementById('city')
const districtSelect = document.getElementById('district')
const categorySelect = document.getElementById('category')
const subcategorySelect = document.getElementById('subcategory')
const priceSelect = document.getElementById('price')

countrySelect.addEventListener('change', function()
{
    const countryId = countrySelect.value;
    getStates(countryId);
});

stateSelect.addEventListener('change', function ()
{
    const stateId = stateSelect.value;
    getCities(stateId);
});

citySelect.addEventListener('change', function ()
{
    const cityId = citySelect.value;
    getDistricts(cityId);
});

categorySelect.addEventListener('change', function()
{
    const categoryId = categorySelect.value;
    getSubcategories(categoryId);
});

function getStates(countryId)
{
    fetch('/venues',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({countryId: countryId})
    })
    .then(response => response.json())
    .then(data => {
        const states = data.states;

        stateSelect.innerHTML = '';

        const defaultOption = document.createElement('option');
        defaultOption.text = "State";
        defaultOption.selected = true;
        defaultOption.disabled = true;

        stateSelect.appendChild(defaultOption);

        states.forEach(state => {
            const option = document.createElement('option');
            option.value = state.id;
            option.textContent = state.state;
            stateSelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));
}

function getCities(stateId)
{
    fetch('/venues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({stateId: stateId})
    })
    .then(response => response.json())
    .then(data => {
        const cities = data.cities;

        citySelect.innerHTML = '';
        
        const defaultOption = document.createElement('option');
        defaultOption.text = "City";
        defaultOption.selected = true;
        defaultOption.disabled = true;

        citySelect.appendChild(defaultOption);

        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city.id;
            option.textContent = city.city;
            citySelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));
}

function getDistricts(cityId)
{
    fetch('/venues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({cityId: cityId})
    })
    .then(response => response.json())
    .then(data => {
        const districts = data.districts;

        districtSelect.innerHTML = '';
        
        const defaultOption = document.createElement('option');
        defaultOption.text = "District";
        defaultOption.selected = true;
        defaultOption.disabled = true;

        districtSelect.appendChild(defaultOption);

        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district.id;
            option.textContent = district.district;
            districtSelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));
}

function getSubcategories(categoryId)
{
    fetch('/venues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({categoryId: categoryId})
    })
    .then(response => response.json())
    .then(data => {
        const subcategories = data.subcategories;

        subcategorySelect.innerHTML = '';
        
        const defaultOption = document.createElement('option');
        defaultOption.text = "Subcategory";
        defaultOption.selected = true;
        defaultOption.disabled = true;

        subcategorySelect.appendChild(defaultOption);

        subcategories.forEach(subcategory => {
            const option = document.createElement('option');
            option.value = subcategory.id;
            option.textContent = subcategory.subcategory;
            subcategorySelect.appendChild(option);
        });
    })
    .catch(error => console.error(error));
}