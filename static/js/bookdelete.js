$(document).ready(function () {

    const deleteButton = document.getElementById('delete-book');

    deleteButton.addEventListener('click', () => {
        const bookName = document.getElementById('data-book-name').innerText;

        const isBorrowed = checkIfBookIsBorrowed();

        if (isBorrowed) {
            alert('此書外借中無法刪除');
        } else {
            const confirmDelete = confirm(`是否刪除【${bookName}】？`);

            if (confirmDelete) {
                deleteBook();
                alert('刪除成功');
            }
        }
    });

    function checkIfBookIsBorrowed() {
        if (document.getElementById('data-book-status').innerText === '已借出') {
            return true;
        } else {
            return false;
        }
    }

    function deleteBook() {
        const bookId = document.getElementById('data-book-id').innerText;
        fetch(`book/delete/${bookId}`, {
            method: 'DELETE',
        })
    }

});