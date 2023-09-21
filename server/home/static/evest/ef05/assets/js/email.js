var mail,mailErrorMsg,mailError;$(document).ready(function(){var emailReg=/^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;mailError=true;$('#email').keyup(function(){mail=$(this).val();if(emailReg.test(mail)){$(this).addClass('done').removeClass('required');$(this).next(".error").remove()
mailError=false;}
else{$(this).removeClass('required done');$(this).next(".error").remove()
mailError=true;}}).blur(function(){if(emailReg.test(mail)&&mail.length!==0){$(this).addClass('done').removeClass('required');$(this).next(".error").remove()
mailError=false;}else{$(this).addClass('required').removeClass('done');if($(this).next('.error').length==0){$(this).after("<span class='error'>"+errorIcon+mailErrorMsg+"</span>")}
mailError=true;}});});