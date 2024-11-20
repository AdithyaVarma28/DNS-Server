# DNS-Server

The **DNS Server** is a simple Python based DNS server implementation using UDP. It simulates the core functionality of a DNS server, handling DNS queries by retrieving resource records from zone files stored locally. The server processes DNS requests for IPv4 records and returns the corresponding IP addresses.

### Features

- **Handles DNS Queries Over UDP:** Supports DNS queries on port `1234` using the UDP protocol.
- **Zone File Support:** Loads DNS zone data from JSON files located in the `zones/` directory. Each zone file contains DNS records for different domain names.
- **Basic Record Types Supported:** Currently supports IPv4 address(Type=`A`) records.
- **DNS Response Construction:** The server constructs DNS responses based on the query, returning the appropriate resource record (RR).
- **Logging:** Logs requests and responses in a log file(`logs/server.log`) for debugging purposes.
- **Basic DNS Functions:** The server supports basic DNS operations like querying, resolving, and responding with `A` record data.

### RFCs for DNS

1. **RFC 1035** - *Domain Names - Implementation and Specification*: 
    [Read RFC 1035](https://tools.ietf.org/html/rfc1035)

2. **RFC 1034** - *Domain Names - Concepts and Facilities*:
    [Read RFC 1034](https://tools.ietf.org/html/rfc1034)

### Setup Instructions

To set up and run the DNS server, follow these steps:

1. **Clone the Repository:**
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/AdithyaVarma28/DNS-Server.git
   ```

2. **Run the Server:**
   Once you have set up the zone files, you can run the server using the following command:
   ```bash
   sudo python server.py
   ```
   The server will start listening for DNS queries on `127.0.0.1:1234` (localhost) by default.

### Configuration

- **Port:** The DNS server listens for requests on UDP port `1234` by default. It is possible to change the port number(preferably to a value above 1023) to a custom port
- **IP Address:** The server binds to `127.0.0.1`(loopback to localhost) by default. You can modify the IP address to bind to other interfaces if necessary.

### Usage

1. **DNS Query:**
   To query the DNS server, you can use tools like `dig` or `nslookup` on your PC. For example:
   ```bash
   dig @127.0.0.1 -p 1234 google.com
   ```
   This will send a DNS query to the server running on `localhost:1234`, requesting the A record for `google.com`.

2. **DNS Response:**
   The server will process the query, look up the corresponding DNS records from the zone files, and respond with the requested record (if found). For example, the server might respond with a record such as `142.250.190.78` for the query `google.com`.

   ![Client to server](client and server.png)

3. **Logging:**
   The server logs all incoming requests and outgoing responses to the `logs/server.log` file. This includes the timestamp and hexadecimal representation of the data.
   Example log entry:
   ```
    2024-11-19 23:15:31,172-DNS Server started on 127.0.0.1:1234
    2024-11-19 23:15:36,201-Received request from ('127.0.0.1', 62440) with data: 7d13012000010000000000010977696b69706564696103636f6d00000100010000291000000000000000
    2024-11-19 23:15:36,201-Sending response to ('127.0.0.1', 62440) with data: 7d13850000010001000000000977696b69706564696103636f6d0000010001c00c0001000100000e100004d0509ae0
   ```

### Zone File Format
Zone files are JSON files that define domain records. Each zone file should contain a list of records for a particular domain. Here's an example zone file for the domain `google.com`:

```json
[
    {
        "$origin": "google.com.",
        "a":[{"ttl":3600,"value":"142.250.190.78"}]
    }
]
```

- `$origin`: Specifies the base domain name for the zone.
- `"a"`: Contains a list of A records, each with a `ttl` (time to live) and `value`(IP address).

### Troubleshooting

If you encounter any issues, check the logs in the `logs/server.log` file for additional information on the requests and responses. 