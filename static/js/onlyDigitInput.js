var priceInput = document.getElementById('price');

priceInput.addEventListener('input', function (event) {
    var value = event.target.value;

    if (!/^\d*\.?\d*$/.test(value)) {
        event.target.value = value.slice(0, -1);
    }
});
