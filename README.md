# QUBE-RT Spaceship Rental Management Project

End to end application for spaceship rental management using Flask

### Steps to be followed in order to run the app

1. Clone this repository in your local machine.
2. Change the directory

```console
sooryakant@ideapad-5-pro:~/Documents$ cd qube-rt/
```

3. Create a new virtual environment-

```console
python -m venv env
```

4. Activate the new virtual environment-

```console
sooryakant@ideapad-5-pro:~/Documents/qube-rt$ source env/bin/activate
```

5. Upgrade the python version if it is not 3.10

  - For Window follow this- https://linuxhint.com/update-python-windows/
  - For Ubuntu follow this- https://cloudbytes.dev/snippets/upgrade-python-to-latest-version-on-ubuntu-linux

6. Install the requirements-

```console
(env) sooryakant@ideapad-5-pro:~/Documents/qube-rt$ pip install -r requirements.txt
```

7. Run the app-

```console
(env) sooryakant@ideapad-5-pro:~/Documents/qube-rt$ python app.py
```

8. Open the URL in your favorite browser-

```console
http://127.0.0.1:8080/
```

9. Send the below data points as a input-

```json
{
    "data": [
        {
            "name": "Contract1",
            "start": 0,
            "duration": 5,
            "price": 10
        },
        {
            "name": "Contract2",
            "start": 3,
            "duration": 7,
            "price": 14
        },
        {
            "name": "Contract3",
            "start": 5,
            "duration": 9,
            "price": 8
        },
        {
            "name": "Contract4",
            "start": 5,
            "duration": 9,
            "price": 7
        }
    ]
}
```

Submit the data and get the response.
