document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#food-form');

    if (form) {
        form.addEventListener('submit', function(event) {
            const portionSizeInput = document.getElementById('portion_size');
            const caloriesSizeInput = document.getElementById('calories_100g');
            const nutrientSizeInput = document.getElementById('nutrient');

            let valid = true;
            let errorMessage = '';

            if (portionSizeInput && (portionSizeInput.value === '' || portionSizeInput.value <= 0)) {
                errorMessage += 'Portion size must be greater than 0.\n';
                valid = false;
            }
            if (caloriesSizeInput && (caloriesSizeInput.value === '' || caloriesSizeInput.value <= 0)) {
                errorMessage += 'Calories must be greater than 0.\n';
                valid = false;
            }
            if (nutrientSizeInput && (nutrientSizeInput.value === '' || nutrientSizeInput.value <= 0)) {
                errorMessage += 'Nutrients must be greater than 0.\n';
                valid = false;
            }

            if (!valid) {
                alert(errorMessage.trim());
                event.preventDefault();
                console.log('Invalid input detected, preventing form submission');
            } else {
                console.log('Form submitted successfully.');
            }
        });
    } else {
        console.log('Form with ID "food-form" not found.');
    }
});
