# Clamd_Upload_Web_Server
This is a simple web server that lets you uploads file and uses clamd to check if it is malicious.

Install Clamd

```
sudo apt install clamav-daemon clamav-freshclam clamav-unofficial-sigs
sudo freshclam
sudo service clamav-daemon start
```

Install Python Dependencies

```
pip install flask
pip install clamd
```
Create folder in cli/terminal. This is where the web server will store uploaded files. 

```
mkdir /tmp/Malware
```
