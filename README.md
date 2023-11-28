[![made with python](https://img.shields.io/badge/made%20in-python-red)](https://img.shields.io/badge/made%20in-python-red)
[![author](https://img.shields.io/badge/author-shibli2700-blue)](https://img.shields.io/badge/author-shibli2700-blue)
[![co-author](https://img.shields.io/badge/co_author-saami97-green)](https://img.shields.io/badge/author-shibli2700-green)
## Kyubi

A tool to discover Nginx alias traversal misconfiguration, read more [https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/](https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/)

<p align="center"><img src="https://i.postimg.cc/NfvjVmJj/Capture.jpg" /></p>

## Installation

### OPTION 1: 

```
git clone https://github.com/shibli2700/Kyubi.git
cd /Kyubi
sudo python3 setup.py install
pip install .
```

### OPTION 2: Pulling the Docker Image from Docker Hub

You can pull the Docker image from Docker Hub and running it locally using the following command:

```bash
docker pull saydocerr/kyubi
```

```bash
docker run -it saydocerr/kyubi
```


## Options
```
usage: kyubi [-h] [-v] [-a] url

This tool checks nginx alias traversal misconfiguration.

positional arguments:
  url         URL of the target

optional arguments:
  -h, --help  show this help message and exit
  -v          increase verbosity
  -a          append segment in the end
  ```

 


## Usage

```
$ kyubi -v https://127.0.0.1/resources/images/users/profile/profile.png
```

## Future Addition

* Brute forcing with filenames and directories.
* Web Interface.
