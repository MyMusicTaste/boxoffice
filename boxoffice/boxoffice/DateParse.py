# Nov. 3-4, 7-8, 10-11, 13-14, 17-18, 20-21, 2015

def get_date_array(date_string):
    date_string = date_string.replace(",", "")
    date_string = date_string.split()

    dates_list = list()
    for element in date_string:
        element = element.split('-')
        dates_list += element
    # print dateslist
    return dates_list

string = ["Nov. 3-4, 7-8, 10-11, Nov. 13-14, 17-18, 20-21, 25, 2015",
          "Sept. 25-26, 2015",
          "Oct. 31-Nov. 1, 2015",
          "Nov. 19, 2015"
          ]

for str in string:
    testlist = get_date_array(str)
    print testlist