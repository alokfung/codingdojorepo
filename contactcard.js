// When you click on the submit button, it should create a new "contact card".
// When you click a contact card, it should flip over and show the description.
// Clicking contact card again, it should flip back to front to show first and last name.
// When I click on a new div, it should hide first name and last name, and show description.
$(document).ready(function(){

    $("input:last").click(function(){
        $("#output").append("<div class='ccard_norm'><h2>"+$("#first_name").val()+" "+$("#last_name").val()+"</h2><h3>Click to view description</h3><p class='ccard_p' style='display:none;'>"+$("#description").val()+"</p></div>")

        return false;
    });

    $("#output").on("click","div.ccard_hover",function(){
        $(this).children("h2").toggle();
        $(this).children("h3").toggle();
        $(this).children("p").toggle();            
        event.stopPropagation;
    });

    $("#output").on("mouseenter","div.ccard_norm",function(){
        $(this).addClass("ccard_hover");
        $(this).removeClass("ccard_norm");
        event.stopPropagation;
    });
    $("#output").on("mouseleave","div.ccard_hover",function(){
        $(this).addClass("ccard_norm");
        $(this).removeClass("ccard_hover");
        event.stopPropagation;
    });

});                                  