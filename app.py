from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def f(x):
    """Function to integrate: f(x) = x^2."""
    return x ** 2

def get_max_y(f, a, b, steps=1000):
    """Calculate the maximum y-value of f(x) over [a, b]."""
    max_y = 0
    for i in range(steps):
        x = a + (b - a) * i / steps
        y = f(x)
        if y > max_y:
            max_y = y
    return max_y

def monte_carlo_integration(f, a, b, n_points):
    """
    Perform Monte Carlo integration for f(x) over [a, b] with n_points.
    Returns estimated integral, points under and above the curve.
    """
    max_y = get_max_y(f, a, b)
    under_curve = []
    above_curve = []
    under = 0

    for _ in range(n_points):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= f(x):
            under += 1
            under_curve.append((x, y))
        else:
            above_curve.append((x, y))

    rect_area = (b - a) * max_y
    estimated_integral = rect_area * (under / n_points)
    return estimated_integral, under_curve, above_curve

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    """Run Monte Carlo simulation based on input points."""
    try:
        n_points = int(request.json['points'])
        if n_points < 100 or n_points > 100000:
            return jsonify({'error': 'Number of points must be between 100 and 100,000'}), 400

        estimated, under, above = monte_carlo_integration(f, 0, 1, n_points)
        actual = 1/3

        return jsonify({
            'estimated': estimated,
            'actual': actual,
            'error': round(actual - estimated, 6),
            'under': under,
            'above': above
        })
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)