### Setup

### Update env file with api key to access the api

```.env -> update API_KEY```


## Docker Setup

### Docker Build

```docker build -t <you username>/<appname>```

To list images

```docker images```

### Run docker image

```docker run -i -t <your username>/<appname>  ```

### Setup on local machine

Install python3.6 - https://www.python.org/downloads/mac-osx/

Install project dependency - ``` pip install -r requirements.txt ```

### Running the code

Usage: ``` python3 find_mac_addr.py --macaddr 44:38:39:ff:ef:57 ```

### Help

```python3 find_mac_addr.py --help```



