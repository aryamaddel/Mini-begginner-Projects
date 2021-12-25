let countEl = document.getElementById("count-el");
let readingEl = document.getElementById("reading-el");
let count = 0;
let readings = "readings:";
let increment_status_checker = true;
function increment() {
  console.log("Button was clicked");
  count = count + 1;
  countEl.innerText = count;
  increment_status_checker = true;
}
function reset() {
  count = 0;
  countEl.innerText = count;
  increment_status_checker = true;
}
function mark() {
  if (increment_status_checker == true) {
    // console.log(count);
    if (readings == "readings:") {
      readings = readings + count;
    } else {
      readings = readings + ", " + count;
    }

    readingEl.innerText = readings;
    increment_status_checker = false;
  }
}
