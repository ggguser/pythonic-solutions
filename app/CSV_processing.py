def count_number_of_entries_in_csv():

    with open('realty.csv', newline='') as csv_file:
        realty_reader = csv.reader(csv_file, delimiter=';')
        row_count = sum(1 for row in realty_reader)

    return row_count
