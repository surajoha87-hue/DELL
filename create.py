from flask import Flask, request, redirect, render_template, jsonify
from db_connector import get_connection

app = Flask(__name__)

# ------------------ READ ------------------
#displaying users data [GET]

@app.route("/view_table")
def view_table():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM uusers")  # fetch all users
        users = cursor.fetchall()
        conn.close()
        
        return jsonify({"status": "success", "data": users})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})



# ------------------ adding------------------
@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO uusers (name, email) VALUES (%s, %s)", (name, email))  # Corrected table name
        conn.commit()
        conn.close()

        # Return success message in JSON format
        return jsonify({"message": "Data inserted successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
        conn.close()

        # Return error message in JSON format
        return jsonify({"message": "An error occurred while inserting data.", "error": str(e)}), 500
# ------------------ UPDATE ------------------
@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            return jsonify({"status": "error", "message": "Name and Email are required"}), 400

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE uusers SET name=%s, email=%s WHERE id=%s", (name, email, id))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"status": "error", "message": f"No user found with id {id}"}), 404

        return jsonify({"status": "success", "message": f"User {id} updated."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if conn:
            conn.close()
# ------------------ DELETE ------------------
#deleting users data
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # First, check if the user exists
        cursor.execute("SELECT * FROM uusers WHERE id=%s", (id,))
        user = cursor.fetchone()  # Fetch one row

        if not user:
            # If no user found, return an error message
            return jsonify({"status": "error", "message": f"User with ID {id} does not exist or is already deleted."}), 404

        # Proceed with deletion since the user exists
        cursor.execute("DELETE FROM uusers WHERE id=%s", (id,))
        conn.commit()

        # Check if any row was affected, meaning deletion was successful
        if cursor.rowcount > 0:
            return jsonify({"status": "success", "message": f"Deleted user with ID {id}."}), 200
        else:
            return jsonify({"status": "error", "message": f"User with ID {id} was not found or already deleted."}), 404

    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return jsonify({"status": "error", "message": "An error occurred while deleting the user.", "error": str(e)}), 500

    finally:
        if conn:
            conn.close()
#--------create table route--------
#[GET]
@app.route("/create_table") 
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = DATABASE()
          AND table_name = 'uusers'
    """)

    (exists,) = cursor.fetchone()

    if exists:
        conn.close()
        return "Table already exists!"

    # Create table only if it doesn't exist
    cursor.execute("""
        CREATE TABLE uusers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    conn.commit()
    conn.close()
    return "Table created successfully!"


#---------testing route---------
@app.route("/test")
def test_route():
    return "Test route is working!"
# Run the app if this file is executed directly
#http://127.0.0.1:5000

if __name__ == "__main__":
    app.run(debug=True)


