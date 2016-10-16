$(document).ready(function(){
    $("#toast").click(function(){
        $("#toast").css("display", "none");
        $("#wtoast").animate({
            top : '-=100px'
        }, "fast");
        $("#wtoast").animate({
            top : '+=100px'
        }, "slow");
        $("#wtoast").animate({
            top : '-=100px'
        }, "fast");
        $("#ntd").css("display", "block");
    });
});