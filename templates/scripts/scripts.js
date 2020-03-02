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
            url: '/recipes?' + $(this).serialize(),
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
        url: '/recipes?id=' + id,
        type: 'delete',
        contentType: "application/json; charset=utf-8",
    }).done(function(data) {
        location.reload();
    })
})

$('.edit').click(function( event ) {
    console.log($(this).attr("value"))
    $('#recipe-modal').modal('show');
    $('.modal-title').html('Edit Recipe');
    $('.form-group').append('<input type="hidden" class="form-control" name="id" id="recipe-id"></input>');
    $('.recipe-form').prop("class", "recipe-form-edit");
    $('#recipe-id').attr("value",$(this).attr("value"));
    $('#recipe-name').attr("value",$(this).attr("row-name"));
})

$('.add').click(function( event ) {
    console.log($(this).attr("value"))
    $('#recipe-modal').modal('show');
    $('.modal-header').html('Add Recipe');
    $('.recipe-form').prop("class", "recipe-form-add");
 })



$('#modal-submit-edit').submit(function( event) {
    event.preventDefault();
    var submit = $(this).serialize();
    console.log(submit)
        $.ajax({
            url: 'recipes?' + $(this).serialize(),
            type: 'put',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        // location.reload();
    });
});

$('.form').submit(function( event) {
    event.preventDefault();
    var submit = $(this).serialize();
    console.log(submit)
        $.ajax({
            url: '/recipes?' + $(this).serialize(),
            type: 'post',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        location.reload();
    });
});

