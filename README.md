# Player Retention Predictor

An interactive game-analytics UI demo built with HTML, CSS, and JavaScript. It illustrates how retained-player counts, churn counts, and retention percentages relate to one another.

**Current scope:** the button generates randomized demonstration values. The repository does not contain a trained prediction model, a gameplay dataset, or a Python machine-learning pipeline.

## What the demo does

- Starts with 1,000 players, 720 retained players, 280 churned players, and a 72% retention rate.
- Generates a random retained-player count from 200 through 900 on each button click.
- Calculates churned players as `1000 - retained`.
- Calculates retention as `retained / 1000 × 100`, displayed to one decimal place after a click.
- Updates the displayed metrics and increments a generation counter.

The interface calls these outputs "predictions," but they are simulations produced by `Math.random()`. They do not estimate actual player behavior, and no accuracy or performance metrics are available.

## Run locally

```bash
git clone https://github.com/gsishir1104/player-retention-predictor.git
cd player-retention-predictor
```

Open `index.html` in a modern browser. No dependencies or build step are required.

Alternatively, with Python 3 installed:

```bash
python -m http.server 8000
```

Open [localhost:8000](http://localhost:8000). Python is an optional static-file server, not part of the analytics implementation.

## Explore the demo

Select **Predict Retention** repeatedly and observe the updated counts and percentage. Retained and churned players should always total 1,000; generated retention rates range from 20.0% to 90.0%.

## Source guide

| File | Responsibility |
| --- | --- |
| [index.html](index.html) | Initial metrics, button, and result container |
| [script.js](script.js) | Random count generation, arithmetic, and DOM updates |
| [style.css](style.css) | Dashboard card and button styling |

## Skills demonstrated

JavaScript event handling, state updates, percentage calculations, and presentation of game-analytics concepts.

A data-driven retention model would require a separate dataset, feature definitions, a training/evaluation workflow, and integration with this interface; those components are not implemented here.

## Author

[Sishir Gottumukkala](https://github.com/gsishir1104) · [LinkedIn](https://linkedin.com/in/sishir-gottumukkala-9a7a43235)
