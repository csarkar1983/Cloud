from flask import Flask,request, jsonify
import socket
import subprocess
app = Flask(__name__)
seed_val = 0

#command = 'python3 /home/ubuntu/MP2/stress_cpu.py'

@app.route('/', methods=['GET'])
def getseed():
    return socket.gethostname()

@app.route('/', methods=['POST'])
def postseed():
    command = 'python3 /home/ubuntu/MP2/stress_cpu.py'
    p = subprocess.Popen(
        [command],
        shell=True,
        stdin=None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True)
    out, err = p.communicate()
    return "sub process initiated "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
