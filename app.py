import time
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import start_http_server, Counter, Histogram

# Define Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency', ['endpoint'])

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        start_time = time.time()
        
        # Simulate occasional latency spikes and errors
        if random.random() < 0.2:  # 20% chance of high latency
            time.sleep(random.uniform(1.0, 3.0))
        else:
            time.sleep(random.uniform(0.1, 0.4))

        if random.random() < 0.15:  # 15% chance of an error (HTTP 500)
            status_code = 500
        else:
            status_code = 200

        # Record metrics
        duration = time.time() - start_time
        REQUEST_LATENCY.labels(endpoint='/').observe(duration)
        REQUEST_COUNT.labels(method='GET', endpoint='/', status=str(status_code)).inc()

        # Send response
        self.send_response(status_code)
        self.end_headers()
        if status_code == 200:
            self.wfile.write(b"Hello from the enterprise sample app!")
        else:
            self.wfile.write(b"Internal Server Error!")

if __name__ == '__main__':
    # Start a separate internal server for Prometheus metrics on port 8000
    start_http_server(8000)
    # Start the main web application on port 8080
    server = HTTPServer(('0.0.0.0', 8080), MetricsHandler)
    print("Sample app running on port 8080 and metrics on port 8000...")
    server.serve_forever()
