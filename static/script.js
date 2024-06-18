document.getElementById('askForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const text = document.getElementById('text').value;
    const imageFile = document.getElementById('image').files[0];

    if (!text || !imageFile) {
        alert('Please provide both text and image.');
        return;
    }

    const formData = new FormData();
    formData.append('text', text);
    formData.append('image', imageFile);

    try {
        const response = await fetch('/ask', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();
        document.getElementById('response').innerText = `Answer: ${data.answer}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('response').innerText = 'An error occurred. Please try again.';
    }
});

// Show image preview
document.getElementById('image').addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const preview = document.getElementById('preview');
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});
