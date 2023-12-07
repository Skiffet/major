# import csv
# with open("seat.csv") as f:
#     data = csv.reader(f)
# for i in data:
#     print(i)

import json
with open("member.json", "r") as f:
    data = json.load(f)
    print(list(data.keys()))
