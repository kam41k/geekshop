window.onload = function () {
    $('.product-list').on('click', 'input[type="button"]', function () {
        const target = event.target;
        const productID = target.name
        $.ajax({
            url: '/basket/basket-add/' + productID + '/',
        })
    })
}