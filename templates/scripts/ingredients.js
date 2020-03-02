$(document).ready( function () {
    var table = $('#myTable').DataTable()
    $( table.table().container() )
    .addClass( 'selectable' );
});



$('.add-ingredient').click(function( event ) {
    console.log($(this).attr("value"))
    $('#add-ingredient-modal').modal('show');
 })

 $('.delete').click(function( event ) {
    console.log($(this).attr("value"));
    var id = $(this).attr("value")
    console.log("")
    $.ajax({
        url: '/ingredients?id=' + id,
        type: 'delete',
        contentType: "application/json; charset=utf-8",
    }).done(function(data) {
        location.reload();
    })
})

$('.edit').click(function( event ) {
    console.log($(this).attr("value"))
    $('#recipe_modal').modal('show');
    $('.modal-header').html('Edit Recipe');
    $('#edit-modal-id').attr("value",$(this).attr("value"));
    $('#edit-modal-name').attr("value",$(this).attr("row-name"));
})

$('#add-ingredient-modal-submit').submit(function( event) {
    event.preventDefault();
    var category = $('#inputcategory').val()
    var submit = $(this).serialize() + '&category='+category;
    console.log(submit)
    console.log()
        $.ajax({
            url: '/ingredients?' + submit,
            type: 'post',
            contentType: "application/json; charset=utf-8",
            success: function(result){
                location.reload();
            }
    }).fail(function(data) {
        location.reload();
    });
});
