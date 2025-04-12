from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Signal received: {data}")
    
    # Save alert to logs
    with open("logs/alerts.json", "a") as f:
        f.write(json.dumps({"timestamp": timestamp, "data": data}) + "\n")
    
    # Placeholder for broker logic
    # Example: send_order(data["symbol"], data["signal"], data["price"])
    
    return jsonify({"status": "success", "message": "Alert received"}), 200

if __name__ == '__main__':
    app.run(debug=True)
