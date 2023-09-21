var firstName,firstNameErrorMsg,firstNameError;$(document).ready(function(){firstNameError=true;$('#firstName').blur(function(){firstName=$(this).val();if($(this).val().length>=2){$(this).addClass('done').removeClass('required');$(this).next(".error").remove()
firstNameError=false;}
else{$(this).removeClass('done').addClass('required');if($(this).next('.error').length==0){$(this).after("<span class='error'>"+firstNameErrorMsg+"</span>")}
firstNameError=true;}}).keyup(function(){$(this).removeClass('required done');});});