import csv

def saveAsCSV(array, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=",")


            for row in array:
                csv_writer.writerow(row)