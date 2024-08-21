import csv
import os

def remove_null_characters(file_path, temp_file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    # Remove null characters
    cleaned_content = content.replace(b'\x00', b'')
    # Write cleaned content to a temporary file
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(cleaned_content)

def process_csv(file_path):
    temp_file_path = file_path + '.tmp'
    
    # Remove null characters and create a temporary file
    remove_null_characters(file_path, temp_file_path)

    # Process the cleaned CSV file
    with open(temp_file_path, 'r', encoding='utf-8', errors='replace') as file:
        reader = csv.reader(file, delimiter=';')
        rows = [row for row in reader]

    # Write the cleaned content back to the original file
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)

    # Remove the temporary file
    os.remove(temp_file_path)

# Example usage
process_csv('./tmp_log_client.csv')
