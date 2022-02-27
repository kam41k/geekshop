window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        const target = event.target;
        const basketID = target.name
        const basketQuantity = target.value
        $.ajax({
            url: '/basket/basket-edit/' + basketID + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}