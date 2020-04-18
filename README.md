# Flask-for-sharperang
This is a developpment for web side for my fork of sharperang

# Environment
- Windows10 x64
- Visual Studio Code 1.44.2+
- Python 3.7.4+
- Zadig 2.5+ (for detecting paperang device)

# Installation

## Detect the paperang device

- Download the application "Zadig" ( https://zadig.akeo.ie/ ).
- Click `Options` menu, and click `List All Devices`.
- Look in the devices list for either `Paperang` or `MPTII Printer`.
- Make sure the driver list on the right side says "WinUSB".
- Click `Replace Driver`.

<img src="https://user-images.githubusercontent.com/41846652/78510298-8052da00-7794-11ea-9b5a-6e19c8a65d56.png" width="450" height="200">

## Install Flask

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install -r requirements.txt
```

I use package `flask-ngrok` to make Flask app running on localhost over the public internet via [ngrok tool](https://ngrok.com/])

To launch app with ngrok, enter:

```python
python app.py
```

Now you can see a random url generated in the output console:

For example:

```
Forwarding                    http://63b82d2d.ngrok.io -> http://localhost:5000
Forwarding                    https://63b82d2d.ngrok.io -> http://localhost:5000
```

