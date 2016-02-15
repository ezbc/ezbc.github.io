
$(document).ready(function() {
    $(".page").children().find(".page-item-body-example").css( "display", "block" );
    $(".page").children().find(".pib-indicator-example")
        .find("i").toggleClass("fa-compress").toggleClass("fa-expand");

    $(".page-item .pib-indicator-listing").click(function() {
        var preview = $(this);
        preview.find("i").toggleClass("fa-expand").toggleClass("fa-compress");
        $(this).closest(".page-item").find(".page-item-body-listing").toggle("slow", function() {});
    });

    $(".page-item .pib-indicator-example").click(function() {
        var preview = $(this);
        preview.find("i").toggleClass("fa-expand").toggleClass("fa-compress");
        $(this).closest(".page-item").find(".page-item-body-example").toggle("slow", function() {});
    });
});

