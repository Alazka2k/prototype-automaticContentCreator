import csv
import os


def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip header if present
        return [row[0] for row in csv_reader]


def write_to_csv(file_path, header, rows):
    print("CSV Header:", header)  # Debugging output
    print("CSV Rows:", rows)      # Debugging output
    # Check if the file exists and is not empty
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        # If the file is new or empty, write the header
        if not file_exists:
            writer.writerow(header)

        # Write the new rows, ensuring they are not empty
        for row in rows:
            if any(row):  # Check if the row is not entirely empty
                writer.writerow(row)
