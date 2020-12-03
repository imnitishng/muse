from itemadapter import ItemAdapter
import os

import mysql.connector

class MySQLPipeline(object):

    def __init__(self, db, user, passwd, host):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_CREDS")
        if not db_settings:
            raise NotConfigured
        db = db_settings['db']
        user = db_settings['user']
        passwd = db_settings['pass']
        host = db_settings['host']
        return cls(db, user, passwd, host)

    def open_spider(self, spider):
        self.cnx = mysql.connector.connect(user=self.user, password=self.passwd,
                                    host=self.host, database=self.db)        
        self.cursor = self.cnx.cursor()

    def process_item(self, item, spider):          
        if isinstance(item, dict) and item['type'] == 'lyrics':
            del item['type']
            
            data = (item['song'], item['artist'], item['lyrics'], item['parent'])
            query = """INSERT INTO lyrics 
                    (name, artist, lyrics, parent) 
                    VALUES (%s, %s, %s, %s)"""    

            self.cursor.execute(query, data)
            return item

    def close_spider(self, spider):
        # Remove file if we have already scraped from MXM
        if spider.name == 'lyricraper_mxm':
            os.remove("to_mxm.txt")

        self.cnx.commit()
        self.cnx.close()