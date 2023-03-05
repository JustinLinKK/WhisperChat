# WhisperChat

The encryption App deployed in python.
This project uses RSA encryption and SHA256 to protect the message.
RSA prevent the MITM attack.

## Usage

If you don't already have a virtual environment for Python in the folder, make one using:

```
py -3 -m venv .venv
.venv\scripts\activate
```

**To get the app running run the following commands**
##Most Simple Demo in python 

```
pip install -r requirements.txt
cd demo


For sender part:
copy the public_keys.txt from the reciever side to the demo folder
python chatClientSender.py
type the destination IP address
type the massage

For reciever part:
Generate the key pairs using python keygeneration.py
enter the public_keys.txt and change the "localhost" to machine IP address
send the public_keys.txt to sender
python chatClientReciever.py to wait for respond

```
## Future Imporvement

```
UI deelopment using JS
Avaliable to request pubilc using non encrypted string and store it
Add exchanger to the network to aollow mor users
Do the groupchat function and replace IP address as username

```


