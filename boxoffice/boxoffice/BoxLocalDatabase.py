import MySQLdb
from items import BoxofficeItem

class BoxLocalDatabase:


    db = MySQLdb.connect('localhost', 'kokonak', '1234', 'testdatabase')

    def __int__(self):
        self.create_tables()


    def create_tables(self):

        cursor = self.db.cursor()


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
                + "event_id int NOT NULL ,"\
                + "price INT ,"\
                + "PRIMARY KEY (event_id, price) ,"\
                + "FOREIGN KEY (event_id) REFERENCES Event (id)"\
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


        # 1. venue
        # 2. city
        # 3. artist_event
        # 4. promoters
        # 5. event
        # 6. prices
        # 7. event_promoters
        # 8. dates

        rank = item['rank']
        artist_event = item['artist_event']
        venue = item['venue']

        city_list = self.process_citys(item['city'])
        city = city_list[0]
        state = city_list[1]

        date = item['date']

        gross_sales_list = self.process_prices(item['gross_sales'])

        attend_cap = self.process_attend_capacity(item['attend_cap'])
        attend = attend_cap[0]
        capacity = attend_cap[1]

        shows_sellout_list = self.process_shows_sellout(item['shows_sellout'])
        show = shows_sellout_list[0]
        sellout = shows_sellout_list[1]

        prices_list = self.process_prices(['prices'])
        promoters_list = self.process_promoters(item['promoters'])


        cursor = self.db.cursor()





        #         parser = BoxDateParser()
        # array = parser.get_date_string(item['date'])
        #
        # for date_list in array:
        #     for date in date_list[2]:
        #         query = "insert into dateTable values(%s, %s, %s);"
        #         args = (date_list[0], date_list[1], date)
        #         cursor.execute(query, args)
        print('')
