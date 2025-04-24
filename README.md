# Monte Carlo Integration Web App 🚀

This is a **Flask-based web application** that estimates the integral of the function `f(x) = x²` over the interval `[0, 1]` using the **Monte Carlo integration** method. The app generates random points, calculates the estimated integral, and visualizes the points that fall above and below the curve.

## Features ✨
- **Monte Carlo Integration**: Estimates the integral of `f(x) = x²` using random sampling.
- **Comparison with Actual Value**: Displays the estimated integral and compares it with the actual value (`1/3`).
- **Visualization**: Displays the points under and above the curve for better visualization.
- **User Interface**: Simple web interface to input the number of points and view the results.

## Prerequisites ⚙️
To run the application, make sure you have the following installed:
- Python 3.6 or higher 🐍
- Git (for cloning the repository) 💻
- A web browser (for accessing the app) 🌐

## Installation 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ali-Ashraf-510/monte-carlo-integration.git
    cd monte-carlo-integration
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On MacOS/Linux
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 🔧

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the web interface**:
    - Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
    - Enter the number of points (between 100 and 100,000) to perform the Monte Carlo simulation.
    - View the estimated integral, actual value, error, and points for visualization.

## Project Structure 🗂️

```bash
monte-carlo-integration/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── templates/
│   └── index.html          # HTML template for the web interface
└── static/                 # Static files (e.g., CSS, JavaScript for visualization)
```
## Dependencies 📦
- The project uses the following Python package:
- Flask: Web framework for building the application.
- See requirements.txt for details:
- 

## Notes ℹ️
- The function f(x) = x² is hardcoded in the app. To integrate a different function, modify the f(x) function in app.py.

- The number of points must be between 100 and 100,000 to ensure reasonable performance.

- The app runs in debug mode by default (debug=True). Disable this in production.
## Contributing 🤝
- Contributions are welcome! To contribute:
- Fork the repository.

- Create a new branch (git checkout -b feature-branch).

- Make your changes and commit (git commit -m "Add feature").

- Push to the branch (git push origin feature-branch).

- Create a pull request.




