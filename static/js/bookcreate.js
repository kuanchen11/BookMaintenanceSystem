var codeBorrowed = 'B';
var codeAvailable = 'Y';
var codeUnavailable = 'N';

$(document).ready(function() {
    $('#borrower').change(function() {
        var selectedBorrower = $(this).val();
        var statusDropdown = $('#status');
        
        if (selectedBorrower) {
            statusDropdown.val(codeBorrowed);
        }
    });
    
    $('#status').change(function() {
        var selectedStatus = $(this).val();
        var borrowerDropdown = $('#borrower');
        
        if (selectedStatus === codeAvailable || selectedStatus === codeUnavailable) {
            borrowerDropdown.val('');
            borrowerDropdown.prop('disabled', true);
        } else {
            borrowerDropdown.prop('disabled', false);
        }
    });

    $('#submit').click(function() {
        var selectedStatus = $('#status').val();
        var selectedBorrower = $('#borrower').val();
        
        if (selectedStatus === codeBorrowed && !selectedBorrower) {
            alert('請選擇借閱人');
            return false;
        }
        

    });
});
