# -*- coding: utf-8 -*-
import calendar

class BoxDateParser:

    month_string_list = [
        ['Jan.', 'January', 1],
        ['Feb.', 'February', 2],
        ['Mar.', 'February', 3],
        ['Apr.', 'April', 4],
        ['May.', 'May', 5],
        ['Jun.', 'June', 6],
        ['Jul.', 'July', 7],
        ['Aug.', 'August', 8],
        ['Sept.', 'September', 9],
        ['Oct.', 'October', 10],
        ['Nov.', 'November', 11],
        ['Dec.', 'December', 12]
    ]

    # 문자열을 나눠 리스트로 만든다.
    def get_date_list(self, date_string):

        date_string = date_string.replace("/", " , ")
        date_string = date_string.replace(",", "")
        date_string = date_string.split()

        dates_list = list()
        for index, element in enumerate(date_string):

            if element.find('-') >= 0:
                element = element.split('-')
                templist = list()

                date = int(element[0])

                if self.check_is_number(element[1]):
                    while date <= int(element[1]):
                        templist.append(str(date))
                        date += 1
                    dates_list += templist
                else:
                    # 다른달과 이어짐. Nov. 30 - Dec. 2
                    templist.append(element[0])
                    templist.append('-')
                    templist.append(element[1])
                    dates_list += templist
                    # raise ValueError("get_date_list - split error ( '-' ) ")

            else:
                element = element.split('-')
                dates_list += element

        return dates_list

    # 숫자로만 구성되어 있으면 True = 1, False = 0
    def check_is_number(self, param_string):
        for character in param_string:
            # ascii 48 = 0, ascii 57 = 9
            if ord(character) < 48 or ord(character) > 57:
                return 0
        return 1

    # 문자열이 년도가 맞는지 확인 True = 1, False = 0
    def check_is_year(self, param_string):

        if len(param_string) >= 4:
            for character in param_string:
                # ascii 48 = 0, ascii 57 = 9
                if ord(character) < 48 or ord(character) > 57:
                    return 0
            return 1
        return 0

    # 년도로 구분한 리스트를 만들어 리턴
    def get_year_list(self, param_list):

        year_list = list()

        index = 0
        for year_string in param_list:
            if self.check_is_year(year_string):
                last_index = param_list.index(year_string) + 1
                year = param_list[index:last_index]

                year_list.append(year)
                index = last_index

        return year_list

    # 달로 구분한 리스트를 만들어 리턴
    def get_month_list(self, param_list):

        original_list = param_list

        param_list = param_list[0:-1]

        month_index_array = list()
        month_list = list()

        for index,  string in enumerate(param_list):
            for month_string in self.month_string_list:
                if string == month_string[0] or string == month_string[1]:
                    param_list[index] = month_string[2]
                    month_index_array.append(index)

        index = 0
        while True:
            if index == len(month_index_array)-1:
                month_list.append(param_list[month_index_array[index]:])
                break;

            month_list.append(param_list[month_index_array[index]:month_index_array[index + 1]])
            index += 1



        for list_index, month in enumerate(month_list):
            for index, string in enumerate(month):
                if string == '-' and index == len(month)-1:

                    range_tuple = calendar.monthrange(int(original_list[-1]), int(month[0]))

                    last_date = range_tuple[1]
                    start_date = int(month[index-1])

                    while True:
                        if int(start_date) >= int(last_date):
                            break
                        else:
                            start_date += 1
                            month.append(str(start_date))
                    del month[index]

                    if list_index < len(month_list)-1:
                        new_month = month_list[list_index + 1]
                        last_date = new_month[1]

                        start_date = 0

                        new_list = list()
                        while True:
                            if int(start_date) >= int(last_date)-1:
                                break
                            else:
                                start_date += 1
                                new_month.append(str(start_date))
                        # new_month



        return month_list

    # 받은 문자열로 [년도, 달, 날짜들]로 구성된 리스트 만들어 리턴
    def get_date_string(self, string):
        try:
            proc_event_date = self.get_date_list(string)

            processed_list = list()

            for array in self.get_year_list(proc_event_date):
            # last index value is year

            # self.get_month_list(array[0:-1])
            # print(self.get_month_list(array[0:-1]))
                month_list = self.get_month_list(array)

                for date_list in month_list:
                    new_dates = date_list[1:]
                    new_dates.sort()
                    processed_list.append([array[-1], date_list[0], new_dates])

            return processed_list
        except ValueError as e:
            print('Error : %s' % e.args)
            return None

# test = BoxDateParser()
# print test.get_date_string('Nov. 14-18, 2015 / Oct. 24-25, Aug. 2 2016, Jan. 25, 2017')
# # print test.get_date_string('Nov. 14-Feb. 2, 2015 / Oct. 24-25, Aug. 2 2016, Jan. 25, 2017')
# # print test.get_date_string('Oct. 11, 16, Nov. 23, 25-Dec. 28, 2015, Jan. 2, Oct. 8, 2016')
#
# test2 = test.get_date_string('Oct. 29-Nov. 1, 25-Dec. 5, 2016')
# print test2