#!/usr/bin/env python
import sys
import json
import porter_stemmer

pinterest_path = ''
furniture_names_path = ''
stopwords_path = ''

def main():
    with open(pinterest_path) as json_pins:
        pins = json.loads(json_pins.read())
        furniture_popularity(pins)
        website_popularity(pins)
        sentiment_analysis(pins)

def furniture_popularity(pins):
    '''
    Input:
        pins : JSON object of Pinterest pins
    '''
    # Find which pieces of furniture occur the most
    with open(furniture_names_path) as f:
        # List of all names of furniture
        names = list(f.read().splitlines())

def website_popularity(pins):
    '''
    Input:
        pins : JSON object of Pinterest pins
    '''
    # TODO: calculate popularity for websites
    pass

def sentiment_analysis(pins):
    '''
    Input:
        pins : JSON object of Pinterest pins
    '''
    # First, match pins with pieces of furniture
    with open(furniture_names_path) as f:
        # List of all names of furniture
        names = list(f.read().splitlines())

    # Then, for each pin remove common words
    with open(stopwords_path) as stopwords:
        # TODO
        stops = list(stopwords.read().splitlines())

    # Next, apply the Porter stemming algorithm
    stemmer = porter_stemmer.PorterStemmer()

    # Finally, calculate sentiment for each piece of furniture

    # Print the five most positive along with their sentiment
    # Print the five most negative along with their sentiment
    # See assignment for format

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'Usage: python process.py pinterest furniture_names stopwords'
    pinterest_path = sys.argv[1]
    furniture_names_path = sys.argv[2]
    stopwords_path = sys.argv[3]
    main()
