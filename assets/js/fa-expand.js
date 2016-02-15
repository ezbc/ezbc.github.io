
$(document).ready(function() {

    $(".page-item .pib-indicator").click(function() {
        var preview = $(this);
        preview.find("i").toggleClass("fa-expand").toggleClass("fa-compress");
        $(this).closest(".page-item").find(".page-item-body").toggle("slow", function() {});
    });
});


