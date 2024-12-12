from flask import Flask, request, jsonify
import logging
import os
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# ================== Logging Configuration ==================
# Ensure the logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up a logger for valid requests
app_logger = logging.getLogger('app_logger')
app_logger.setLevel(logging.INFO)

valid_handler = logging.FileHandler('logs/routing.log', mode='a', encoding='utf-8')
valid_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
valid_handler.setFormatter(formatter)
app_logger.addHandler(valid_handler)

# Set up a logger for errors
error_logger = logging.getLogger('error_logger')
error_logger.setLevel(logging.ERROR)

error_handler = logging.FileHandler('logs/errors.log', mode='a', encoding='utf-8')
error_handler.setFormatter(formatter)
error_logger.addHandler(error_handler)

# ================== Database Integration ==================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a database model to store requests
class RequestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_data = db.Column(db.Text, nullable=False)
    approver = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

# Initialize the database
with app.app_context():
    db.create_all()

# ================== Flask Route ==================
@app.route('/route_request', methods=['POST'])
def route_request_api():
    try:
        req_data = request.get_json()

        if not req_data:
            error_logger.error("Received an empty or invalid JSON payload")
            return jsonify({"error": "Invalid JSON or empty request"}), 400

        # Check for required fields
        if 'type' not in req_data or 'priority' not in req_data or 'department' not in req_data:
            error_logger.error(f"Missing required fields in request: {req_data}")
            return jsonify({"error": "Missing fields: type, priority, department"}), 400

        # Custom routing logic to assign an approver
        if req_data['type'] == 'Leave':
            approver = "Direct Manager"
        elif req_data['priority'] == 'High':
            approver = "Senior Manager"
        else:
            approver = "Department Head"

        # Log the request to the database
        new_log = RequestLog(request_data=str(req_data), approver=approver)
        db.session.add(new_log)
        db.session.commit()

        # Log the request details
        app_logger.info(f"Request: {req_data}, Assigned Approver: {approver}")

        return jsonify({
            "message": "Request processed",
            "data": req_data,
            "approver": approver
        })

    except Exception as e:
        error_logger.error(f"Request processing failed: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
