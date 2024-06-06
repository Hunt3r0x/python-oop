# Portswigger (burp pro) free trial automation
This Python script automates the process of signing up for a free trial of PortSwigger's Burp Suite Professional.

1. **Imports**: It imports necessary modules:
   - `requests` for making HTTP requests.
   - `BeautifulSoup` from `bs4` for parsing HTML.
   - `random` and `string` for generating random strings.
   - `click` for creating command-line interfaces.
   - `Faker` for generating fake data.

2. **PortSwiggerTrial Class**:
   - Initializes with an email address.
   - Sets up a session and defines default headers.
   - Generates a fake name for the trial.
   - Defines methods to extract the Request Verification Token and Order ID from HTML responses.
   - Sends HTTP requests to different endpoints of the trial signup process:
     - `get_initial_token()` fetches the initial Request Verification Token.
     - `first_post_request()` submits the email and initial token to start the trial.
     - `second_post_request()` proceeds with the trial process after the first submission.
     - `third_post_request()` submits the user's objective.
     - `fourth_post_request()` submits user details like role, experience, etc.
   - `run()` method orchestrates the entire trial process by calling these methods in sequence.

3. **Main Function**:
   - Uses `click` to prompt the user for their email address.
   - Creates an instance of `PortSwiggerTrial` with the provided email.
   - Calls `run()` method to start the trial process.

4. **Command Line Interface**:
   - The script is designed to be run from the command line. When executed directly, it prompts the user to enter their email address.

5. **Execution**:
   - When run, it automates the process of signing up for the Burp Suite Professional trial by simulating HTTP requests and form submissions.

6. **Usage**
```python
python3 ./portswigger.py --email any@domain.edu.uk
```

7. **Comments**:
   - The comments in the code help explain each step of the signup process and provide context for the purpose of each method and request.

8. **Objective**:
   - The objective of this script is to simplify the process of signing up for the trial by automating the manual steps involved.

9. **Disclaimer**:
   - It's important to note that automating web interactions like this should only be done in accordance with the terms of service of the website in question.
