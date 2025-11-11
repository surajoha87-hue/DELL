#insert query in admin_commisions table
from flask import Blueprint, request, render_template, jsonify
from db_connector import get_connection

routes_post = Blueprint('routes_post', __name__)

@routes_post.route('/admin_commisions_insert', methods=['POST'])
def insert_admin_commission():
    try:
        data = request.get_json()
        amount = data.get('amount')

        if amount is None:
            return jsonify({"error": "amount is required"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO admin_commisions (amount) VALUES (%s)", 
            (amount,)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Admin commission added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#          http://127.0.0.1:5000//api/admin_commisions_insert flask postman
#update query in admin_commisions table
@routes_post.route('/admin_commisions_update/<int:id>', methods=['PUT'])
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
#       http://127.0.0.1:5000/api/admin_commisions_update/11 flask postman
#delete query in admin_commisions table
@routes_post.route('/admin_commisions_delete/<int:id>', methods=['DELETE'])
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
#      http://127.0.0.1:5000/api/admin_commisions_delete/11 flask postman
# User form bhar ke submit kare → db me entry ho jaye esa kr skta hu
@routes_post.route('/users_insert', methods=['POST'])
def insert_user():
    try:
      #  print("FORM DATA RECEIVED:", request.form)  # Debug line
        first_name = request.form.get('first_name')   # ✅ match HTML
        email = request.form.get('email')
        age = request.form.get('age')

        if not first_name or not email or not age:
            return jsonify({"error": "All fields are required"}), 400

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (first_name, email, age) VALUES (%s, %s, %s)",
            (first_name, email, int(age))
        )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "User added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
# http://127.0.0.15000/form flask form    
# http://127.0.0.1:5000/api/users_insert flask postman form data 