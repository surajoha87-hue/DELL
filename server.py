from flask import Flask, jsonify    
from routes_get import routes_get       # GET / UPDATE
from routes_post import routes_post     # POST / INSERT / DELETE

app = Flask(__name__)

# ✅ Register Blueprints
app.register_blueprint(routes_get, url_prefix="/api")
app.register_blueprint(routes_post, url_prefix="/api")

# Optional root route for testing
@app.route('/')
def home_root():
    return jsonify({"message": "Welcome to Flask API"})

# Optional /test route
@app.route('/test')
def test():
    return jsonify({"message": "Flask API is running successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
