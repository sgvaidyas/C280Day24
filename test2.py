import json
import datetime
from pprint import pprint

with open('restaurant.json', 'r') as f:
    data = f.readlines()
f.close()
restuarants = []

for row in data:
     x = json.loads(row)
     restuarants.append(x)


def replace_timestamps(data):
    new_data = data
    for grade in new_data["grades"]:
        temp = int(grade["date"]["$date"])
        try:
            grade["date"]["$date"] = datetime.datetime.fromtimestamp(temp)
        except OSError:  # Format is in milliseconds
            grade["date"]["$date"] = datetime.datetime.fromtimestamp(temp / 1000)
    return new_data
dated_restuarants = list(map(replace_timestamps,restuarants))

print(dated_restuarants[0])

def review_filter(restuarants):
    index = 1
    for restuarant in list(restuarants["grades"]):
        pprint(f"INDEX {index}")
        index+=1
        pprint(restuarant)
        temp = len(restuarant)
        if temp >= 5:
           return True
        else:
            return False


restuarants_filtered = filter(review_filter,dated_restuarants)
print(list(restuarants_filtered))
