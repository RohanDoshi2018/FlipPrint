function randId() {
    return Math.random().toString(36).substr(2, 10);
}

// assign a random ID to this browser instance
var browser_id = randId();
$("#hidden_id").val(browser_id);

$('#inkjet_img').popover();
$('#laser_img').popover();

$( "#inkjet" ).click(function() {
    $('.upload_file').show();
    $('.select_printer').hide();
    $('#hidden_printer_type').val("inkjet");
});

$( "#laser" ).click(function() {
    $('.upload_file').show();
    $('.select_printer').hide();
    $('#hidden_printer_type').val("laser");
});

// form validation
$('#file_input').change(function(){
    var file = this.files[0];
    var name = file.name;
    var size = file.size;
    var type = file.type;
    //Your validation
    if ((type == "application/pdf") && (size<100000) && (size>0)) {
        submit_form();
    } else {
        $('#upload_err_msg').append("Upload must be a PDF under 100 MB. Try another file.");
    }
});

function submit_form() {
    var formData = new FormData($('#upload_form')[0]);
    $.ajax({
        url: '/upload',  //Server script to process data
        type: 'POST',
        xhr: function() {  // Custom XMLHttpRequest
            var myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // Check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunction, false); // For handling the progress of the upload
            }
            return myXhr;
        },
        success: function(data){
            $('#odd_print').attr("onclick", "printJS(\'temp/"+browser_id+"_odd.pdf\')");
            $('#even_print').attr("onclick", "printJS(\'temp/"+browser_id+"_even.pdf\')");
            $('.output').show();
            $('.upload_file').hide();
        },
        data: formData,
        cache: false,
        contentType: false,
        processData: false
    });
}

function progressHandlingFunction(e){
    if(e.lengthComputable){
        $('progress').attr({value:e.loaded,max:e.total});
    }
}

$(window).on('beforeunload', function () {
    var id_data = {id: browser_id};
    id_data = JSON.stringify(id_data, null, '\t');

    $.ajax({
        type : "POST",
        url : "/delete",
        data: id_data,
        contentType: 'application/json;charset=UTF-8'
    });
    return false;
});

function go_home() {
    $('.select_printer').show();
    $('#file_input').val('');
    $('.upload_file').hide();
    $('#upload_err_msg').hide();
    $('.output').hide();
}