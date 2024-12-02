function setInitialRating(url, book_id) {
    $.ajax({
        url: url,
        method: "GET",
        data: {
            book: book_id
        },
        headers: {
            'X-CSRFToken': CSRF_TOKEN,
        },
        success: function (data) {
            console.log(data);
            $('#rating').val(data["rating"]);
        }
    });
}

