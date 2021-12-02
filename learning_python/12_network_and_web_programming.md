# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 3
**Week**: 11

---
# Network & Web Programming in Python

![img](/assets/img/500.jpg)

---

### Using HTTP 
Sometimes we need to access services over the web. One common example is to request data from a REST-base API. To do this we use HTTP as a client.

__Hypertext Transfer Protocol (HTTP)__ is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes. HTTP follows a classical client-server model, with a client opening a connection to make a request, then waiting until it receives a response. HTTP is a stateless protocol, meaning that the server does not keep any data (state) between two requests.

HTTP defines a set of request methods to:
* __GET__ : The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
* __HEAD__ : The HEAD method asks for a response identical to a GET request, but without the response body.
* __POST__ : The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
* __PUT__ : The PUT method replaces all current representations of the target resource with the request payload.
* __DELETE__ : The DELETE method deletes the specified resource.
* __CONNECT__ : The CONNECT method establishes a tunnel to the server identified by the target resource.
* __OPTIONS__ : The OPTIONS method describes the communication options for the target resource.
* __TRACE__ : The TRACE method performs a message loop-back test along the path to the target resource.
* __PATCH__ : The PATCH method applies partial modifications to a resource.

Python provides `urllib` and the `request` libraries for interacting with the web and HTTP. 

Lets look at a basic example:


```python
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
 'name1' : 'value1',
 'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make request
u = request.urlopen(url+'?' + querystring)

# Read the response
resp = u.read()

```

If you need to send the query parameters in the request body using a POST method, encode them and supply them as an optional argument to `urlopen()` like this:

```python
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
 'name1' : 'value1',
 'name2' : 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)

# Make a POST request
u = request.urlopen(url, querystring.encode('ascii'))

# Read the response
resp = u.read()
```

If you need to supply some custom HTTP headers in the outgoing request such as a change to the user-agent field, make a dictionary containing their value and create a Request instance and pass it to `urlopen()` like this:

```python
from urllib import request, parse

# Extra headers
headers = {
 'User-agent' : 'none/ofyourbusiness',
 'Spam' : 'Eggs'
}

# Create a request object with headers passed as an argument
req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request 
u = request.urlopen(req)

# Read the response
resp = u.read()

```

### Using the Request Library for more complex scenarios

A notable feature of requests is how it returns the resulting response content from a request. In the below example, the `resp.text` attribute gives you the Unicode decoded text of a request. However, if you access `resp.content`, you get the raw binary content instead. On the other hand, if you access `resp.json`, then you get the response content interpreted as JSON.

Here is an example of using requests to make a HEAD request and extract a few fields of header data from the response:
```python
import requests

# Make a HEAD request
resp = requests.head('http://www.python.org/index.html')

# Return the status code of the request
status = resp.status_code
print(status)

# Return the last modified date to a variable
last_modified = resp.headers['last-modified']
print(last_modified)

# Return the content-type to a variable
content_type = resp.headers['content-type']
print(content_type)

# Return the content-length to a variable
content_length = resp.headers['content-length'
print(content_length)

# Decoded text returned by the request
text = resp.text
print(text)
```

Here is a requests example that executes a login into the Python Package index using basic authentication:
```python

import requests

resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user','password'))
```

Here is an example of using requests to pass HTTP cookies from one request to the next:
```python
import requests

# First request
resp1 = requests.get(url)

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)
```
```python
# Last, but not least, here is an example of using requests to upload content:

import requests

# make the url string
url = 'http://httpbin.org/post'

# encode a csv file 
files = { 'file': ('data.csv', open('data.csv', 'rb')) }

# Make the POST Request
r = requests.post(url, files=files)
```
### Summary:
For really simple HTTP client code, using the built-in `urllib` module is usually fine. However, if you have to do anything other than simple `GET` or `POST` requests, you really can’t rely on its functionality. This is where a third-party module, such as `requests`, comes in handy.

If you have to write code involving proxies, authentication, cookies, and other details, using `urllib` is awkward and verbose. 

For example, here is a sample of code that
authenticates to the Python package index:
```python
import urllib.request

auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')

# Build a url reader object
opener = urllib.request.build_opener(auth)

# Make a request object with authentication
r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')

# Use the url opener to make the POST request 
u = opener.open(r)

# Read the response
resp = u.read()

# From here. You can access more pages using opener
```

### Using TCP

__Transmission Control Protocol__, or TCP protocol for short, is a standard for exchanging data between different devices in a computer network. TCP allows for transmission of information in _both_ directions. This means that computer systems that communicate over TCP can send and receive data at the same time, similar to a telephone conversation. The protocol uses segments (packets) as the basic units of data transmission. In addition to the payload, segments can also contain control information and are limited to 1,500 bytes. The TCP software in the network protocol stack of the operating system is responsible for establishing and terminating the end-to-end connections as well as transferring data.

The TCP software is controlled by the various network applications, such as web browsers or servers, via specific interfaces. Each connection must always be identified by two clearly defined endpoints (client and server). It doesn’t matter which side assumes the client role and which assumes the server role. All that matters is that the TCP software is provided with a unique, ordered pair consisting of IP address and port (also referred to as "2-tuple" or "socket") for each endpoint.

An easy way to create a TCP server is to use the `socketserver` library. 

In the below code, you define a special handler class that implements a `handle()` method for servicing client connections. The request attribute is the underlying client socket and `client_address` has client address.

```python
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
    print('Got connection from', self.client_address)
    while True:
        msg = self.request.recv(8192)
        if not msg:
            break
        self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
```

To test the server, run it and then open a separate Python process that connects to it

```python
from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
```
```python
s.recv(8192)
b'Hello'
```

In many cases, it may be easier to define a slightly different kind of handler. Here is an example that uses the `StreamRequestHandler` base class to put a file-like interface on the underlying socket:

```python
from socketserver import StreamRequestHandler, TCPServer, ThreadingTCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
        # self.wfile is a file-like object for writing
            self.wfile.write(line)

if __name__ == '__main__':
    # Single client request (DEFAULT)
    serv = TCPServer(('', 20000), EchoHandler)
    
    # Multi client request
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
```

`socketserver` makes it relatively easy to create simple TCP servers. However, you should be aware that by default the servers are single threaded and can only serve one client at a time. If you want to handle multiple clients, either use `ForkingTCPServer` or `ThreadingTCPServer`.   

### Using UDP

__User Datagram Protocol__, or UDP, is a communication protocol used across the Internet for especially time-sensitive transmissions such as video playback or DNS lookups. It speeds up communications by not formally establishing a connection before data is transferred. This allows data to be transferred very quickly, but it can also cause packets to become lost in transit — and create opportunities for exploitation in the form of DDoS attacks

Compared to other protocols, UDP accomplishes the data transfer process in a simple fashion:
* it sends packets (units of data transmission) directly to a target computer, without establishing a connection first
* does not indicating the order of packets, 
* does not check whether packets arrived as intended

As with TCP, UDP servers are also easy to create using the socketserver library. For example, here is a simple time server:

```python

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()
```

As before, you define a special handler class that implements a handle() method for servicing client connections. The request attribute is a tuple that contains the incoming `datagram` and underlying socket object for the server. The client_address contains the client address. To test the server, run it and then open a separate Python process that sends messages
to it:

example:
```python
>>> from socket import socket, AF_INET, SOCK_DGRAM
>>> s = socket(AF_INET, SOCK_DGRAM)
>>> s.sendto(b'', ('localhost', 20000))
0
>>> s.recvfrom(8192)
(b'Wed Aug 15 20:35:08 2012', ('127.0.0.1', 20000))
```

### Communicating between Interpreters

Lets see and example where you are running multiple instances of the Python interpreter on different machines and you would like to exchange data between interpreters using messages. It is easy to communicate between interpreters if you use the `multiprocessing.connection` module. 

Here is a simple example of writing an echo server:
```python
`
from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
        except EOFError:
            print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey=b'peekaboo')
```

Here is a simple example of a client connecting to the server and sending various messages:
```python
from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')
c.send('hello')
c.recv()
'hello'

c.send(42)
c.recv()
42

c.send([1, 2, 3, 4, 5])
c.recv()
[1, 2, 3, 4, 5]
```
Unlike a low-level socket, messages are kept intact (each object sent using `send()` is received in its entirety with `recv()` ). In addition, objects are serialized using `pickle`. So any object compatible with pickle can be sent or received over the connection.

### Working with SSL to improve Security

__Secure Sockets Layer__, or SSL is an encryption-based Internet security protocol. It was first developed by Netscape in 1995 for the purpose of ensuring privacy, authentication, and data integrity in Internet communications. SSL is the predecessor to the modern TLS encryption used today.

__Note:__ A website that implements SSL/TLS has "HTTPS" in its URL instead of "HTTP."

Let say we want to implement a network service involving sockets where servers and clients authenticate themselves and encrypt the transmitted data using SSL.

The `ssl` module provides support for adding SSL to low-level socket connections. In particular, the `ssl.wrap_socket()` function takes an existing socket and wraps an SSL layer around it. 

For example, here’s an example of a simple echo server that presents a server certificate to connecting clients:
```python
from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem' # Private key of the server
CERTFILE = 'server_cert.pem' # Server certificate (given to client)

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')
    
def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    # Wrap with an SSL layer requiring client certs
    s_ssl = ssl.wrap_socket(
        s,
        keyfile=KEYFILE,
        certfile=CERTFILE,
        server_side=True
    )
 
    # Wait for connections
    while True:
        try:
            c,a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))

echo_server(('', 20000))
```
Here is an interactive session that shows how to connect to the server as a client. The client requires the server to present its certificate and verifies it:

```python
from socket import socket, AF_INET, SOCK_STREAM
import ssl

s = socket(AF_INET, SOCK_STREAM)
s_ssl = ssl.wrap_socket(
    s, 
    cert_reqs=ssl.CERT_REQUIRED,
    ca_certs = 'server_cert.pem'
)

# Send message
s_ssl.connect(('localhost', 20000))
s_ssl.send(b'Hello World?')
12

# Receive response
s_ssl.recv(8192)
b'Hello World?'
```

The problem with all of this low-level socket hacking is that it doesn’t play well with existing network services already implemented in the standard library. For example, most server code (HTTP, XML-RPC, etc.) is actually based on the socketserver library. Client code is also implemented at a higher level. It is possible to add SSL to existing services, but a slightly different approach is needed. First, for servers, SSL can be added through the use of a <u>mixin class</u> like this:

> What is a __mixin?__
A __mixin__ is a class that provides method implementations for reuse by multiple related child classes. 
> * A mixin doesn’t define a new type. Therefore, it is not intended for direction instantiation.
> * A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, implementing closely related methods.
> * Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.
> * Since Python doesn’t define a formal way to define mixin classes, it’s a good practice to name mixin classes with the suffix Mixin.

```python
import ssl
class SSLMixin:
    '''
    Mixin class that adds support for SSL to existing servers based on the socketserver module.
    '''

    def __init__(self, *args, keyfile=None, certfile=None, certs=None, cert_reqs=ssl.NONE, **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(
            client,
            keyfile = self._keyfile,
            certfile = self._certfile,
            ca_certs = self._ca_certs,
            cert_reqs = self._cert_reqs,
            server_side = True
        )
        return client_ssl, addr
```

### Event Driven I/O

We have previously discussed topics based on _event-driven_ or _asynchronous I/O_, but you are not entirely sure what it means, how it actually works under the hood, or how it might impact your program if you use it.

At a fundamental level, event-driven I/O is a technique that takes basic I/O operations (e.g. reads and writes) and converts them into events that must be handled by your program. 

For example, whenever data was received on a socket, it turns into a "receive" event that is handled by some sort of callback method or function that you supply to respond to it. As a possible starting point, an event-driven framework might start with a base class that implements a series of basic event handler methods like this: 

```python

class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')
 
    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False
 
    def handle_receive(self):
        'Perform the receive operation'
        pass
 
    def wants_to_send(self):
        'Return True if sending is requested'
        return False
 
    def handle_send(self):
        'Send outgoing data'
        pass
```
Instances of this class then get plugged into an event loop that looks like this:

```python
import select
def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

    for h in can_recv:
        h.handle_receive()

    for h in can_send:
        h.handle_send()
```

Thats pretty much it. The key to the event loop is the `select()` call, which polls file descriptors for
activity. Prior to calling `select()`, the event loop simply queries all of the handlers to see which ones want to _receive_ or _send_. It then supplies the resulting lists to select(). As a result, `select()` returns the list of objects that are ready to receive or send. The corresponding `handle_receive()` or `handle_send()` methods are then triggered.

One potential benefit of event-driven I/O is that it can handle a very large number of simultaneous connections without ever using threads or processes. That is, the `select()` call (or equivalent) can be used to monitor hundreds or thousands of sockets and respond to events occuring on any of them. Events are handled one at a time by the event loop, without the need for any other concurrency primitives.

The downside to event-driven I/O is that there is no true concurrency involved. If any of the event handler methods blocks or performs a long-running calculation, it blocks the progress of everything. There is also the problem of calling out to library functions that aren’t written in an event-driven style. There is always the risk that some library call will block, causing the event loop to stall.