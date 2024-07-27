// Add a click event listener to each carousel item
document.querySelectorAll('.carousel-item').forEach(item => {
  item.addEventListener('click', event => {
    // Get the category from the data-cat attribute
    const category = event.currentTarget.getAttribute('data-cat').toLowerCase();

    // Redirect to the corresponding venue page
    window.location.href = `/${category}`;
  });
});
