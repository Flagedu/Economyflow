function scrollMe(){var pageWidth=window.innerWidth;if(pageWidth>=375){window.scroll(0,660);}
if(pageWidth<=360){window.scroll(0,680);}
if(pageWidth>=1000){window.scroll(0,0);}}
window.onscroll=function(){if(window.pageYOffset>=61&&window.innerWidth>=1000){$(".signBar").css("display","block");}else{$(".signBar").css("display","none");}}