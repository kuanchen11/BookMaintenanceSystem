$(document).ready(function() {
    $('.delete-book').on('click', function() {
        var bookId = $(this).data('book-id');
        var bookName = $(this).data('book-name');
        var bookStatus = $(this).data('book-status');

        if (checkIfBookIsBorrowed(bookStatus)) {
            alert('此書外借中無法刪除');
        } else {
            const confirmDelete = confirm(`是否刪除【${bookName}】？`);

            if (confirmDelete) {
                deleteBook(bookId);
            }
        }
    });

    function checkIfBookIsBorrowed(status) {
        return status === '已借出';
    }

    function deleteBook(bookId) {
        $.ajax({
            url: `/book/delete/${bookId}`,
            type: 'DELETE',
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.message === 'unable') {
                    alert("此書外借中無法刪除");
                } else if (response.message === 'success') {
                    alert("刪除成功");
                    window.location.href = '/book/';
                }
            }
        });
    }
});
