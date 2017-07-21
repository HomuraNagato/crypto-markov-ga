#!/usr/bin/env python
import sys
import csv
import re

furniture_path = '../data/furniture.csv'

def main():
    

    with open(furniture_path) as f:
        reader = csv.reader(f)
        for row in reader:
            '''row = str(row)
            m = re.split(',', row)
            print m'''
            new_m = row[24] + ", " + row[13] + ", " + row[19] + ", " + row[35]
            print new_m


            #return
    
    # TODO: clean furniture.csv
    #pass

if __name__ == '__main__':
    '''if len(sys.argv) < 2:
        print 'Usage: python clean_furniture.py furniture'
    furniture_path = sys.argv[1]'''
    main()
