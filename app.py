from flask import Flask, render_template, request

app = Flask(__name__)

movie = {
    "title": "Tourist Family",
    "shows": [
        {"label": "Morning Show - 10:00 AM", "time": "10:00 AM", "price": 100},
        {"label": "Noon Show - 1:00 PM", "time": "1:00 PM", "price": 150},
        {"label": "Night Show - 6:00 PM", "time": "6:00 PM", "price": 200}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', movie=movie)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    show_time = request.form['show_time']
    seats = int(request.form['seats'])

    selected_show = next((show for show in movie["shows"] if show["time"] == show_time), None)
    if selected_show:
        total_price = selected_show["price"] * seats
        return render_template('success.html', name=name, movie=movie["title"],
                               show_time=show_time, seats=seats, total_price=total_price)
    else:
        return "Invalid Show Time", 400

if __name__ == '__main__':
    app.run(debug=True)
