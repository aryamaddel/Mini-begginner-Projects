let countEl = document.getElementById("count-el");
let count = 0;
let readings = "readings: ";
function increment() {
  console.log("Button was clicked");
  count = count + 1;
  countEl.innerText = count;
}
function reset() {
  count = 0;
  countEl.innerText = count;
}
function mark() {
  console.log(count);
}
