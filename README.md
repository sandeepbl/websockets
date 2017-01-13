# Websockets in Python

> Trying to implement websockets in Python with the help of the package from [Websocketd.com](http://websocketd.com/)

## Instructions to run:
* Download the Websocketd binary from the above link
* Make sure that you have installed Python2 with sqlite3 module
* Clone the repo to your system and enter into the directory
* Make note of your systems IP address
* Run python webserver with the following command:
~~~
>> python -m SimpleHTTPServer 8181
~~~
* Run the websocket server with the following command:
~~~
>> websocketd --port 8080 python wsUpdate.py
~~~
* In the web browser/s enter the path for the hosted page as shown:
~~~
http://<your-IP-address>/deptNotes.html
~~~
Let me know whar you think.
