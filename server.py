from flask import Flask, jsonify, render_template
from routes_get import routes_get    # GET / UPDATE
from routes_post import routes_post  # POST / INSERT / DELETE

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(routes_get, url_prefix='/api')
app.register_blueprint(routes_post, url_prefix='/api')  # ← API routes ke liye

# Optional: Root route for testing
@app.route('/')
def home_root():
    return jsonify({"message": "Welcome to Flask API"})

# Optional: Test route
@app.route('/test')
def test():
    return jsonify({"message": "Flask API is running successfully!"})
@app.route('/form')
def user_form():
    return render_template("user_form.html")

if __name__ == '__main__':
    app.run(debug=True)