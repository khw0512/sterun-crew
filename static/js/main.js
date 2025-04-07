let btn = document.getElementById("menu-button");
let screen = document.getElementById("screen");
let menu = document.getElementById("mobile_menu");

function open_close() {
  if (btn.dataset.menu === "0") myOpen();
  else myClose();
}

function myOpen() {
  menu.style.left = "0px";
  btn.dataset.menu = "1";
  btn.src = "/static/img/x-symbol_btn.svg"
  setTimeout((screen.style.backgroundColor = "rgb(200,200,200)"), 300);
}

function myClose() {
  menu.style.left = "-100%";
  btn.dataset.menu = "0";
  btn.style.backgroundColor = "transparent";
  screen.style.backgroundColor = "transparent";
  btn.src = "/static/img/hamber_btn.svg"
}

window.addEventListener("click", (e) => {
  if (e.target.className !== "submenu" && e.target !== btn) myClose();
});

window.onload = function(){
  setTimeout(function(){
  document.querySelector('.loading').style.visibility = 'hidden'
  document.querySelector('.loading').style.opacity = 0
  },300);
};

