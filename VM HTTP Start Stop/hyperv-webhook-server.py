from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import json
import urllib.parse

class HyperVHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)

        if 'action' in params and 'vm' in params:
            action = params['action'][0]
            vm_name = params['vm'][0]

            if action == 'start':
                result = subprocess.run(
                    ["powershell", "-ExecutionPolicy", "Bypass", "-File", "start-vm.ps1", "-vmName", vm_name],
                    capture_output=True, text=True
                )
                response = {"vm_name": vm_name, "action": "start", "output": result.stdout.strip()}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            elif action == 'stop':
                result = subprocess.run(
                    ["powershell", "-ExecutionPolicy", "Bypass", "-File", "stop-vm.ps1", "-vmName", vm_name],
                    capture_output=True, text=True
                )
                response = {"vm_name": vm_name, "action": "stop", "output": result.stdout.strip()}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            elif action == 'status':
                result = subprocess.run(
                    ["powershell", "-ExecutionPolicy", "Bypass", "-File", "status-vm.ps1", "-vmName", vm_name],
                    capture_output=True, text=True
                )
                status = result.stdout.strip()
                response = {"vm_name": vm_name, "action": "status", "status": status}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            else:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                error_response = {"error": "Invalid action"}
                self.wfile.write(json.dumps(error_response).encode())
        else:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_response = {"error": "Missing parameters"}
            self.wfile.write(json.dumps(error_response).encode())

def run(server_class=HTTPServer, handler_class=HyperVHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
