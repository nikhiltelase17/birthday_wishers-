# Birthday Greeting System

A Python script that automates the process of sending birthday greetings via email. The script reads birthday data from a CSV file, checks if there are any birthdays on the current day, and sends personalized birthday letters to the respective individuals.

## Features

- Reads birthday data from a CSV file.
- Checks for birthdays on the current day.
- Sends personalized birthday letters via email.
- Supports multiple letter templates.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- pandas library (`pip install pandas`)

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/nikhiltelase17/birthday_wishers.git
    cd birthday-greeting-system
    ```

2. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure CSV Data:**

    - Create a CSV file named `birthdays.csv` with the following columns: `name`, `email`, `month`, `day`.
    - Add entries for each person's name, email, birth month, and day.

        ```csv
        name,email,month,day
        John Doe,johndoe@example.com,5,15
        ```

5. **Create Letter Templates:**

    - Place letter templates in the `letter_templates` directory, named `letter_1.txt`, `letter_2.txt`, etc.
    - Use the placeholder `[NAME]` in the letter templates, which will be replaced with the recipient's name.

6. **Update Email Credentials:**

    - Replace the placeholder values in the script with your Gmail email and password.

7. **Enable "Less Secure App Access" on Gmail:**

    - To allow the script to send emails via Gmail, enable "Less secure app access" for the Gmail account you use in the script. You can do this in your Google Account settings.

## Usage

Run the script using the following command:

```bash
python birthday_reminder.py
```

The script will check for birthdays on the current day and send personalized birthday letters to the respective email addresses.

## Important Note

- Ensure that you are compliant with Gmail's security policies when using your email credentials in the script.
- It is recommended to use a dedicated Gmail account for sending birthday greetings.

---

Feel free to adjust the instructions and details based on your specific needs and preferences.
