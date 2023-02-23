$(document).ready(function(){
    // $("#btnSubmit").hide()
    // $("#btnReEvaluate").hide()
    $(".btn-success").mouseover(function(){
        $(this).css("background-color", "rgb(175, 158, 74)");
        $(this).css("color", "black")
    })
    $(".btn-success").mousedown(function(){
        $(this).css("background-color", "rgb(180, 115, 115)");
    })
    $(".btn-success").mouseup(function(){
        $(this).css("background-color", "rgb(175, 158, 74)");
        $(this).css("color", "black")
    })
    $(".btn-success").mouseleave(function(){
        $(this).css("background-color", "")
        $(this).css("color", "white")
    })
    $("button.btn-success").click(function(){
        $(".btn-success").fadeOut('slow');
        $("#btnSubmit").fadeIn(2000);
        $("#btnReEvaluate").fadeIn(2000);
        $("#txtHSelectedEvent").val(this.name)
        // console.log(">>>>>>>>>>this.name>>>>>>>>>>>>>", typeof this.name)
        $(this).parent().parent().css("background-color", "rgb(185, 234, 185)");
    })
    $("#btnReEvaluate").click(function(){
        $("#txtHSelectedEvent").val("re-evaluate")
    })
})