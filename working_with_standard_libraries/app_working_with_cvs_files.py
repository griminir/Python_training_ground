import csv

# works but better to use with since close is done automatically
# file = open('data.csv', 'w')
# file.close()

# writing to a csv file
# with open('data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['transaction_id', 'product_id', 'price'])
#     writer.writerow([1000, 2, 50])
#     writer.writerow([1001, 1, 100])

# reading a csv file
with open('data.csv') as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
