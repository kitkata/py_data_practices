from csv import reader
import os
opened_file = open(os.path.realpath("Files\AppleStore.csv"), encoding="utf8")
read_file = reader(opened_file)
apps_data = list(read_file)

print(apps_data[0])
print(apps_data[1])