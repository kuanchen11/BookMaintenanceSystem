var codeBorrowed = 'B';
var codeAvailable = 'Y';
var codeUnavailable = 'N';
$(document).ready(function() {
    // Bind change event to borrower dropdown
    $('#borrower').change(function() {
        var selectedBorrower = $(this).val();
        var statusDropdown = $('#status');
        
        // If borrower is selected, set status to "Borrowed" and disable borrower field
        if (selectedBorrower) {
            statusDropdown.val(codeBorrowed);
            $('#borrower').prop('readonly', true);
        } else {
            // If borrower is not selected, enable borrower field
            $('#borrower').prop('readonly', false);
        }
    });
    
    // Bind change event to status dropdown
    $('#status').change(function() {
        var selectedStatus = $(this).val();
        var borrowerDropdown = $('#borrower');
        
        // If status is "Available" or "Unavailable", clear and disable borrower field
        if (selectedStatus === codeAvailable || selectedStatus === codeUnavailable) {
            borrowerDropdown.val('');
            borrowerDropdown.prop('readonly', true);
        } else {
            // If status is not "Available" or "Unavailable", enable borrower field
            borrowerDropdown.prop('readonly', false);
        }
    });

    // Bind click event to submit button
    $('#submit').click(function() {
        var selectedStatus = $('#status').val();
        var selectedBorrower = $('#borrower').val();
        
        // If status is "Borrowed" and borrower is not selected, show alert and prevent form submission
        if (selectedStatus === codeBorrowed && !selectedBorrower) {
            alert('請選擇借閱人。');
            return false;

        }
        

    });
});