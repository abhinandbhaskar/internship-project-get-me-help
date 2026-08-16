/**
 * Created by abhin on 19-07-2024.
 */

       function confirmLogout() {
            var confirmLogout = confirm("Are you sure you want to logout?");
            if (confirmLogout) {
                logout();
            }
        }

        function logout() {
            window.location.href = '/';
        }


document.getElementById('image').addEventListener('change',function(){
    const file = this.files[0];
    const fileType = file.type;
    if (!fileType.startsWith('image/')){
        alert('please select an image file.');
        this.value = '';
    }
});