
$(document).ready(function() {
    $(".page").children().first().find(".page-item-body").css( "display", "block" );
    $(".page").children().first().find(".pib-indicator")
        .find("i").toggleClass("fa-compress").toggleClass("fa-expand");

    $(".page-item .pib-indicator").click(function() {
        var preview = $(this);
        preview.find("i").toggleClass("fa-expand").toggleClass("fa-compress");
        $(this).closest(".page-item").find(".page-item-body").toggle("slow", function() {});
    });
});

