from flask import Blueprint, jsonify
from db_connector import get_connection

routes_get = Blueprint('routes_get', __name__)

@routes_get.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_connection()
        if conn is None:
            return jsonify({"error": "Database connection failed"}), 500

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")  # Table name users
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        if not data:
            return jsonify({"message": "No users found"}), 200

        return jsonify(data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
