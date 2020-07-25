from csv import reader
import os
opened_file = open(os.path.realpath("Files\AppleStore.csv"), encoding="utf8")
read_file = reader(opened_file)
apps_data = list(read_file)

# a function to generate freqency table
def freq_table(data_set, index):
    frequency_table = {}
    column_list = []

    for app in data_set[1:]:
        column_list.append(app[index])

    for line in column_list:
        if line in frequency_table:
            frequency_table[line] += 1
        else:
            frequency_table[line] = 1

    return frequency_table

# Print user rating frequency table
ratings_ft = freq_table(apps_data, 7)
content_ratings_ft = freq_table(apps_data, 10)
genres_ft = freq_table(index = 11, data_set = apps_data)

print(ratings_ft)
print(content_ratings_ft)
print(genres_ft)

content_ratings = {}

for app in apps_data[1:]:
    c_rating = app[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1

print(content_ratings)

# Find out the MIN/MAX of the rating counts
rating_count_tot = []
for app in apps_data[1:]:
    ratings_tot = int(app[5])
    rating_count_tot.append(ratings_tot)

ratings_min = min(rating_count_tot)
ratings_max = max(rating_count_tot)

# Rating count within range
rating_counts = {'0 - 500': 0, '501 - 1000': 0, '1001 - 2000': 0, '2001 - 50000': 0, '50001 +': 0}

for row in rating_count_tot:
    if 0 < row <= 500:
        rating_counts['0 - 500'] += 1
    elif 500 < row <= 1000:
        rating_counts['501 - 1000'] += 1
    elif 1001 < row <= 2000:
        rating_counts['1001 - 2000'] += 1
    elif 2001 < row <= 50000:
        rating_counts['2001 - 50000'] += 1
    elif row > 50000:
        rating_counts['50001 +'] += 1

print(rating_counts)

# find mean functions
def extract(data_set, index):
    column = []
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    extracted_col = extract(data_set, index)
    return find_sum(extracted_col) / find_length(extracted_col)

avg_price = mean(apps_data, 4)