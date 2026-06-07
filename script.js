let predictionCount = 0;

function predictRetention() {
  predictionCount++;

  const players = 1000;
  const retained = Math.floor(Math.random() * 701) + 200;
  const churned = players - retained;
  const rate = ((retained / players) * 100).toFixed(1);

  document.getElementById("retained").innerText = retained;
  document.getElementById("churned").innerText = churned;
  document.getElementById("rate").innerText = rate + "%";

  document.getElementById("result").innerText =
    "Prediction #" + predictionCount + ": Retention Rate = " + rate + "%";
}