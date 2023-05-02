# Clickjacking POC
A Python package for creating a clickjacking proof of concept (POC).

<p align="center"><img src="https://raw.githubusercontent.com/marksowell/Clickjacking-POC/main/images/screenshot.png" width="300px" />

## Requirements

- Python 3.6 or newer
- Google Chrome installed on the system
- Write permissions for the current directory for the user running the script

## Installation
Install using pip:

```
pip install clickjacking-poc
```

## Usage
Run the script with the following command:

```
clickjacking-poc <URL> [-p <port>]
```

### Arguments
`<URL>`      The URL of the page to be displayed in the clickjacking POC.  
`-p <port>` (Optional) The port number to use for the temporary web server. If not specified, the default port is 80.

### Example

```
clickjacking-poc https://example.com/login
```

```
clickjacking-poc https://example.com/login -p 8000
```

## License
The scripts and documentation in this project are released under the [MIT License](https://github.com/marksowell/Clickjacking-POC/blob/main/LICENSE.txt).