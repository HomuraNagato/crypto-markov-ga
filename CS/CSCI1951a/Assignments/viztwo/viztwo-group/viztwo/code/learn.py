from __future__ import division
import sys
import csv
import json
import argparse
from collections import defaultdict

import util

import math

import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import cross_validation
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC


def load_json(file_path):
  json_data = []
  # Open json file
  with open(file_path, 'r') as f:
    for line in f:
      j = (json.loads(line))
      json_data += j['data']
  return json_data


def group_by_feature(data, key, remove_list):
	obj_grouped = {}
	for obj in data:
		if obj[key]:
			if obj[key] not in obj_grouped:
				obj_grouped[obj[key]] = []
			obj_grouped[obj[key]].append(obj)
			for rem in remove_list:
				del obj[rem]
		
	return obj_grouped


def extract_features(data, key):	
	obj_labels = []
	obj_features = []
	for user in data:
		obj_labels.append(0)
		features = []
		for obj in data[user]:
			for feature in obj:
				feat = obj[feature]
				if (feature == key and feat):
						obj_labels[-1] = feat
						continue
				if type(feat) is float or type(feat) is int:
					continue
				if type(feat) is dict:
					for subfeature in feat:
						subfeat = feat[subfeature]
						if type(subfeat) is float or type(feat) is int:
							continue
						features.append(subfeat)
				else:
						features.append(feat)
		obj_features.append(" ".join(features))
	return (obj_labels, obj_features)


def print_json_file(filename, data):
	with open(filename, 'w') as f:
  		json.dump(users, f)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', default="log", type=str, help='classifier to use')
	parser.add_argument('-field', type=str, default="device", help='Variable to use as label')
	parser.add_argument('-top', type=int, default="10", help='Number of top features to show')
	parser.add_argument('-p', type=bool, default='False', help='If true, prints out information')
	opts = parser.parse_args()

	# Extract data from file
	data = load_json('../data/data.json')

	# Group events by session_id and remove location
	users = group_by_feature(data, "session_id", ["session_id", "location"])

	# Get training labels and data
	training_labels, training_features = extract_features(users, opts.field)


	vectorizer = CountVectorizer(decode_error='replace')

	training_features = vectorizer.fit_transform(training_features)
	training_labels = numpy.array(training_labels)

	cf = opts.c

	if cf == 'nb':
		# Initialize Naive Bayes and train
		classifier = BernoulliNB(binarize=None)
		classifier.fit(training_features, training_labels)

	elif cf == 'log':
		# Initialize Logistic Regression and train
		classifier = LogisticRegression()
		classifier.fit(training_features, training_labels)

	elif cf == 'svm':
		# Initialize SVM and train
		classifier = LinearSVC()
		classifier.fit(training_features, training_labels)
	else:
		raise Exception('Unrecognized classifier!')

	print "Made classifier!"

	on_own_set_score = classifier.score(training_features, training_labels)

	print "Scored!"

	# Perform 10 fold cross validation (cross_validation.cross_val_score) with scoring='accuracy'
	scores = cross_validation.cross_val_score(classifier, training_features, training_labels, cv=10)

	print "Cross validated!"

	if opts.p:
		print "Top Features:"
		num_top = 10
		if opts.top:
			num_top = opts.top
		print util.print_most_informative_features(cf,vectorizer,classifier,num_top)
		print("Mean %0.2f , StdDev %0.2f" % (scores.mean(), scores.std()))

	print "All done!"



if __name__ == '__main__':
	main()
