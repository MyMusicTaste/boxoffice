# -*- coding: utf-8 -*-

import MySQLdb
# from items import BoxofficeItem

from DateParse import BoxDateParser
from BoxString import BoxString

import datetime
from time import strftime

import json


class BoxLocalDatabase:
    # db = MySQLdb.connect('localhost', 'boxoffice', 'mmtboxoffice1234', 'boxoffice_database')
    db = MySQLdb.connect('localhost', 'root', '1234', 'boxoffice_database')

    def drop_all_table(self):

        cursor = self.db.cursor()

        query_list = ["DROP TABLE IF EXISTS boxoffice_app_EventPromoters;",
                      "DROP TABLE IF EXISTS boxoffice_app_Promoter;",
                      "DROP TABLE IF EXISTS boxoffice_app_EventPrice;",
                      "DROP TABLE IF EXISTS boxoffice_app_Price;",
                      "DROP TABLE IF EXISTS boxoffice_app_Date;",
                      "DROP TABLE IF EXISTS boxoffice_app_Event;",
                      "DROP TABLE IF EXISTS boxoffice_app_ArtistEvent;",
                      "DROP TABLE IF EXISTS boxoffice_app_Venue;",
                      "DROP TABLE IF EXISTS boxoffice_app_City;",
                      "DROP TABLE IF EXISTS boxoffice_app_ErrorLog;"
                      ]

        for query in query_list:
            print(query)
            cursor.execute(query)

        self.db.commit()

    def create_tables(self):

        cursor = self.db.cursor()

        # query = "CREATE DATABASE IF NOT EXiSTS testdatabase;"
        # cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS boxoffice_app_UpdateLog( " \
                + "id INT NOT NULL AUTO_INCREMENT, " \
                + "last_update varchar (128), " \
                + 'PRIMARY KEY (id)' \
                + '); '
        cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS  boxoffice_app_ErrorLog( " \
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
                + "create_date VARCHAR (128), " \
                + 'PRIMARY KEY (id)' \
                + '); '
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_ArtistEvent(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (512) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_Venue(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_City(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "state VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS boxoffice_app_Event(" \
                + "id INT NOT NULL AUTO_INCREMENT ," \
                + "artist_event_id INT ," \
                + "city_id INT ," \
                + "venue_id INT ," \
                + "sale DOUBLE ," \
                + "attend INT ," \
                + "capacity INT ," \
                + "shows INT ," \
                + "sellout INT ," \
                + "rank INT ," \
                + "dates VARCHAR (512) ," \
                + "create_date VARCHAR (128), " \
                + "PRIMARY KEY (id) ," \
                + "FOREIGN KEY (artist_event_id) REFERENCES boxoffice_app_ArtistEvent (id) ," \
                + "FOREIGN KEY (city_id) REFERENCES boxoffice_app_City (id) ," \
                + "FOREIGN KEY (venue_id) REFERENCES boxoffice_app_Venue (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_Promoter(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "name VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_EventPromoter(" \
                + "id INT NOT NULL AUTO_INCREMENT, " \
                + "event_id int NOT NULL ," \
                + "promoter_id INT ," \
                + "PRIMARY KEY (id)," \
                + "FOREIGN KEY (event_id) REFERENCES boxoffice_app_Event (id)," \
                + "FOREIGN KEY (promoter_id) REFERENCES boxoffice_app_Promoter (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_Price(" \
                + "id int NOT NULL AUTO_INCREMENT," \
                + "price VARCHAR (256) ," \
                + "PRIMARY KEY (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_EventPrice(" \
                + "id INT NOT NULL AUTO_INCREMENT, " \
                + "event_id int NOT NULL ," \
                + "price_id INT ," \
                + "PRIMARY KEY (id)," \
                + "FOREIGN KEY (event_id) REFERENCES boxoffice_app_Event (id) ," \
                + "FOREIGN KEY (price_id) REFERENCES boxoffice_app_Price (id)" \
                + "); "
        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS boxoffice_app_Date(" \
                + "id INT NOT NULL AUTO_INCREMENT, " \
                + "event_id int NOT NULL ," \
                + "event_date DATETIME ," \
                + "PRIMARY KEY (id)," \
                + "FOREIGN KEY (event_id) REFERENCES boxoffice_app_Event (id)" \
                + "); "
        cursor.execute(query)

        self.db.commit()

    # ----------------------------------------------------------------------------------------------------------------------
    def artist_event_insert_item(self, item):
        cursor = self.db.cursor()

        artist_event = item['artist_event']

        check_query = """SELECT COUNT(*) FROM boxoffice_app_artistevent WHERE name = "%s";""" % artist_event
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in Artist_Event" % artist_event
            else:
                query = """INSERT INTO boxoffice_app_artistevent (name) VALUES ("%s");""" % artist_event
                cursor.execute(query)
                self.db.commit()

    def venue_insert_item(self, item):
        cursor = self.db.cursor()
        venue = item['venue']

        check_query = """SELECT COUNT(*) FROM boxoffice_app_venue WHERE name = "%s";""" % venue
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in Venue" % venue
            else:
                query = """INSERT INTO boxoffice_app_venue (name) VALUES ("%s")""" % venue
                cursor.execute(query)
                self.db.commit()

    def city_insert_item(self, item):
        cursor = self.db.cursor()

        city_list = BoxString.normalize_city(item['city'])
        city = city_list[0]
        state = city_list[1]

        check_query = """SELECT COUNT(*) FROM boxoffice_app_city WHERE name = "%s" AND state = "%s";""" % (city, state)
        cursor.execute(check_query)

        for row in cursor:
            if row[0] > 0:
                print "%s exist in City" % '%s-%s' % (city, state)
            else:
                query = """INSERT INTO boxoffice_app_city (name, state) VALUES ("%s", "%s");""" % (city, state)
                cursor.execute(query)
                self.db.commit()

    def promoters_insert_item(self, item):
        cursor = self.db.cursor()

        promoters_list = BoxString.normalize_promoters(item['promoters'])

        for promoter in promoters_list:

            check_query = """SELECT COUNT(*) FROM boxoffice_app_promoter WHERE name = "%s";""" % promoter
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Promoters" % promoter
                else:
                    query = """INSERT INTO boxoffice_app_promoter (name) VALUES ("%s");""" % promoter
                    cursor.execute(query)
                    self.db.commit()

    def prices_insert_item(self, item):
        cursor = self.db.cursor()

        prices_list = BoxString.normalize_prices(item['prices'])

        for price in prices_list:

            check_query = """SELECT COUNT(*) FROM boxoffice_app_price WHERE price = "%s";""" % price
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Prices" % price
                else:
                    query = """INSERT INTO boxoffice_app_price (price) VALUES ("%s");""" % price
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

            update_date = item["create_date"]

            check_query = """SELECT COUNT(*) """\
                          """FROM boxoffice_app_event """ \
                          """WHERE id = (SELECT boxoffice_app_event.id """ \
                          """FROM boxoffice_app_event """ \
                          """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                          """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                          """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                          """AND dates = "%s" ) """ \
                          % (artist_event, venue, city, state, date_list)
            cursor.execute(check_query)

            for row in cursor:
                if row[0] > 0:
                    print "%s exist in Event" % '%s / %s / %s / %s' % (artist_event, city, venue, date_list)
                else:
                    query = """INSERT INTO boxoffice_app_event VALUES (""" \
                            """NULL, """ \
                            """(SELECT id FROM boxoffice_app_artistevent WHERE name = "%s"), """ \
                            """(SELECT id FROM boxoffice_app_city WHERE name = "%s" AND state = "%s"), """ \
                            """(SELECT id FROM boxoffice_app_venue WHERE name = "%s"), "%s", %s, %s, %s, %s, %s, "%s", "%s");""" \
                            % (artist_event, city, state, venue, sale, attend, capacity, show, sellout, rank, date_list, update_date)
                    cursor.execute(query)
                    self.db.commit()

        except ValueError as e:
            self.create_error_log('Event', item)
        except Exception as e:
            print 'Error ----------------------%s--------------------------------------------------' % 'Event'
            print e.args
            print item
            self.create_error_log('Event', item)
            raise Exception("Event Insert Error")

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
            update_date = item["create_date"]

            for promoter in promoters_list:
                check_query = """SELECT COUNT(*) """ \
                              """FROM boxoffice_app_eventpromoter """ \
                              """WHERE event_id = (SELECT boxoffice_app_event.id """ \
                              """FROM boxoffice_app_event """ \
                              """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                              """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                              """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                              """AND dates = "%s" ) """ \
                              """AND promoter_id = (SELECT id """ \
                              """FROM boxoffice_app_promoter """ \
                              """WHERE name = "%s"); """ \
                              % (artist_event, venue, city, state, date_list, promoter)
                cursor.execute(check_query)
                for row in cursor:
                    if row[0] > 0:
                        print "%s exist in Event_Promoters" % '%s-%s' % (artist_event, promoter)
                    else:
                        query = """INSERT INTO boxoffice_app_eventpromoter VALUES (NULL, """ \
                                """(SELECT boxoffice_app_event.id """ \
                                """FROM boxoffice_app_event """ \
                                """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                                """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                                """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                                """AND dates = "%s" ), """ \
                                """(SELECT id """ \
                                """FROM boxoffice_app_promoter """ \
                                """WHERE name = "%s")); """ \
                                % (artist_event, venue, city, state, date_list, promoter)

                        cursor.execute(query)
                        self.db.commit()
        except ValueError as e:
            self.create_tables('Event_Promoters', item)
        except Exception as e:
            print 'Error ----------------------%s--------------------------------------------------' % 'Event_Promoters'
            print e.args
            print item
            self.create_error_log('Event_Promoters', item)

    def event_prices_insert_item(self, item):
        cursor = self.db.cursor()

        try:
            artist_event = item['artist_event']
            venue = item['venue']
            city_list = BoxString.normalize_city(item['city'])
            city = city_list[0]
            state = city_list[1]
            date_list = item['date']
            update_date = item["create_date"]

            prices_list = BoxString.normalize_prices(item['prices'])
            for price in prices_list:
                check_query = """SELECT COUNT(*) """ \
                              """FROM boxoffice_app_eventprice """ \
                              """WHERE event_id = (SELECT boxoffice_app_event.id """ \
                              """FROM boxoffice_app_event """ \
                              """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                              """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                              """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                              """AND dates = "%s" ) """ \
                              """AND price_id = (SELECT id """ \
                              """FROM boxoffice_app_price """ \
                              """WHERE price = "%s"); """ \
                              % (artist_event, venue, city, state, date_list, price)
                cursor.execute(check_query)
                for row in cursor:
                    if row[0] > 0:
                        print "%s exist in Event_Prices" % '%s-%s' % (artist_event, price)
                    else:
                        query = """INSERT INTO boxoffice_app_eventprice VALUES (NULL, """ \
                                """(SELECT boxoffice_app_event.id """ \
                                """FROM boxoffice_app_event """ \
                                """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                                """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                                """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                                """AND dates = "%s" ), """ \
                                """(SELECT id """ \
                                """FROM boxoffice_app_price """ \
                                """WHERE price = "%s")); """ \
                                % (artist_event, venue, city, state, date_list, price)

                        cursor.execute(query)
                        self.db.commit()
        except ValueError as e:
            self.create_error_log('Event_Prices', item)
        except Exception as e:
            print 'Error ----------------------%s--------------------------------------------------' % 'Event_Prices'
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
        update_date = item['create_date']

        parser = BoxDateParser()
        array = parser.get_date_string(date_list)

        if array == None:
            self.create_error_log('Date', item)
        else:
            try:
                for dateObj in array:
                    for date in dateObj[2]:
                        check_query = """SELECT COUNT(*) """ \
                                      """FROM boxoffice_app_date """ \
                                      """WHERE event_id = (SELECT boxoffice_app_event.id """ \
                                      """FROM boxoffice_app_event """ \
                                      """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                                      """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                                      """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                                      """AND dates = "%s" ) """ \
                                      """AND event_date = "%s-%s-%s"; """ \
                                      % (artist_event, venue, city, state, date_list, dateObj[0], dateObj[1], date)
                        cursor.execute(check_query)
                        for row in cursor:
                            if row[0] > 0:
                                print "%s exist in Dates" % '%s-%s-%s' % (dateObj[0], dateObj[1], date)
                            else:
                                query = """INSERT INTO boxoffice_app_date VALUES (NULL, """ \
                                        """(SELECT boxoffice_app_event.id """ \
                                        """FROM boxoffice_app_event """ \
                                        """WHERE artist_event_id=(SELECT id FROM boxoffice_app_artistevent where name = "%s") """ \
                                        """AND venue_id=(SELECT id FROM boxoffice_app_venue where name = "%s") """ \
                                        """AND city_id=(SELECT id FROM boxoffice_app_city where name = "%s" AND state = "%s") """ \
                                        """AND dates = "%s" ), "%s-%s-%s"); """ \
                                        % (artist_event, venue, city, state, date_list, dateObj[0], dateObj[1], date)

                                cursor.execute(query)
                                self.db.commit()
            except ValueError as e:
                self.create_error_log('Date', item)
            except Exception as e:
                print 'Error ----------------------%s--------------------------------------------------' % 'Date'
                print e.args
                print item
                self.create_error_log('Date', item)

    def update_updatelog(self, item):
        cursor = self.db.cursor()

        update_date = item["create_date"]

        query = "SELECT COUNT(*) FROM boxoffice_app_updatelog"
        cursor.execute(query)
        for row in cursor:
            if row[0] > 0:
                query = "UPDATE boxoffice_app_updatelog SET last_update = '%s' WHERE id = 1" % update_date
                cursor.execute(query)
            else:
                query = "INSERT INTO boxoffice_app_updatelog VALUES (NULL, '%s')" % update_date
                cursor.execute(query)
                self.db.commit()



    def insert_item(self, item):

        self.update_updatelog(item)

        self.artist_event_insert_item(item)
        self.city_insert_item(item)
        self.venue_insert_item(item)
        self.promoters_insert_item(item)
        self.prices_insert_item(item)

        try:
            self.event_insert_item(item)
            self.event_promoters_insert_item(item)
            self.event_prices_insert_item(item)
            self.dates_insert_item(item)
        except Exception as e:
            print(e.args)

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
        create_date = item['create_date']


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
            query = """INSERT INTO boxoffice_app_errorlog VALUES (NULL, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" \
                    % (table, artist_event, city, venue, attend_cap, gross_sales, shows_sellout, rank, dates, prices,
                       promoters, create_date)
            cursor.execute(query)
            self.db.commit()
        except ValueError as e:
            print e


# test = BoxLocalDatabase()
#
# with open("test.json") as json_file:
#     json_data = json.load(json_file)
#
#     test_list = json_data
#     for string in test_list:
#         print(string)
#         string['create_date'] = "2015-12-14 17:41"
#         test.insert_item(string)
