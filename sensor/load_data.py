import os, glob, csv

def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), "datasets", "*.csv"))
    #Loop each thru list of files
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            #Create a csv.DistReader
            data_reader = csv.DictReader(data_file, delimiter=',')
            #Loop over each row
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data
