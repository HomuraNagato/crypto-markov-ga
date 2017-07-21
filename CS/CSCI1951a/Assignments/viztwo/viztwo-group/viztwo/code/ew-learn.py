import csv
import json
from collections import defaultdict
import collections

def main():
    # Dictionary to keep track of donations per state

    categoryToAgeToFrequency = defaultdict(lambda : defaultdict(int))

    # Open json file; store line of data
    with open('../data/data.json', 'rb') as f:
        for line in f:
            json_data = json.loads(line)
    
    # Store data array in list  
    entry_list = json_data["data"]

    for entry in entry_list:
    	if entry["event_name"] == "Fund Project" and entry["gender"] == "M" and entry["marital_status"] == "single":
    		age = entry["age"]
    		category = entry["category"]
    		categoryToAgeToFrequency[category][age] += 1
    
    with open('../data/categoryToAgeToFrequency.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["category", "18-24", "25-34", "35-44", "45-54", "55+"])
        for key, value in categoryToAgeToFrequency.iteritems():
            to_write = []
            to_write.append(key)
            #print key
            for key, value in categoryToAgeToFrequency[key].iteritems():
                #print key, value
                to_write.append(value)
            writer.writerow(to_write)
        
if __name__ == "__main__":
    main()



