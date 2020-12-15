    function update() {
        $.ajax({
            url: '/update',
            data: $('form').serialize(),
            type: 'PUT',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    };
