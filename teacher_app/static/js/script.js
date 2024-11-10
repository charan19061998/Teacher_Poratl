
function toggleDropdown(button) {
    const studentId = button.getAttribute('data-id');  // Get the student ID from the data attribute
    const dropdownContent = document.getElementById('dropdown-' + studentId);
    
    // Toggle the visibility of the dropdown menu
    if (dropdownContent.style.display === 'none' || dropdownContent.style.display === '') {
        dropdownContent.style.display = 'block';
    } else {
        dropdownContent.style.display = 'none';
    }
}

// Close dropdown if clicked outside
document.addEventListener('click', function (event) {
    // Close dropdown if clicked outside the dropdown menu
    if (!event.target.closest('.dropdown')) {
        document.querySelectorAll('.dropdown-menu-content').forEach((dropdown) => {
            dropdown.style.display = 'none';
        });
    }
});
