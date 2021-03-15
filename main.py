import csv
import logging
import os

import csv_editor


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

class Robot(object):
    def __init__(self, robot_name, user_name=None, favorite_resutaurant=None):
        self.robot_name = robot_name
        self.user_name = user_name
        self.favorite_restaurant = favorite_resutaurant

    def who_are_you(self):
        print('こんにちは！私は{}です。あなたの名前は何ですか？'.format(self.robot_name))
        self.user_name = input()
        logger.debug('log:{}'.format(self.user_name))

    def ask_favorite_restaurant(self):
        print('{}さん。どこのレストランが好きですか?'.format(self.user_name))
        self.favorite_restaurant = input()
        self.favorite_restaurant = self.favorite_restaurant.capitalize()
        logger.debug('log:{}'.format(self.favorite_restaurant))

    def add_file(self):
        if os.path.isfile('Restaurant.csv'):
            logger.debug('Restaurant.csv is exist')
            with open('Restaurant.csv', 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                now_files = {}
                for row in reader:
                    now_files.update({row['NAME'] : row['COUNT']})
                if self.favorite_restaurant not in now_files:
                    now_files.update({self.favorite_restaurant: 1})
                else:
                    now_files[self.favorite_restaurant] = (int(now_files[self.favorite_restaurant]) + 1)
            csv_editor.add_csvfile(now_files)
        else:
            logger.debug('Restaurant.csv is not exist')
            with open('Restaurant.csv', 'w') as csv_file:
                fieldnames = ['NAME', 'COUNT']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                now_files = {}
                now_files.update({self.favorite_restaurant: 1})
            csv_editor.add_csvfile(now_files)

    def recommend(self):
        now_files = csv_editor.read_csvfile()
        files_sorted = sorted(now_files.items(), key=lambda x:x[1], reverse=True)
        restaurant = ''
        print(files_sorted)
        for k,v in files_sorted:
            while restaurant != 'YES' and restaurant != 'NO':
                print("私のオススメのレストランは{}です。\nこのレストランは好きですか？[yes/no]".format(k))
                restaurant = input().upper()
            if restaurant == 'YES':
                break
            else:
                restaurant = ''

    def say_goodbye(self):
        print('{}さん。ありがとうございました。\n良い1日を！さようなら。'.format(self.user_name))


if __name__ == '__main__':
    roboko = Robot('Roboko')
    roboko.who_are_you()
    if os.path.isfile('Restaurant.csv'):
        print('aaa')
        roboko.recommend()
    roboko.ask_favorite_restaurant()
    roboko.add_file()
    roboko.say_goodbye()