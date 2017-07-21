import operator,sys
from datetime import datetime
import re

#init(dict count_mat) takes in an empty dictionary
#and initializes every (day,hour) pair to zero
def init(count_mat):
    count_mat = {} #dictionary mapping tuples (day, hour) to counts of crime
    for day in range(7): #days of week
    	for h in range(24): #hours of day
    		count_mat[(day+1, h+1)] = 0
    return count_mat

def count_crime(data, count_mat):
    """This method parses crime dataset and derives the count of crime
    sent at various day,hour pairs.
    Input: file containing crime data in CSV format.
    Hint : Use the Python datetime module 
    """
    # TODO : Fill in count_mat
    time_list = []
    for line in data:
        # TODO : CODE HERE
        line = line.split(',')
        string_time = line[2]
        #print string_time
        ## parsing example time: 12/06/2013 06:30:00 PM
        ## day parses in month(1), day(2), year(3), hour(4). daytime requires in year(3), month(1), day(2) 
        day = re.match(r'^(\d\d)\/(\d\d)\/(\d+)\s(\d\d).*(AM|PM)', string_time)
        if day:
            #print day.group(5)
            if day.group(5) == 'PM':
                hour = int(day.group(4))+12
                if  int(day.group(4)) == 12:
                    hour = 0
                d = datetime(int(day.group(3)), int(day.group(1)), int(day.group(2)), hour)
            else:
                d = datetime(int(day.group(3)), int(day.group(1)), int(day.group(2)), int(day.group(4)))
            time_list.append(d)
            #print d
        else:
            print "no day found"
            
        '''
    for i in time_list:
        for day_match in range(0,6):
            for hour_match in range(0, 24):
                if i.weekday() == day_match and i.hour == hour_match:
                    count_mat[(day_match, hour_match)] += 1
                    print "day {} hour {} count {}".format(day_match, hour_match, count_mat[(day_match, hour_match)])
        '''
    for i in time_list:
        hr = i.strftime('%H')
        if hr != '00':
            hr = int(hr.lstrip("0"))
        else:
            hr = int(hr)+24
        #print hr
        for day_range in range(1,8):
            for hour_range in range(1,25):
                if i.weekday()+1 == day_range:
                    if hr == hour_range:
                        count_mat[(day_range, hour_range)] = count_mat[(day_range, hour_range)] + 1

                #print "weekday 0 hour {} and count {}".format(i.strftime('%H'),count_mat[(1, 1)])
    print "weekday 1 hour 1 and count {}".format(count_mat[(1, 1)])
    print "weekday 1 hour 24 and count {}".format(count_mat[(1, 24)])
    print "weekday 4 hour 10 and count {}".format(count_mat[(4, 10)])
    print "weekday 7 hour 13 and count {}".format(count_mat[(7, 1)])
    print "weekday 7 hour 24 and count {}".format(count_mat[(7, 24)])
    return count_mat


def main():
    data = open(sys.argv[1], 'r') 
    count_mat = init({})
    #print(count_mat)
    count_mat = count_crime(data, count_mat)

    out = open(sys.argv[2], 'w')
    out.write("day\thour\tvalue\n")
    
    #sort by day, hour (ascending)
    sorted_counts = sorted(count_mat.items(), key=operator.itemgetter(0))
    for (x, y) in sorted_counts:
        out.write(str(x[0])+"\t"+str(x[1])+'\t'+str(y)+"\n")
    out.close()

if __name__ == '__main__':
    main()