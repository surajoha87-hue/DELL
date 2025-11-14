# server.py
from flask import Flask
from routes.routes_post import routes_post
from routes.routes_get import routes_get
from routes.routes_update import routes_update
from routes.routes_delete import routes_delete

app = Flask(__name__)

# Register all blueprints
app.register_blueprint(routes_post, url_prefix="/api")
app.register_blueprint(routes_get, url_prefix="/api")
app.register_blueprint(routes_update, url_prefix="/api")
app.register_blueprint(routes_delete, url_prefix="/api")

@app.route("/")
def home():
    return "API is running..."

if __name__ == "__main__":
    app.run(debug=True)