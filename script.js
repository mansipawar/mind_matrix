document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("question-form");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const responses = [];

        for (const [name, value] of formData) {
            responses.push({ question: name, answer: value });
        }

        // Send 'responses' to your server for saving to the database
        // You would typically make an AJAX request to your server here
        // Example:
        // fetch('/save-responses', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(responses)
        // })
        // .then(response => {
        //     if (response.ok) {
        //         // Handle success
        //     } else {
        //         // Handle error
        //     }
        // })
        // .catch(error => {
        //     // Handle error
        // });

        // For this example, we'll just log the responses
        console.log(responses);
    });
});

const questionCards = document.querySelectorAll('.question-card');
const submitButton = document.getElementById('submit-button');

let currentQuestion = 0;

function showQuestion(index) {
    questionCards.forEach((card, i) => {
        if (i === index) {
            card.classList.add('active');
        } else {
            card.classList.remove('active');
        }
    });
}

submitButton.addEventListener('click', () => {
    if (currentQuestion < questionCards.length - 1) {
        currentQuestion++;
        showQuestion(currentQuestion);
    }
});

// Show the first question initially
showQuestion(currentQuestion);
