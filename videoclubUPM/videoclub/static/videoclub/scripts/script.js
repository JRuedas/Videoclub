$(document).ready(function(){
    $(".showFunction").click(function(event){
        var target = $(event.target);
        var text = document.getElementById("toShow");
        if(target.is("#showInfo")) {
            text.innerHTML = "Information";
            $("#liInfo").attr('class','active');
            $("#liDevices").attr('class','noActive');
            $("#liPricing").attr('class','noActive');
            $("#liAbout").attr('class','noActive');
        }
        else if(target.is("#showDevices")) {
            text.innerHTML = "Devices";
            $("#liDevices").attr('class','active');
            $("#liInfo").attr('class','noActive');
            $("#liPricing").attr('class','noActive');
            $("#liAbout").attr('class','noActive');
        }
        else if(target.is("#showPricing")) {
            text.innerHTML = "Pricing";
            $("#liPricing").attr('class','active');
            $("#liInfo").attr('class','noActive');
            $("#liDevices").attr('class','noActive');
            $("#liAbout").attr('class','noActive');
        }
        else if(target.is("#showAbout")) {
            text.innerHTML = "About Us";
            $("#liAbout").attr('class','active');
            $("#liInfo").attr('class','noActive');
            $("#liPricing").attr('class','noActive');
            $("#liDevices").attr('class','noActive');
        }  
    });
});

