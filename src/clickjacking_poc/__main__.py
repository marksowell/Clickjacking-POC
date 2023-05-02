#!/usr/bin/env python3

import sys
import platform
import urllib.parse
import subprocess
import time
import socket

VERSION = "v1.0.1"

def create_html_file(url):
    parsed_url = urllib.parse.urlparse(url)
    host = parsed_url.hostname
    filename = host + ".html"
    with open(filename, "w") as f:
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title>Clickjacking POC</title>\n")
        f.write("</head>\n")
        f.write("<span STYLE='font-family:\"Arial\"'><b>Clickjacking POC</b><br></span>\n")
        f.write("<iframe src='" + url + "' height='100%' width='100%'></iframe>\n")
        f.write("</body>\n")
        f.write("</html>\n")
    return filename

def main():
    port = 80
    print(f"Clickjacking POC - Version {VERSION}")
    if len(sys.argv) < 2:
        print("Error: Incorrect number of arguments")
        print("Usage: python clickjacking-poc.py <URL> [-p <port>]")
        sys.exit(1)
    elif len(sys.argv) == 3 and sys.argv[2] == "-p":
        print("Error: Port number not specified")
        print("Usage: python clickjacking-poc.py <URL> [-p <port>]")
        sys.exit(1)
    elif len(sys.argv) == 4 and sys.argv[2] == "-p":
        port = sys.argv[3]
    url = sys.argv[1]
    filename = create_html_file(url)
    print("HTML file created successfully!")
    try:
        server = subprocess.Popen([sys.executable, "-m", "http.server", str(port)])
        time.sleep(1)
        if platform.system() == "Windows":
            subprocess.run(["start", "chrome", "--guest", "http://127.0.0.1:" + str(port) + "/" + filename], shell=True)
        else:
            subprocess.run(["open", "-n", "-a", "Google Chrome", "--args", "--guest", "http://127.0.0.1:" + str(port) + "/" + filename])
        time.sleep(5)
        server.terminate()
        print("Web server stopped.")
    except OSError as e:
        if e.errno == socket.errno.EADDRINUSE:
            print("Error: Port", port, "is already in use. Please choose a different port and try again.")
        else:
            raise

if __name__ == '__main__':
    main()