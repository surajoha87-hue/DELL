# delete query in admin_commisions table
from flask import Blueprint, jsonify
from db_connector import get_connection

routes_delete = Blueprint('routes_delete', __name__)

@routes_delete.route('/admin_commisions_delete/<int:id>', methods=['DELETE'])
def delete_admin_commission(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM admin_commisions WHERE id = %s",
            (id,)
        )
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Admin commission deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
