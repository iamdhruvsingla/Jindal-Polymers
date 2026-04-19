import os
import http.server
import socketserver

PORT = 8000

class ExtensionlessHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Ignore query params and hashes for file matching
        clean_path = self.path.split('?')[0].split('#')[0]
        
        # Build local filesystem path
        filepath = os.path.join(os.getcwd(), clean_path.lstrip('/'))
        
        # If the direct path doesn't exist AND the path + .html exists, rewrite request!
        if clean_path != '/' and not os.path.exists(filepath):
            if os.path.exists(filepath + '.html'):
                self.path = clean_path + '.html'
            
        return super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ExtensionlessHandler) as httpd:
        print("======== Jindal Polymers Local Workflow ========")
        print(f"Running Local Server at:  http://localhost:{PORT}")
        print("This server seamlessly handles clean URLs!")
        print("Press Ctrl+C to close.")
        print("================================================")
        httpd.serve_forever()
