# FIleDomainParser

`FIleDomainParser` is a Python script designed for reading file contents and making HTTP requests using specified methods and domains. The script employs Object-Oriented Programming (OOP) principles and demonstrates handling command-line arguments to configure its behavior.

## Overview

The script performs two primary tasks:
1. **File Reading**: Reads and displays the contents of a specified file.
2. **HTTP Requests**: Makes HTTP requests to a given domain using a specified method and outputs specific response attributes.

## Prerequisites

Ensure you have Python 3.x installed. Additionally, the script requires the `requests` library. Install it using pip if necessary:

```bash
pip install requests
```

## Usage

To use the script, run it from the command line with the desired arguments. 

### Command-Line Arguments

- `-file` (Optional): Path to the file to read.
- `-domain` (Optional): Domain to make the HTTP request to.
- `-X` (Optional): HTTP method to use (e.g., `GET`, `POST`).
- `-type` (Optional): Response attribute to output (e.g., `status_code`, `text`, `headers`).

### Examples

**Read a file:**

```bash
python3 ./shitoopidea.py -file example.txt
```

**Make an HTTP GET request and output the status code:**

```bash
python3 ./shitoopidea.py -domain http://example.com -X GET -type status_code
```

**Make an HTTP POST request and output the response text:**

```bash
python3 ./shitoopidea.py -domain http://example.com -X POST -type text
```

## Script Details

- **Class**: `FIleDomainParser`
  - **Methods**:
    - `__init__()`: Initializes the parser and parses command-line arguments.
    - `parse_args()`: Defines and parses command-line arguments.
    - `readfile(path)`: Reads the content of the specified file.
    - `curl(domain, method)`: Makes an HTTP request using the specified method.
    - `mainfn()`: Main function to execute the file reading and HTTP request tasks based on provided arguments.

## Error Handling

- **File Errors**: Handles `FileExistsError` and `IOError` during file operations.
- **HTTP Errors**: Catches and prints errors related to HTTP requests, such as invalid methods.

## License

This script is provided as-is for practice and educational purposes. Feel free to modify and use it as needed.