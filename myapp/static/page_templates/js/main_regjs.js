/**
 * Created by abhin on 23-07-2024.
 */


          document.getElementById('image').addEventListener('change', function() {
        const file = this.files[0];
        const fileType = file.type;

        // Check if the selected file type is an image
        if (!fileType.startsWith('image/')) {
            alert('Please select an image file.');
            this.value = ''; // Clear the file input
        }
    });

