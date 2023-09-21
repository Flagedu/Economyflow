var red_url = "";
var has_accepted = false;

function handlePopup(){
    swal({
        title: "",
        text: "هذا العرض لا يشمل منطقتك الجغرافيه (اضغط الاستفاده من العرض) وانتقل الى منصة تدعم دولتك",
        icon: "warning",
        dangerMode: true,
        buttons: ["إلغاء", "الإستفادة من العرض"]               //["Cancel", "Redirect Me"],
    })
    .then((willDelete) => {
        if (willDelete) {
            location.href = red_url;
        } else {
            console.log("CANCEL")
        }
    });
}


// $.get("https://ipinfo.io", function(response) {
function red(){
    const countryCode = country_code_server;
    
    for(var i=0; i<accepted_list.length; i++){
        const countries = accepted_list[i].countries;
        if(countries.includes(countryCode)){
            has_accepted = true;
            return true;
        }
    }
    
    if(has_accepted == false){
        for(var i=0; i<redirect_list.length; i++){
            const redirect_url = redirect_list[i].redirect_url;
            const countries = redirect_list[i].countries;
            red_url = redirect_url;
            if(countries.includes(countryCode)){
                location.href = red_url;
                return true;
            }
        }


        for(var i=0; i<others_list.length; i++){
            const redirect_url = others_list[i].redirect_url;
            red_url = redirect_url;
            location.href = red_url;
            return true;
        }
    }
}
// }, "jsonp")

red();