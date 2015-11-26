import MySQLdb
from items import BoxofficeItem

class BoxLocalDatabase:


    db = MySQLdb.connect('localhost', 'root', '', 'testdatabase')

    def __int__(self):
        self.create_tables()

    def drop_table(self, table_name):
        cursor = self.db.cursor()

        query = "DROP TABLE %s;" % table_name
        cursor.execute(query)

        self.db.commit()
        self.db.close()

    def drop_all_table(self):

        cursor = self.db.cursor()

        query = "DROP TABLE Artist_Event; " \
                "DROP TABLE Venue;" \
                "DROP TABLE City;" \
                "DROP TABLE Event;" \
                "DROP TABLE Promoters;" \
                "DROP TABLE Event_Promoters;" \
                "DROP TABLE Prices;" \
                "DROP TABLE Event_Prices;" \
                "DROP TABLE Dates;" \

        cursor.execute(query)

        self.db.commit()
        self.db.close()


    def create_tables(self):

        cursor = self.db.cursor()

        # query = "CREATE DATABASE IF NOT EXiSTS testdatabase;"
        # cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Artist_Event("\
                + "id int NOT NULL AUTO_INCREMENT,"\
                + "name VARCHAR (512) ,"\
                + "PRIMARY KEY (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Venue("\
                + "id int NOT NULL AUTO_INCREMENT,"\
                + "name VARCHAR (256) ,"\
                + "PRIMARY KEY (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS City("\
                + "id int NOT NULL AUTO_INCREMENT,"\
                + "name VARCHAR (256) ,"\
                + "state VARCHAR (256)),"\
                + "PRIMARY KEY (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Promoters("\
                + "id int NOT NULL AUTO_INCREMENT,"\
                + "name VARCHAR (256) ,"\
                + "PRIMARY KEY (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE IF NOT EXISTS Event("\
                + "id INT NOT NULL AUTO_INCREMENT ," \
                + "artist_event_id INT ," \
                + "city_id INT ,"\
                + "venue_id INT ,"\
                + "sale INT ,"\
                + "attend INT ,"\
                + "capacity INT ,"\
                + "gross_show INT ,"\
                + "sellout INT ,"\
                + "rank INT ,"\
                + "PRIMARY KEY (id) ,"\
                + "FOREIGN KEY (artist_event_id) REFERENCES Artist_Event (id) ,"\
                + "FOREIGN KEY (city_id) REFERENCES City (id) ,"\
                + "FOREIGN KEY (venue_id) REFERENCES Venue (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Event_Promoters("\
                + "event_id int NOT NULL ,"\
                + "promoter_id INT ,"\
                + "PRIMARY KEY (event_id, promoter_id) ,"\
                + "FOREIGN KEY (event_id) REFERENCES Event (id) ,"\
                + "FOREIGN KEY (promoter_id) REFERENCES Promoters (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Prices("\
                + "id int NOT NULL AUTO_INCREMENT,"\
                + "price INT ,"\
                + "PRIMARY KEY (id)"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Event_Prices("\
                + "event_id int NOT NULL ,"\
                + "price_id INT ,"\
                + "PRIMARY KEY (event_id, price_id) ,"\
                + "FOREIGN KEY (event_id) REFERENCES Event (id) ,"\
                + "FOREIGN KEY (price_id) REFERENCES Prices (id) ,"\
                + "); "

        cursor.execute(query)

        query = "CREATE TABLE  IF NOT EXISTS Dates("\
                + "event_id int NOT NULL ,"\
                + "year INT ,"\
                + "month INT ,"\
                + "date INT ,"\
                + "PRIMARY KEY (event_id, year, month, date) ,"\
                + "FOREIGN KEY (event_id) REFERENCES Event (id)"\
                + "); "

        cursor.execute(query)

        self.db.commit()
        self.db.close()


    def process_attend_capacity(self, string):
        string = string.replace(' ', '')
        string = string.replace(',', '')
        return_list = string.split('/')
        return return_list


    def process_shows_sellout(self, string):
        string = string.replace('\u00a0', '')
        return_list = string.split('/')
        return return_list


    def process_prices(self, string):
        string = string.replace(' ', '')
        string = string.replace('$', '')
        return_list = string.split(',')
        return return_list


    def process_promoters(self, string):
        return_list = string.split('/')
        return return_list


    def process_citys(self, string):
        return_list = string.split(',')
        return return_list


    def insert_item(self, item):

        # artist_event = scrapy.Field()
        #     venue = scrapy.Field()
        #     rank = scrapy.Field()
        #     city = scrapy.Field()
        #     date = scrapy.Field()
        #     gross_sales = scrapy.Field()
        #     attend_cap = scrapy.Field()
        #     shows_sellout = scrapy.Field()
        #     prices = scrapy.Field()
        #     promoters = scrapy.Field()



        rank = item['rank']
        artist_event = item['artist_event']
        venue = item['venue']

        city_list = self.process_citys(item['city'])
        city = city_list[0]
        state = city_list[1]

        date_list = item['date']

        gross_sales_list = self.process_prices(item['gross_sales'])
        sale = gross_sales_list[0]

        attend_cap = self.process_attend_capacity(item['attend_cap'])
        attend = attend_cap[0]
        capacity = attend_cap[1]

        shows_sellout_list = self.process_shows_sellout(item['shows_sellout'])
        show = shows_sellout_list[0]
        sellout = shows_sellout_list[1]

        prices_list = self.process_prices(['prices'])
        promoters_list = self.process_promoters(item['promoters'])

        cursor = self.db.cursor()


        query = "INSERT INTO Artist_Event (name) VALUES (%s);" % artist_event
        query = "INSERT INTO Venue (name) VALUES (%s)" % venue
        query = "INSERT INTO City (name, state) VALUES (%s, %s);" % (city, state)

        for promoter in promoters_list:
            query = "INSERT INTO Promoters (name) VALUES (%s);" % promoter

            query = "INSERT INTO Event_Promoters (event_id, promoter_id) " \
                    "VALUES ( " \
                    "(SELECT id FROM Artist_Event WHERE name = %s)," \
                    "(SELECT id FROM Promoters WHERE name = %s)" \
                    ");" % (artist_event, promoter)

        query = "INSERT INTO Event (" \
                "artist_event_id," \
                "city_id, " \
                "venue_id, " \
                "sale, " \
                "attend, " \
                "capacity, " \
                "gross_show, " \
                "sellout, " \
                "rank)" \
                " VALUES ( " \
                            "(SELECT id FROM Artist_Event WHERE name = %s),"\
                            "(SELECT id FROM City WHERE name = %s),"\
                            "(SELECT id FROM Venue WHERE name = %s), %s, %s, %s, %s, %s, %s " \
                        ");" % (artist_event, city, venue, sale, attend, capacity, show, sellout, rank)

        for price in prices_list:
            query = "INSERT INTO Prices (price) VALUES ( %s);" % price

            query = "INSERT INTO Event_Prices (event_id, price_id) " \
                    "VALUES ( " \
                    "(SELECT id FROM Artist_Event WHERE name = %s)," \
                    "(SELECT id FROM Prices WHERE price = %s)" \
                    ");" % (artist_event, promoter)


        parser = BoxDateParser()
        array = parser.get_date_string(date_list)
        for dates in array:
            for date in dates[2]:
                query = "INSERT INTO Dates values(%s, %s, %s);" % (dates[0], dates[1], date)


        # 1. Venue
        # 2. City
        # 3. Artist_Event
        # 4. Promoters
        # 5. Event
        # 6. Prices
        # 7. Event_Prices
        # 8. Event_Promoters
        # 9. Dates


#                 + "artist_event_id INT ," \
#                 + "city_id INT ,"\
#                 + "venue_id INT ,"\
#                 + "sale INT ,"\
#                 + "attend INT ,"\
#                 + "capacity INT ,"\
#                 + "gross_show INT ,"\
#                 + "sellout INT ,"\
#                 + "rank INT ,"\


# test = BoxLocalDatabase()
