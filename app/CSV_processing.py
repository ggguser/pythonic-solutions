import csv


def from_csv_to_dict():

    with open('metro.csv', newline='') as csv_file:
        metro_import = csv.reader(csv_file, delimiter=';')
        #  Composing the dict, converting values to appropriate types
        metro_csv_import = {metro[0]: (float(metro[1]), float(metro[2])) for metro in metro_import}

    return metro_csv_import


def count_number_of_entries_in_csv():

    with open('realty.csv', newline='') as csv_file:
        realty_reader = csv.reader(csv_file, delimiter=';')
        row_count = sum(1 for row in realty_reader)

    return row_count


def get_hash_of_csv():

    with open('realty.csv', 'rb') as realty_csv:
        csv_reader = realty_csv.read()
        csv_hash = hashlib.md5(csv_reader).hexdigest()
    return csv_hash


def write_hash_of_csv(csv_hash):

    with open('realty.csv.md5', 'w') as realty_hash_file:
        realty_hash_file.write(str(csv_hash))


def read_hash_of_csv():

    with open('realty.csv.md5') as csv_hash_file:
        csv_hash = csv_hash_file.read()
    return csv_hash
