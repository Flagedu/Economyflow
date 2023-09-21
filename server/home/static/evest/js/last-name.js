var lastName,lastNameErrorMsg,lastNameError;$(document).ready(function(){lastNameError=true;$('#lastName').blur(function(){lastName=$(this).val();if($(this).val().length>=2){$(this).addClass('done').removeClass('required');$(this).next(".error").remove()
lastNameError=false;}
else{$(this).removeClass('done').addClass('required');if($(this).next('.error').length==0){$(this).after("<span class='error'>"+lastNameErrorMsg+"</span>")}
lastNameError=true;}}).keyup(function(){$(this).removeClass('required done');});});