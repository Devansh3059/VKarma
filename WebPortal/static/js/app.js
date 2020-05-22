window.onload = function(){
    const navSlide = function(){
        var burgerr = document.querySelector(".burger");
        const nav = document.querySelector(".nav-links");
        const navLinks = document.querySelectorAll(".nav-links li");

        burgerr.addEventListener("click",function(){
            nav.classList.toggle("nav-active");

            //link animation
        navLinks.forEach((link)=>{
            if(link.style.animation){
                link.style.animation = ``;
            }
            else
            link.style.animation = `navLinkFade 0.5s ease forwards `
        });
        burgerr.classList.toggle("toggle");
        });
        
    };
    navSlide();
};