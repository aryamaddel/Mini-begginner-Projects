count = 0;
function increment() {
  console.log("Button was clicked");
  count = count + 1;
  document.getElementById("count-el").innerText = count;
}
