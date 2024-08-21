import csv
import os

def sanitize_content(content):
    # Define replacement for problematic characters
    sanitized = content.replace('\x00', '')  # Null bytes
    sanitized = sanitized.replace('\x01', '')  # Unusual control characters
    # Add more replacements as needed
    return sanitized

def sanitize_csv_file(file_path):
    temp_file_path = file_path + '.tmp'

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        reader = csv.reader(file, delimiter=';')
        rows = [sanitize_content(''.join(row)).split(';') for row in reader]

    with open(temp_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(rows)

    os.replace(temp_file_path, file_path)

# Example usage
sanitize_csv_file('./log_files/tmp_log_client.csv')