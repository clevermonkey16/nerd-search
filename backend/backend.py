from flask import Flask, jsonify, g
from flask_cors import CORS
from writedata import SQLWriter
import sqlite3
import os
from flask import send_file

app = Flask(__name__)
CORS(app, origins=["https://nerd-search-79d2.onrender.com/", "http://localhost:3000"])
DATABASE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "jobs.db")


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


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/folders")
def list_folders():
    # Get the list of folders in the current directory
    folders = [folder for folder in os.listdir(".") if os.path.isdir(folder)]
    # Return the list of folders as JSON data
    return jsonify(folders)


@app.route("/files")
def list_files():
    # Get the path to the current directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Get the list of files in the current directory
    files = [
        file
        for file in os.listdir(current_directory)
        if os.path.isfile(os.path.join(current_directory, file))
    ]
    # Return the list of files as JSON data
    return jsonify(files)


@app.route("/file/<filename>")
def get_file_content(filename):
    # Get the path to the current directory
    current_directory = os.path.dirname(os.path.realpath(__file__))
    # Construct the full path to the requested file
    file_path = os.path.join(current_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # Return the file contents as a response
        return send_file(file_path)
    else:
        # Return a 404 Not Found error if the file doesn't exist
        return "File not found", 404


@app.route("/jobs", methods=["GET"])
def get_jobs():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    return jsonify(jobs)


# if __name__ == "__main__":
#    app.run(debug=True, port=4000)
