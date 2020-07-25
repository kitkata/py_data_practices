from csv import reader
import os
opened_file = open(os.path.realpath("Files\AppleStore.csv"), encoding="utf8")
read_file = reader(opened_file)
apps_data = list(read_file)

# Find the highest rating in the app list
temp = 0
for app in apps_data[1:]:
    if float(app[7]) > temp:
        temp = float(app[7])

rating = []
rating_tot = []
name = []
for app in apps_data[1:]:
    # Display app only when the count of rating is more than 20000
    if float(app[7]) == temp and int(app[5]) >= 20000:
        name.append(app[1])
        rating.append(app[7])
        rating_tot.append(app[5])

i = 0
if len(name) > 0:
    print(str(len(name)) + " of apps found.")
    print(apps_data[0][1], apps_data[0][7], apps_data[0][5])
    for app in name:
        print(app + ": " + str(rating[i]) + ", number of ratings: " + str(rating_tot[i]))
        i+=1
else:
    print("No app found")