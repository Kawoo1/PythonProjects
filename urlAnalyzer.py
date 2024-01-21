import re
import mysql.connector

# This code is authored by Kyle Shanahan
# This python script analuzes URLs in a text file and insert them into a "MySQL" database
# In the comments below are the syntax used in this script and an explanation on how to utilize it individually.

#  1) Function to extract URLs from a text file
def extract_urls(file_path):
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    with open(file_path, 'r') as file:
        content = file.read()

    urls = re.findall(url_pattern, content)
    return urls

# 2) Function to insert URLs into a MySQL database
def insert_urls_into_database(urls):
    # Replace with your MySQL database credentials
    db_connection = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )

    cursor = db_connection.cursor()

    # 3) Replace 'your_table_name' with your actual table name. In this examplt the table name is 'im_your_table'
    insert_query = "INSERT INTO im_your_table (url_column) VALUES (%s)"

    for url in urls:
        cursor.execute(insert_query, (url,))

    db_connection.commit()
    db_connection.close()

# 4) Replace '/path/to/your/textfile.txt' with the ACTUAL path to your text file
file_path = '/path/to/your/textfile.txt'

#--------------------------------------------------------------------------------------------------------------------
# Extract URLs from the text file
urls = extract_urls(file_path)
# Insert URLs into the database
insert_urls_into_database(urls)
