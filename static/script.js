let img=document.querySelector(".navbtn")
let nav=document.querySelector(".mobnav")

console.log(img)
img.addEventListener("click",()=>{
    nav.classList.toggle("show");
    console.log("Test-2");
});

console.log("Test");
console.log("Test-3");