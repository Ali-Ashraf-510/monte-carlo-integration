# Monte Carlo Integration Web App

This is a Flask-based web application that performs Monte Carlo integration to estimate the integral of the function `f(x) = x²` over the interval `[0, 1]`. The app generates random points, calculates the estimated integral, and visualizes the points under and above the curve.

## Features
- Calculates the estimated integral of `f(x) = x²` using the Monte Carlo method.
- Compares the estimated integral with the actual value (`1/3`).
- Returns the points under and above the curve for visualization.
- Provides a simple web interface to input the number of points and view results.

## Prerequisites
- Python 3.6 or higher
- Git (to clone the repository)
- A web browser to access the app

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ali-Ashraf-510/monte-carlo-integration.git
   cd monte-carlo-integration
   ```
   python -m venv venv
   .\venv\Scripts\activate
