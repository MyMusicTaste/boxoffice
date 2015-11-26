# -*- coding: utf-8 -*-


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
        for element in date_string:
            element = element.split('-')
            dates_list += element

        # ex ['Jan.', '2', '3', '2015']
        return dates_list

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

        month_index_array = list()
        month_list = list()

        index = 0
        for string in param_list:
            for month_string in self.month_string_list:
                if string == month_string[0] or string == month_string[1]:
                    param_list[index] = month_string[2]
                    month_index_array.append(index)
            index += 1

        index = 0
        while True:

            if index == len(month_index_array)-1:
                month_list.append(param_list[month_index_array[index]:])
                break;

            month_list.append(param_list[month_index_array[index]:month_index_array[index + 1]])
            index += 1

        return month_list

    # 받은 문자열로 [년도, 달, 날짜들]로 구성된 리스트 만들어 리턴
    def get_date_string(self, string):
        proc_event_date = self.get_date_list(string)

        processed_list = list()

        for array in self.get_year_list(proc_event_date):
            # last index value is year

            self.get_month_list(array[0:-1])
            # print(get_month_list(array[0:-1]))
            month_list = self.get_month_list(array[0:-1])

            for date_list in month_list:
                processed_list.append([array[-1], date_list[0], date_list[1:]])

        return processed_list

# test = BoxDateParser()
# print test.get_date_string('Nov. 14, Feb. 25 2015 / Oct. 24-25, Aug. 2 2016, Jan. 25, 2017')

