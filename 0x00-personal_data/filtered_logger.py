#!/usr/bin/env python3
"""
filtered_logger module handles logging with obfuscated PII fields,
database connection, and log filtering.
"""
import re
import os
import logging
import mysql.connector
from typing import List, Tuple


PII_FIELDS: Tuple[str] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate PII fields in the log message.

    Args:
    - fields: list of field names to obfuscate
    - redaction: string to replace the field's value with
    - message: log message in format "key=value"
    - separator: the character separating key-value pairs

    Returns:
    - Obfuscated log message
    """
    pattern = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to filter PII fields from log records """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
        - fields: list of field names to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log message, obfuscating PII fields.

        Args:
        - record: The logging record to format

        Returns:
        - Formatted log message with obfuscated PII fields
        """
        log_msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            log_msg, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates a logger that handles PII with a RedactingFormatter.

    Returns:
    - Configured logger with PII filtering
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to a secure database using credentials from environment variable.

    Returns:
    - MySQLConnection object to interact with the database
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )


def main() -> None:
    """
    Retrieve and log all rows from the users table in a filtered format.
    Logs are displayed with obfuscated sensitive information.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    logger = get_logger()

    for row in rows:
        # Assuming the table has columns in this order:
        # name, email, phone, ssn, password, ip, last_login, user_agent
        name, email, phone, ssn, password, ip, last_login, user_agent = row
        message = (
            f"name={name}; email={email}; phone={phone}; ssn={ssn}; "
            f"password={password}; ip={ip}; last_login={last_login}; "
            f"user_agent={user_agent};"
        )
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
