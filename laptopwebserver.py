from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
       <head>
    <title>Device Information</title>
       </head>
<body>
     <h1 align="center">Vijayan.M-26018999</h1>

    <h2 align="center">MY DEVICE INFORMATION</h2>
    <h2>Device Info</h2>

    <table border="1" cellpadding="10" cellspacing="0">
        <tr>
            <th>S.No</th>
            <th>Property</th>
            <th>Details</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Device Name</td>
            <td>TL15-53M-G2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel Core 5 210H (2.20 GHz)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Installed RAM</td>
            <td>16 GB (15.7 GB usable)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Graphics Card</td>
            <td>Intel Graphics (128 MB)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Storage</td>
            <td>477 GB (186 GB used)</td>
        </tr>
        <tr>
            <td>6</td>
            <td>System Type</td>
            <td>64-bit operating system, x64-based processor</td>
        </tr>
        <tr>
            <td>7</td>
            <td>Pen and Touch</td>
            <td>No pen or touch input available</td>
        </tr>
    </table>

</body> 
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()