#update query in admin_commisions table
from flask import Blueprint, request, jsonify
from db_connector import get_connection

routes_update = Blueprint('routes_update', __name__)

@routes_update.route('/admin_commisions_update/<int:id>', methods=['PUT'])
def update_admin_amount(id): 
    try:
        data = request.get_json()
        amount = data.get('amount')

        if amount is None:
            return jsonify({"error": "amount is required"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE admin_commisions SET amount = %s WHERE id = %s",
            (amount, id)
        )
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Admin commission updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

