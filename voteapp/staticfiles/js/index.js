//var acc = document.getElementsByClassName("accordion");
//var i;
//
//for (i = 0; i < acc.length; i++) {
//  acc[i].addEventListener("click", function() {
//    this.classList.toggle("active");
//    var panel = this.nextElementSibling;
//    if (panel.style.maxHeight) {
//      panel.style.maxHeight = null;
//    } else {
//      panel.style.maxHeight = panel.scrollHeight + "px";
//    }
//  });
//}
let acc = document.querySelectorAll(".accordion");
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    var panel = this.querySelector(".accordion_in");
    if (panel.style.maxHeight) {
      this.querySelector(".red-border").querySelector("span").style = "transform:rotate(0deg); transition:transform 0.5s;"
      panel.style.maxHeight = null;
      this.querySelector(".border-list").style.backgroundColor = `inherit`
    } else {
      this.querySelector(".border-list").style.backgroundColor = `${this.getAttribute("ls-color")}`
      this.querySelector(".red-border").querySelector("span").style = "transform:rotate(180deg); transition:transform 0.5s;"
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}