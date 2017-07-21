#narrow_category.py
import csv
import json
import collections

def main():
    # Dictionary to keep count of number of people in an age range that looked at specified categories
    age_cat = {}
    user_id = []

    # Open json file; store line of data
    with open('data.json', 'rb') as f:
        for line in f:
            json_data = json.loads(line)
    
    # Store data array in list  
    entry_list = json_data["data"]

    # Iterate over list for relevant information
    age_grouper = ["18-24", "25-34", "35-44", "45-54", "55+"]
    state_NE = ["MA", "ME", "VT", "NH", "CT", "RI", "NY", "PA", "NJ"]

    for age_range in age_grouper:
	    for item in entry_list:
	        # Select for the desired age group and single 
	        # Select for session_id
	        if item["age"] == age_range and item["location"]["state"] in state_NE and item["session_id"] not in user_id:
	            # Collect state and amount information

	            user_id.append(item["session_id"])

	            category = item["category"].encode('utf-8')
	            count = 1

	            # If the state is in the dictionary, update its donation total
	            if category in age_cat:
	                age_cat[category] = age_cat[category] + count

	            # Otherwise, create an entry for it with this amount.
	            else:
	                age_cat[category] = count

	    # Print out the minimum and maximum (to make bucket sizes easier to find)
	    max_entry = age_cat["Environment"]
	    min_entry = age_cat["Environment"]
	    max_age = ""
	    min_age = ""
	    for entry in age_cat:
	        if age_cat[entry] > max_entry:
	            max_entry = age_cat[entry]
	            max_age = entry
	        if age_cat[entry] < min_entry:
	            min_entry = age_cat[entry]
	            min_age = entry

	    print "single ", str(age_range)
	    print max_age, " donated the most: ", str(max_entry)
	    print min_age, " donated the least: ", str(min_entry)

	    #Write to 'state_donations.csv'. 

	    age_cat_ordered = collections.OrderedDict(sorted(age_cat.items()))
	    with open('data/age_NE_%s.csv' %age_range, 'wb') as f:
	        writer = csv.writer(f)
	        writer.writerow(["category", "count"])
	        for entry in age_cat_ordered:
	            to_write = [entry, age_cat_ordered[entry]]
	            writer.writerow(to_write)
	    age_cat = {}

if __name__ == "__main__":
    main()
