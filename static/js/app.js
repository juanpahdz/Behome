let openModal = document.getElementsByClassName("modal_anuncements");
let closeBtn = document.getElementsByClassName("close_btn")
let closeFloatingMesssage = document.querySelectorAll("#close_floatmess")

Array.from(openModal).forEach(function(element) {
    element.addEventListener('click', () => {
       document.getElementById("modal_anuncements").style.display = "flex"
       document.getElementById("modal_anuncements").style.animationName = "apper"
        document.body.classList += "in-modal"
    });
});

Array.from(closeBtn).forEach(function(element) {
    element.addEventListener('click', () => {
       document.getElementById("modal_anuncements").style.display = "none"
        document.body.classList.remove("in-modal")
    });
});

Array.from(closeFloatingMesssage).forEach(function(element) {
    element.addEventListener('click', () => {
        element.parentElement.style.animation = "dissaper 0.6s forwards"
        setTimeout( () => { 
            element.parentElement.style.display = "none"
        }, 600)
    });
});


openDropdown = () => {
    const dropdown = document.getElementById("profile_drop")
    const openDropdown = document.getElementById("openDropdown")

    if (dropdown.classList.contains("active")){
        dropdown.classList.remove("active");
    }

    else {
        dropdown.classList.add("active")
    }
    
    window.addEventListener('click', function(e){   
        if (!dropdown.contains(e.target) && dropdown.classList.contains("active") && !openDropdown.contains(e.target)){
            dropdown.classList.remove("active");
            window.removeEventListener('click')
        } 
    });

    
}



