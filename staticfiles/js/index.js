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
/* AJAX FILTER */
let select = document.querySelector(".select_category");
select.addEventListener("change",function(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
         let plselect = document.querySelector('.select_places');
         if(select.value != "-----"){
            let data = JSON.parse(this.response);
            let result = JSON.parse(data.ref);
            plselect.innerHTML = "<option>-----</option>"
            result.forEach(function(e){
                   plselect.innerHTML += `<option value="${e.fields.name}">${e.fields.name}</option>`;
            })
         }
         else{
            plselect.innerHTML = "<option>-----</option>"
         }
    }
    else{

    }
    }
    xhttp.open("GET", `?category=${select.value}`, true);
    xhttp.send();
})

select_places = document.querySelector(".select_places");
tbody = document.querySelector(".tbody");
select_places.addEventListener("change",function(){
    document.querySelector(".loader").classList = "loader loader_block"
    tbody.innerHTML = ""
    var http = new XMLHttpRequest();
    http.onreadystatechange = function(){
    if (http.readyState === 4 && http.status === 200) {
        if(select_places.value != "-----"){
            tbody.innerHTML = this.responseText;
            document.querySelector(".loader").classList = "loader"
        }
    }
    }
    http.open("GET", `${window.location.origin}/getfilterusers?places=${select_places.value}`, true);
    http.send();
})