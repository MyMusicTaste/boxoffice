# -*- coding: utf-8 -*-

import MySQLdb
from items import BoxofficeItem
from DateParse import BoxDateParser
from BoxString import BoxString

import json


class BoxLocalDatabase:
    db = MySQLdb.connect('localhost', 'root', '1234', 'testdatabase')

    def drop_all_table(self):

        cursor = self.db.cursor()

        query_list = ["DROP TABLE IF EXISTS Event_Promoters;",
                      "DROP TABLE IF EXISTS Promoters;",
                      "DROP TABLE IF EXISTS Event_Prices;",
                      "DROP TABLE IF EXISTS Prices;",
                      "DROP TABLE IF EXISTS Dates;",
                      "DROP TABLE IF EXISTS Event;",
                      "DROP TABLE IF EXISTS Artist_Event;",
                      "DROP TABLE IF EXISTS Venue;",
                      "DROP TABLE IF EXISTS City;",
                      "DROP TABLE IF EXISTS Error_Log;"
                      ]

        for query in query_list:
            print(query)
            cursor.execute(query)

        self.db.commit()

    def create_tables(self):

        cursor = self.db.cursor()

        # query = "CREATE DATABASE IF NOT EXiSTS testdatabase;"
        # cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS  Error_Log( " \
                + "id INT NOT NULL AUTO_INCREMENT, " \
                + "table_name VARCHAR (256) , " \
                + "artist_event VARCHAR (512), " \
                + "city VARCHAR (256) ," \
                + "venue VARCHAR (256) ," \
                + "attend_capacity VARCHAR (256) ," \
                + "gross_sales VARCHAR (256) ," \
                + "show_sellout VARCHAR (256)," \
                + "rank VARCHAR (256)," \
                + "dates VARCHAR (512) ," \
                + "prices VARCHAR (256) ," \
                + "promoters VARCHAR (512) ," \
                + 'PRIMARY KEY (id)' \
                + '); '
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Artist_Event(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (512) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Venue(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS City(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "state VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS Event(" \
                + "id INT NOT NULL AUTO_INCREMENT ," \
                + "artist_event_id INT ," \
                + "city_id INT ," \
                + "venue_id INT ," \
                + "sale VARCHAR (256) ," \
                + "attend INT ," \
                + "capacity INT ," \
                + "shows INT ," \
                + "sellout INT ," \
                + "rank INT ," \
                + "dates VARCHAR (512) ," \
                + "PRIMARY KEY (id) ," \
                + "FOREIGN KEY (artist_event_id) REFERENCES Artist_Event (id) ," \
                + "FOREIGN KEY (city_id) REFERENCES City (id) ," \
                + "FOREIGN KEY (venue_id) REFERENCES Venue (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Promoters(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Event_Promoters(" \
                + "event_id int NOT NULL ," \
                + "promoter_id INT ," \
                + "PRIMARY KEY (event_id, promoter_id) ," \
                + "FOREIGN KEY (event_id) REFERENCES Event (id)," \
                + "FOREIGN KEY (promoter_id) REFERENCES Promoters (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Prices(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "price VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Event_Prices(" \
                + "event_id int NOT NULL ," \
                + "price_id INT ," \
                + "PRIMARY KEY (event_id, price_id) ," \
                + "FOREIGN KEY (event_id) REFERENCES Event (id) ," \
                + "FOREIGN KEY (price_id) REFERENCES Prices (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Dates(" \
                + "event_id int NOT NULL ," \
                + "year INT ," \
                + "month INT ," \
                + "date INT ," \
                + "PRIMARY KEY (event_id, year, month, date) ," \
                + "FOREIGN KEY (event_id) REFERENCES Event (id)" \
                + "); "
        cursor.execute(query)

        self.db.commit()

    # ----------------------------------------------------------------------------------------------------------------------
    def artist_event_insert_item(self, item):
        cursor = self.db.cursor()

        artist_event = item['artist_event']

        check_query = """SELECT COUNT(*) FROM Artist_Event WHERE name = "%s";""" % artist_event
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in Artist_Event" % artist_event
            else:
                query = """INSERT INTO Artist_Event (name) VALUES ("%s");""" % artist_event
                cursor.execute(query)
                self.db.commit()

    def venue_insert_item(self, item):
        cursor = self.db.cursor()
        venue = item['venue']

        check_query = """SELECT COUNT(*) FROM Venue WHERE name = "%s";""" % venue
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in Venue" % venue
            else:
                query = """INSERT INTO Venue (name) VALUES ("%s")""" % venue
                cursor.execute(query)
                self.db.commit()

    def city_insert_item(self, item):
        cursor = self.db.cursor()

        city_list = BoxString.normalize_city(item['city'])
        city = city_list[0]
        state = city_list[1]

        check_query = """SELECT COUNT(*) FROM City WHERE name = "%s" AND state = "%s";""" % (city, state)
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in City" % '%s-%s' % (city, state)
            else:
                query = """INSERT INTO City (name, state) VALUES ("%s", "%s");""" % (city, state)
                cursor.execute(query)
                self.db.commit()

    def promoters_insert_item(self, item):
        cursor = self.db.cursor()

        promoters_list = BoxString.normalize_promoters(item['promoters'])

        for promoter in promoters_list:

            check_query = """SELECT COUNT(*) FROM Promoters WHERE name = "%s";""" % promoter
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Promoters" % promoter
                else:
                    query = """INSERT INTO Promoters (name) VALUES ("%s");""" % promoter
                    cursor.execute(query)
                    self.db.commit()

    def prices_insert_item(self, item):
        cursor = self.db.cursor()

        prices_list = BoxString.normalize_prices(item['prices'])

        for price in prices_list:

            check_query = """SELECT COUNT(*) FROM Prices WHERE price = "%s";""" % price
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Prices" % price
                else:
                    query = """INSERT INTO Prices (price) VALUES ("%s");""" % price
                    cursor.execute(query)
                    self.db.commit()


    # ---------------------------------생각 좀 해보자 ---------------------------------------------------------------------
    def event_insert_item(self, item):
        cursor = self.db.cursor()

        rank = item['rank']
        artist_event = item['artist_event']
        venue = item['venue']

        try:
            city_list = BoxString.normalize_city(item['city'])
            city = city_list[0]
            state = city_list[1]

            date_list = item['date']

            gross_sales_list = BoxString.normalize_prices(item['gross_sales'])
            sale = gross_sales_list[0]

            attend_cap = BoxString.normalize_attend_capacity(item['attend_cap'])
            attend = attend_cap[0]
            capacity = attend_cap[1]

            shows_sellout_list = BoxString.normalize_shows_sellout(item['shows_sellout'])
            show = shows_sellout_list[0]
            sellout = shows_sellout_list[1]

            check_query = """SELECT COUNT(*)"""\
                          """FROM Artist_Event, City, Venue, Event """ \
                          """WHERE Artist_Event.name = "%s" AND Event.dates = "%s" """ \
                          """AND City.name = "%s" AND City.state = "%s" AND Venue.name = "%s";""" \
                          % (artist_event, date_list, city, state, venue)
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Event" % '%s / %s / %s / %s' % (artist_event, city, venue, date_list)
                else:
                    query = """INSERT INTO Event VALUES (""" \
                            """NULL, """ \
                            """(SELECT id FROM Artist_Event WHERE name = "%s"), """ \
                            """(SELECT id FROM City WHERE name = "%s" AND state = "%s"), """ \
                            """(SELECT id FROM Venue WHERE name = "%s"), "%s", %s, %s, %s, %s, %s, "%s");""" \
                            % (artist_event, city, state, venue, sale, attend, capacity, show, sellout, rank, date_list)
                    cursor.execute(query)
                    self.db.commit()

        except ValueError as e:
            self.create_error_log('Event', item)
        except Exception as e:
            print 'Error -------------------------------------------------------------------------'
            print e.args
            print item
            self.create_error_log('Event_Prices', item)

    def event_promoters_insert_item(self, item):
        cursor = self.db.cursor()

        try:
            artist_event = item['artist_event']
            venue = item['venue']
            city_list = BoxString.normalize_city(item['city'])
            city = city_list[0]
            state = city_list[1]
            date_list = item['date']
            promoters_list = BoxString.normalize_promoters(item['promoters'])

            for promoter in promoters_list:
                check_query = """SELECT COUNT(*) """ \
                              """FROM Event_Promoters """ \
                              """WHERE event_id = (SELECT Event.id """ \
                              """FROM Artist_Event, City, Venue, Event """ \
                              """WHERE Artist_Event.name = "%s" """ \
                              """AND Event.dates = "%s" """ \
                              """AND City.name = "%s" AND City.state = "%s" """ \
                              """AND Venue.name = "%s") """ \
                              """AND promoter_id = (SELECT id """ \
                              """FROM Promoters """ \
                              """WHERE name = "%s"); """ \
                              % (artist_event, date_list, city, state, venue, promoter)
                cursor.execute(check_query)
                for row in cursor:
                    if row[0] > 0:
                        print "%s exist in Event_Promoters" % '%s-%s' % (artist_event, promoter)
                    else:
                        query = """INSERT INTO Event_Promoters VALUES ( """ \
                                """(SELECT Event.id """ \
                                """FROM Artist_Event, City, Venue, Event """ \
                                """WHERE Artist_Event.name = "%s" """ \
                                """AND Event.dates = "%s" """ \
                                """AND City.name = "%s" AND City.state = "%s" """ \
                                """AND Venue.name = "%s"), """ \
                                """(SELECT id """ \
                                """FROM Promoters """ \
                                """WHERE name = "%s")); """ \
                                % (artist_event, date_list, city, state, venue, promoter)

                        cursor.execute(query)
                        self.db.commit()
        except ValueError as e:
            self.create_tables('Event_Promoters', item)
        except Exception as e:
            print 'Error -------------------------------------------------------------------------'
            print e.args
            print item
            self.create_error_log('Event_Prices', item)

    def event_prices_insert_item(self, item):
        cursor = self.db.cursor()

        try:
            artist_event = item['artist_event']
            venue = item['venue']
            city_list = BoxString.normalize_city(item['city'])
            city = city_list[0]
            state = city_list[1]
            date_list = item['date']

            prices_list = BoxString.normalize_prices(item['prices'])
            for price in prices_list:
                check_query = """SELECT COUNT(*) """ \
                              """FROM Event_Prices """ \
                              """WHERE event_id = (SELECT Event.id """ \
                              """FROM Artist_Event, City, Venue, Event """ \
                              """WHERE Artist_Event.name = "%s" """ \
                              """AND Event.dates = "%s" """ \
                              """AND City.name = "%s" AND City.state = "%s" """ \
                              """AND Venue.name = "%s") """ \
                              """AND price_id = (SELECT id """ \
                              """FROM Prices """ \
                              """WHERE price = "%s"); """ \
                              % (artist_event, date_list, city, state, venue, price)
                cursor.execute(check_query)
            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Event_Prices" % '%s-%s' % (artist_event, price)
                else:
                    query = """INSERT INTO Event_Prices VALUES (""" \
                            """(SELECT Event.id """ \
                            """FROM Artist_Event, City, Venue, Event """ \
                            """WHERE Artist_Event.name = "%s" """ \
                            """AND Event.dates = "%s" """ \
                            """AND City.name = "%s" AND City.state = "%s" """ \
                            """AND Venue.name = "%s"), """ \
                            """(SELECT id """ \
                            """FROM Prices """ \
                            """WHERE price = "%s")); """ \
                            % (artist_event, date_list, city, state, venue, price)

                    cursor.execute(query)
                    self.db.commit()
        except ValueError as e:
            self.create_error_log('Event_Prices', item)
        except Exception as e:
            print 'Error -------------------------------------------------------------------------'
            print e.args
            print item
            self.create_error_log('Event_Prices', item)

    def dates_insert_item(self, item):
        cursor = self.db.cursor()

        artist_event = item['artist_event']
        venue = item['venue']
        city_list = BoxString.normalize_city(item['city'])
        city = city_list[0]
        state = city_list[1]
        date_list = item['date']

        parser = BoxDateParser()
        array = parser.get_date_string(date_list)

        if array == None:
            self.create_error_log('Event', item)
        else:
            try:
                for dateObj in array:
                    for date in dateObj[2]:
                        check_query = """SELECT COUNT(*) """ \
                                      """FROM Dates """ \
                                      """WHERE event_id = (SELECT Event.id """ \
                                      """FROM Artist_Event, City, Venue, Event """ \
                                      """WHERE Artist_Event.name = "%s" """ \
                                      """AND Event.dates = "%s" """ \
                                      """AND City.name = "%s" AND City.state = "%s" """ \
                                      """AND Venue.name = "%s") """ \
                                      """AND year = %s AND month = %s AND date = %s; """ \
                                      % (artist_event, date_list, city, state, venue, dateObj[0], dateObj[1], date)
                        cursor.execute(check_query)
                        for row in cursor:
                            if row[0] > 0:
                                print "%s exist in Dates" % '%s-%s-%s' % (dateObj[0], dateObj[1], date)
                            else:
                                query = """INSERT INTO Dates VALUES (""" \
                                        """(SELECT Event.id """ \
                                        """FROM Artist_Event, City, Venue, Event """ \
                                        """WHERE Artist_Event.name = "%s" """ \
                                        """AND Event.dates = "%s" """ \
                                        """AND City.name = "%s" AND City.state = "%s" """ \
                                        """AND Venue.name = "%s"), %s, %s, %s); """ \
                                        % (artist_event, date_list, city, state, venue, dateObj[0], dateObj[1], date)

                                cursor.execute(query)
                                self.db.commit()
            except ValueError as e:
                self.create_error_log('Dates', item)
            except Exception as e:
                print 'Error -------------------------------------------------------------------------'
                print e.args
                print item
                self.create_error_log('Event_Prices', item)

    def insert_item(self, item):
        self.artist_event_insert_item(item)
        self.city_insert_item(item)
        self.venue_insert_item(item)
        self.promoters_insert_item(item)
        self.prices_insert_item(item)
        self.event_insert_item(item)
        self.event_promoters_insert_item(item)
        self.event_prices_insert_item(item)
        self.dates_insert_item(item)

    def create_error_log(self, table, item):

        cursor = self.db.cursor()

        city = item['city']
        dates = item['date']
        shows_sellout = item['shows_sellout']
        promoters = item['promoters']
        attend_cap = item['attend_cap']
        venue = item['venue']
        rank = item['rank']
        artist_event = item['artist_event']
        prices = item['prices']
        gross_sales = item['gross_sales']



        # query = "CREATE TABLE IF NOT EXISTS  Error_Log( " \
        #         + "id INT NOT NULL AUTO_INCREMENT, " \
        #         + "table_name VARCHAR (256) , " \
        #         + "artist_event VARCHAR (256), " \
        #         + "city VARCHAR (256) ," \
        #         + "venue VARCHAR (256) ," \
        #         + "attend_capacity VARCHAR (256) ," \
        #         + "gross_sales VARCHAR (256) ," \
        #         + "show_sellout VARCHAR (256)," \
        #         + "rank VARCHAR (256)," \
        #         + "dates VARCHAR (512) ," \
        #         + "prices VARCHAR (256) ," \
        #         + "promoters VARCHAR (512) ," \
        #         + 'PRIMARY KEY (id)' \
        #         + '); '

        try:
            query = """INSERT INTO Error_Log VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" \
                    % (table, artist_event, city, venue, attend_cap, gross_sales, shows_sellout, rank, dates, prices,
                       promoters)
            cursor.execute(query)
            self.db.commit()
        except ValueError as e:
            print e


# test = BoxLocalDatabase()
# test.drop_all_table()

# test.insert_item(item)

# with open("test.json") as json_file:
#     json_data = json.load(json_file)
#
#     test_list = json_data
#     for string in test_list:
#         test.insert_item(string)

# test.create_tables()
