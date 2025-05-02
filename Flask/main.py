from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory log storage (for demonstration purposes)
tab_switch_logs = []

@app.route('/log_tab_switch', methods=['POST'])
def log_tab_switch():
    data = request.get_json()
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())
    user_ip = request.remote_addr
    log_entry = {
        'timestamp': timestamp,
        'user_ip': user_ip
    }
    tab_switch_logs.append(log_entry)
    print(f"Tab switch detected: {log_entry}")
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
