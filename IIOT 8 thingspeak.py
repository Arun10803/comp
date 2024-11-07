import http.client , urllib.request,urllib.parse
key = 'E3FA97PNKV3CQ70Z' # copy the write API key

t=int(22)

while True:
    t=t+1
    print ("temperature",t)
    params=urllib.parse.urlencode({'field1':t,'key':key})
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    con=http.client.HTTPConnection("api.thingspeak.com")
    con.request("POST","/update",params,headers)
    response=con.getresponse()
    print (response.status,response.reason)
    data=response.read()
    con.close()


'''
This code is used to send temperature data to ThingSpeak, an IoT platform that allows you to collect and store sensor data. It uses HTTP requests to interact with the ThingSpeak API and send data to a specified channel.

Here’s a step-by-step breakdown:

1. Imports:
python
Copy code
import http.client, urllib.request, urllib.parse
http.client: Provides functions for making HTTP requests. In this case, it is used to send a POST request to the ThingSpeak API.
urllib.request and urllib.parse: These modules are used for handling URL encoding and building the request to send data in the right format to the ThingSpeak API.
2. API Key and Initial Temperature Value:
python
Copy code
key = 'E3FA97PNKV3CQ70Z'  # API Key for authentication
t = int(22)  # Initial temperature value
key: The API key is a unique identifier that ThingSpeak uses to authenticate requests from your account. You need to use the key associated with your ThingSpeak channel.
t = int(22): Initializes the temperature value to 22. This value will be updated and sent to ThingSpeak in each iteration of the loop.
3. Infinite Loop:
python
Copy code
while True:
    t = t + 1  # Increase temperature by 1
    print("temperature", t)  # Print the current temperature value
while True:: This is an infinite loop. It will keep running, sending updated temperature values to ThingSpeak indefinitely.
t = t + 1: Increments the temperature by 1 with each iteration.
print("temperature", t): Prints the current temperature to the console.
4. Preparing the Request Data:
python
Copy code
params = urllib.parse.urlencode({'field1': t, 'key': key})
params: Encodes the parameters that will be sent in the HTTP POST request to ThingSpeak. The parameters include:
field1: The field that will hold the temperature value (t).
key: The API key for authentication.
urllib.parse.urlencode takes a dictionary of key-value pairs and encodes them into a URL-encoded string (e.g., field1=23&key=E3FA97PNKV3CQ70Z).
5. Setting HTTP Request Headers:
python
Copy code
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
Content-type: application/x-www-form-urlencoded: Specifies that the data is being sent in URL-encoded format.
Accept: text/plain: Specifies that the response from the server is expected to be plain text.
6. Creating the HTTP Connection and Sending Data:
python
Copy code
con = http.client.HTTPConnection("api.thingspeak.com")
con.request("POST", "/update", params, headers)
http.client.HTTPConnection("api.thingspeak.com"): Creates a connection to the ThingSpeak server at api.thingspeak.com.
con.request("POST", "/update", params, headers): Sends a POST request to the /update endpoint of ThingSpeak, passing the params and headers created earlier.
7. Getting the Response:
python
Copy code
response = con.getresponse()
print(response.status, response.reason)
con.getresponse(): Sends the request and gets the HTTP response from the ThingSpeak server.
print(response.status, response.reason): Prints the HTTP status code and reason phrase (e.g., 200 OK) to the console, indicating whether the request was successful.
8. Reading and Closing the Response:
python
Copy code
data = response.read()
con.close()
response.read(): Reads the content of the response from the server (though the data is not being used in this code).
con.close(): Closes the connection to the ThingSpeak server to free resources.
Summary of the Code’s Behavior:
The program simulates a sensor that sends temperature data (incremented by 1 in each iteration) to ThingSpeak continuously.
It connects to the ThingSpeak API, formats the data with the field1 value (the temperature) and the API key, and sends it as an HTTP POST request.
The program runs indefinitely, incrementing the temperature and sending the updated value to ThingSpeak every time it loops.
Example of API Request and Response:
A typical request sent by this code will look like:

bash
Copy code
POST /update HTTP/1.1
Host: api.thingspeak.com
Content-type: application/x-www-form-urlencoded
Accept: text/plain

field1=23&key=E3FA97PNKV3CQ70Z
The server will respond with a status like:

Copy code
HTTP/1.1 200 OK
This confirms that the data has been successfully updated on your ThingSpeak channel.
'''