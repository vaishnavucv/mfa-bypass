# mfa-bypass
## Flask 2FA Web Application

This is a simple Flask web application designed for demonstrating 2FA (Two-Factor Authentication) bypass techniques using Burp Suite.

## Features

- User login with username and password
- 3-digit MFA (Multi-Factor Authentication) code verification
- Session management with limited MFA attempts

## Requirements

- Python 3.7+
- Flask

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/vaishnavu/mfa-bypass.git
    cd flask-2fa-app
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```
4. one-line command clone-&-run
   ```bash
   git clone https://github.com/vaishnavu/mfa-bypass.git && cd flask-2fa-app && pip install -r requirements.txt && python app.py
   ```
## Usage

1. Access the application at `http://localhost:5000`.
2. Log in with the username `carlos` and password `password123`.
3. Enter the 3-digit MFA code sent to the console.
4. Use Burp Suite to test 2FA bypass techniques.

## License

This project is licensed under the MIT License.

