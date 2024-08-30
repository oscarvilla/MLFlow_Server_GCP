from flask import Flask
import subprocess
import os


# Set the environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/datascientistoscar/sa-private-key.json"

app = Flask(__name__)

@app.route('/')
def run_script():
    # Ensure the script has execute permissions
    subprocess.run(['chmod', '+x', './server.sh'])
    result = subprocess.run(['./server.sh'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    port = 8080  # Set the port directly here
    app.run(host='0.0.0.0', port=port)
