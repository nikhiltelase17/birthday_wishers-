# Birthday Reminder and Greeting System

A simple Python script to check for birthdays in a CSV file and send personalized birthday greetings via email.

## Usage

1. Ensure you have the required dependencies installed:

    ```bash
    pip install pandas
    ```

2. Create a CSV file named `birthdays.csv` with the following format:

    ```csv
    name,email,month,day
    John Doe,johndoe@example.com,5,15
    ```

    Add more entries as needed, where `month` and `day` represent the birthday.

3. Customize birthday letter templates:

    - Place letter templates in the `letter_templates` directory, named `letter_1.txt`, `letter_2.txt`, etc.
    - Use the placeholder `[NAME]` in the letter templates, which will be replaced with the recipient's name.

4. Update email credentials:

    - Replace the placeholder values in the script with your Gmail email and password.

5. Run the script:

    ```bash
    python birthday_reminder.py
    ```

## Important Note

Make sure to enable "Less secure app access" for the Gmail account you use to send emails. You can do this in your Google Account settings.

---

Remember to replace placeholder values and add more details if needed based on your specific use case or any additional functionalities you may have in your script.
