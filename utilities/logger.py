import json
import csv
import logging


class Logger:

    def message(self, data):
        logging.debug(data)

    def error(self, data):
        logging.debug(data)

    def save_to_csv(self, data):
        with open('message.csv', 'w') as csvfile:
            fieldnames = ['word', 'count']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for word, count in data:
                writer.writerow([word, count])

    def save_to_json(self, data):
        data = {word: count for word, count in data }
        with open('message.json', 'w') as jsonfile:
            json.dump(data, jsonfile)