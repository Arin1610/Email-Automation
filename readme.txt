

# Email Automation Project

## Overview

This project demonstrates a simple email automation script using Python's `smtplib`. The script allows you to send an email to a specified recipient with a custom message.

## Project Setup

### Prerequisites

- Python 3.x installed on your machine.
- Access to a Gmail account (or other SMTP server credentials).

### Script Details

The script performs the following tasks:

1. Prompts the user for the recipient's email address.
2. Asks the user to input the message content.
3. Sends an email using Gmail's SMTP server.


### Usage

1. Open a terminal or command prompt.
2. Run the script:
    ```bash
    python email_automation.py
    ```
3. Follow the prompts to enter the recipient's email address and the message you wish to send.

### Security Note

- **Important:** Do not hard-code your email credentials in the script. Consider using environment variables or a secure vault for storing sensitive information.

### Troubleshooting

- Ensure you have a stable internet connection.
- Verify that your email credentials are correct.
- Ensure that "Less secure app access" is enabled for your Gmail account or use an App Password if two-factor authentication is enabled.
