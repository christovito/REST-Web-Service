$(function () {
    $('#btnDelete').click(function () {

        $.ajax({
            data: $('form').serialize(),
            type: 'DELETE',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});