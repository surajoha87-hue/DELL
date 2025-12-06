"""
===========================================================
PROJECT ARCHITECTURE & FLOW — FLASK + MYSQL + CONFIG
===========================================================

This file explains the full flow of the application and how
all Python files are connected together.

Project Structure:
------------------
your_project/
│
├── app.py                <-- Main Flask application
├── db_connector.py       <-- Handles database connection
├── project_flow.py       <-- This documentation file
│
└── config/
    └── config.ini        <-- DB credentials

└── templates/
    └── index.html        <-- Frontend HTML for CRUD UI


===========================================================
1. config/config.ini  →  Store Database Configuration
===========================================================

This file contains database login details:

Example:
--------
[database]
host = localhost
user = root
password = 1234
database = mydb
port = 3306


We keep credentials OUTSIDE Python code for:
✔ security
✔ easier environment changes
✔ cleaner code


===========================================================
2. db_connector.py  →  Centralized MySQL Connection
===========================================================

Purpose:
--------
This file reads config.ini and returns a live MySQL connection to be used in Flask.

Main Responsibilities:
----------------------
✔ Read config.ini  
✔ Connect to MySQL  
✔ Return the connection object  
✔ Handle connection errors  

Used by:
--------
app.py (imported from db_connector)


Function Flow:
--------------

1. configparser loads config.ini  
2. get_connection() extracts DB credentials  
3. mysql.connector.connect() creates connection  
4. Connection is returned to caller  
5. In case of failure → returns None  

This file abstracts DB logic, so Flask app stays clean.


===========================================================
3. app.py  →  Main Flask Application with CRUD
===========================================================

Purpose:
--------
The core web application.  
Handles user actions, communicates with DB, and renders templates.

Imported From:
--------------
db_connector → to fetch DB connection

CRUD Endpoints:
---------------

1. READ  →  "/"  
   - Fetch all users from DB  
   - Render HTML table  

2. CREATE → "/add"  
   - Insert new user into DB  

3. UPDATE → "/update/<id>"  
   - Modify existing user  

4. DELETE → "/delete/<id>"  
   - Remove user from DB  


Flow Example (READ):
--------------------
User opens browser → Flask receives "/" request →
→ app.py calls get_connection() →
→ Runs SQL query SELECT * FROM users →
→ Data is passed to index.html →
→ HTML renders list of users.


===========================================================
4. templates/index.html  →  UI for CRUD Operations
===========================================================

Purpose:
--------
Provide an HTML interface for showing users and forms for:

✔ Add User  
✔ Update User  
✔ Delete User  

The HTML page receives "users" list from app.py.

Example Flow:
-------------
1. User fills form → submit  
2. Form triggers add/update route in app.py  
3. app.py updates DB using db_connector  
4. Page reloads with updated data  


===========================================================
FULL REQUEST FLOW (Example for Adding a User):
===========================================================

1. User fills “Add User” form in index.html  
2. Form sends POST request to /add  
3. app.py receives request → extracts name & email  
4. app.py calls get_connection() from db_connector.py  
5. db_connector returns MySQL connection  
6. app.py runs SQL INSERT query  
7. DB stores new user  
8. app.py redirects back to "/"  
9. "/" fetches all users → displays updated list  


===========================================================
WHY THIS ARCHITECTURE IS GOOD?
===========================================================

✔ Separation of concerns  
   - db_connector handles DB logic  
   - app.py handles web logic  
   - config.ini stores credentials  
   - templates handle UI  

✔ Security  
   No credentials or SQL logic inside main app file.

✔ Scalability  
   Easy to add new tables, modules, or APIs.

✔ Maintainability  
   Each component has a clear job.


===========================================================
FUTURE IMPROVEMENTS
===========================================================

You can add:
------------
- Connection pooling
- Models (ORM layer)
- user_service.py (to split logic from app.py)
- Logging system
- Role-based authentication (login system)
- API endpoints (REST API)

===========================================================
END OF DOCUMENTATION
===========================================================
"""
