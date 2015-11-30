# -*- coding: utf-8 -*-

class BoxString:

    @staticmethod
    def normalize_attend_capacity(string):
        # string = str(string)

        string = string.encode('ascii','ignore')
        string = string.replace(' ', '')
        string = string.replace(',', '')
        return_list = string.split('/')

        for index, value in enumerate(return_list):
            if len(value) == 0:
                return_list[index] = 0

        return return_list

    @staticmethod
    def normalize_shows_sellout(string):
        string = string.encode('ascii','ignore')

        string = string.replace(' ', '')
        string = string.replace(',', '')
        return_list = string.split('/')

        for index, value in enumerate(return_list):
            if len(value) == 0:
                return_list[index] = 0

        return return_list

    @staticmethod
    def normalize_prices(string):
        string = str(string)

        index_list = list()

        for index, char in enumerate(string):
            if char == '$':
                index_list.append(index)

        price_list = list()

        index = 0
        while True:
            if index == len(index_list)-1:
                price_list.append(string[index_list[index]:])
                break;

            price_list.append(string[index_list[index]:index_list[index + 1]])
            index += 1

        for place, value in enumerate(price_list):
            value = value.replace(' ', '')
            value = value.replace(',', '')
            value = value.replace('$', '')
            price_list[place] = value

        return price_list

    @staticmethod
    def normalize_promoters(string):
        string = str(string)
        return_list = string.split('/')
        return return_list

    @staticmethod
    def normalize_city(string):
        string = str(string)
        return_list = string.split(',')
        return return_list

    @staticmethod
    def normalize_venue(string):
        string = string.replace('/', ' ')
        return string
