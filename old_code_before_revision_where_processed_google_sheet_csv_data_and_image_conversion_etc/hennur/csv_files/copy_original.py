import os


def run():
    csv_file_name = "Directory Form - Form Responses_edited.csv"
    file_source_location = os.path.join("csv_files", "original")
    csv_url_source = os.path.join(file_source_location, csv_file_name)

    csv_url_destination = os.path.join("csv_files", "original.csv")

    # copying csv_files file to csv_files base directory
    with open(csv_url_source, 'r') as source_file:
        with open(csv_url_destination, 'w') as destination_file:
            destination_file.write(source_file.read())

    print(f"CSV FILE COPIED FROM '{csv_url_source}' TO '{csv_url_destination}'")
