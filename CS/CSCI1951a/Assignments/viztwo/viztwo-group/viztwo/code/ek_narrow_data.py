import csv
import json

def main():
    # Dictionary to keep track of donations per state
    info = {}

    # Open json file; store line of data
    with open('data/data.json', 'rb') as f:
        for line in f:
            json_data = json.loads(line)
    
    # Store data array in list  
    entry_list = json_data["data"]

    # Iterate over list for relevant information
    for item in entry_list:
        # Only funding projects will have an amount field
        if item["event_name"] == "Fund Project":
            # Collect state and amount information
            state = item["location"]["state"].encode('utf-8')
            funds = item["amount"]

            # If the state is in the dictionary, update its donation total
            if state in info:
                info[state] = info[state] + funds

            # Otherwise, create an entry for it with this amount.
            else:
                info[state] = funds

    # Print out the minimum and maximum (to make bucket sizes easier to find)
    max_entry = info["RI"]
    min_entry = info["RI"]
    for entry in info:
        if info[entry] > max_entry:
            max_entry = info[entry]
            max_state = entry
        if info[entry] < min_entry:
            min_entry = info[entry]
            min_state = entry

    print max_state, " donated the most: ", str(max_entry)
    print min_state, " donated the least: ", str(min_entry)

    # Write to 'state_donations.csv'. 
    with open('data/state_donations.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["state", "amount"])
        for entry in info:
            to_write = [entry, info[entry]]
            writer.writerow(to_write)

if __name__ == "__main__":
    main()
 