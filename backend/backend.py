from flask import Flask, jsonify, g
from flask_cors import CORS
from writedata import SQLWriter
import sqlite3

app = Flask(__name__)
CORS(app)
DATABASE = "/jobs.db"


# Connect to the database
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Close the database connection at the end of each request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/", methods=["GET"])
def get_jobs():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    return jsonify(jobs)


# if __name__ == "__main__":
#    app.run(debug=True, port=4000)
