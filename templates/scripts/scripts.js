$(document).ready( function () {
    var table = $('#myTable').DataTable()
    $( table.table().container() )
    .addClass( 'selectable' );
});

$('#submit_recipe').submit(function( event) {
    event.preventDefault();
    var submit = $(this).serialize();
    console.log(submit)
        $.ajax({
            url: '/api/add?' + $(this).serialize(),
            type: 'post',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        location.reload();
    });
});

$('.delete').click(function( event ) {
    console.log($(this).attr("value"));
    var id = $(this).attr("value")
    $.ajax({
        url: '/api/del?id=' + id,
        type: 'delete',
        contentType: "application/json; charset=utf-8",
    }).done(function(data) {
        location.reload();
    })
})

$('.edit').click(function( event ) {
    console.log($(this).attr("value"))
    $('#edit_modal').modal('show');
    $('#edit-modal-id').attr("value",$(this).attr("value"));
    $('#edit-modal-name').attr("value",$(this).attr("row-name"));
})

$('.add').click(function( event ) {
    console.log($(this).attr("value"))
    $('#add-modal').modal('show');
 })

$('#edit-modal-submit').submit(function( event) {
    event.preventDefault();
    var submit = $(this).serialize();
    console.log(submit)
        $.ajax({
            url: '/api/edit?' + $(this).serialize(),
            type: 'put',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        location.reload();
    });
});

$('#add-modal-submit').submit(function( event) {
    event.preventDefault();
    var submit = $(this).serialize();
    console.log(submit)
        $.ajax({
            url: '/api/add?' + $(this).serialize(),
            type: 'post',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        location.reload();
    });
});