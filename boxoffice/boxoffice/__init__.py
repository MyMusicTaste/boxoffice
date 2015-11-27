 # rank = item['rank']
 #        artist_event = item['artist_event']
 #        venue = item['venue']
 #
 #        city_list = BoxString.normalize_city(item['city'])
 #        city = city_list[0]
 #        state = city_list[1]
 #
 #        date_list = item['date']
 #
 #        gross_sales_list = BoxString.normalize_prices(item['gross_sales'])
 #        sale = gross_sales_list[0]
 #
 #        attend_cap = BoxString.normalize_attend_capacity(item['attend_cap'])
 #        attend = attend_cap[0]
 #        capacity = attend_cap[1]
 #
 #        shows_sellout_list = BoxString.normalize_shows_sellout(item['shows_sellout'])
 #        show = shows_sellout_list[0]
 #        sellout = shows_sellout_list[1]
 #
 #        prices_list = BoxString.normalize_prices(item['prices'])
 #        promoters_list = BoxString.normalize_promoters(item['promoters'])
 #
 #        cursor = self.db.cursor()
 #
 #        query = 'INSERT INTO Artist_Event (name) VALUES ("%s");' % artist_event
 #        cursor.execute(query)
 #
 #        query = 'INSERT INTO Venue (name) VALUES ("%s")' % venue
 #        cursor.execute(query)
 #
 #        query = "INSERT INTO City (name, state) VALUES ('%s', '%s');" % (city, state)
 #        cursor.execute(query)
 #
 #
 #        check_query = 'SELECT COUNT(*) ' \
 #                      'FROM Artist_Event, City, Venue, Dates ' \
 #                      'WHERE Artist_Event.name = "%s" ' \
 #                      'AND City.name = "%s" AND City.state = "%s" ' \
 #                      'AND Venue.name = "%s" ' \
 #                      'AND Dates.year = %s AND Dates.month = %s AND Dates.date = %s;'
 #        cursor.execute(check_query)
 #
 #        if check_query[0][0] == 0:
 #            query = "INSERT INTO Event VALUES (" \
 #                    "NULL, "\
 #                    "(SELECT id FROM Artist_Event WHERE name = '%s'), "\
 #                    "(SELECT id FROM City WHERE name = '%s'), "\
 #                    "(SELECT id FROM Venue WHERE name = '%s'), %s, %s, %s, %s, %s, %s);"\
 #                    % (artist_event, city, venue, sale, attend, capacity, show, sellout, rank)
 #            cursor.execute(query)
 #
 #        for promoter in promoters_list:
 #            query = "INSERT INTO Promoters (name) VALUES ('%s');" % promoter
 #            cursor.execute(query)
 #
 #            # query = "INSERT INTO Event_Promoters (event_id, promoter_id) " \
 #            #         "VALUES ( " \
 #            #         "(SELECT id FROM Event WHERE name = '%s')," \
 #            #         "(SELECT id FROM Promoters WHERE name = '%s')" \
 #            #         ");" % (artist_event, promoter)
 #            # cursor.execute(query)
 #
 #        for price in prices_list:
 #            query = "INSERT INTO Prices (price) VALUES ('%s');" % price
 #            cursor.execute(query)
 #
 #            # query = "INSERT INTO Event_Prices (event_id, price_id) " \
 #            #         "VALUES ( " \
 #            #         "(SELECT id FROM Artist_Event WHERE name = %s)," \
 #            #         "(SELECT id FROM Prices WHERE price = %s)" \
 #            #         ");" % (artist_event, promoter)
 #            # cursor.execute(query)
 #
 #        # parser = BoxDateParser()
 #        # array = parser.get_date_string(date_list)
 #        # for dates in array:
 #        #     for date in dates[2]:
 #        #         query = "INSERT INTO Dates values( (SELECT id FROM Event WHERE), %s, %s, %s);" % (dates[0], dates[1], date)
 #        #         cursor.execute(query)
 #
 #        self.db.commit()