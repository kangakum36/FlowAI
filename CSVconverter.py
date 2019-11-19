# Concatenates all the rows in a CSV file into one, which we call a "Flat File"

import os
import csv

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

changes = {
    '\n': '',
    }

with open(os.path.join(__location__, 'CAP 01 2019_Tube 6_001.csv')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count = 0
    antibodies = []
    elements = []
    antibodies_header = []

    for row in csv_reader:
        if row_count == 0:
            antibodies = row
            row_count += 1
        else:
            for i in row:
                elements.append(i)
                elements.append(',')
            row_count += 1
    col_count = len(row)
    cell_count = row_count - 1
    for x in range(cell_count):
        cell_number = x + 1
        antibody_num = x % len(antibodies)
        for y in range(len(antibodies)):
            antibodies_header.append(str(cell_number) + '-' + antibodies[y])
            antibodies_header.append(',')


    new_csv_elements = antibodies_header + elements

with open("output.csv", "w") as output_file:
    writer = csv.writer(output_file, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(antibodies_header)
    writer.writerow(elements)