let countEl = document.getElementById("count-el");
let count = 0;
function increment() {
  console.log("Button was clicked");
  count = count + 1;
  countEl.innerText = count;
}
