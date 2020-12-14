from itemadapter import ItemAdapter
import os
import mysql.connector

from apps.endpoints.models import Songs, SongQueryObject, QueryStatus

class MySQLPipeline(object):
    '''
    This pipeline is used to store the incoming 
    data from spider to a normal SQL database, 
    this will run typically in file based mode of 
    the spider. (Standalone mode using files)
    [Will have to change spider arguments to make 
    this work again.]
    '''

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

class DjangoModelPipeline(object):
    '''
    This pipeline is used to store the incoming 
    data from spider to a Django model, the songs
    have already been stored in the model, this pipeline
    will update them based on the 
    '''

    def __init__(self):
        self.songs_not_found = []
        self.current_query_obj = None

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):   
        if item.get('type') != 'lyrics':
            self.songs_not_found.append(item.get('song_id', 1))
            self.current_query_obj = item.get('query_id')
        else:
            song = Songs.objects.get(pk=item.get('song_id'))
            song.lyrics = item.get('lyrics')
            song.save()

    def close_spider(self, spider):
        # if spider.name == 'lyricraper_mxm':
            # os.remove("to_mxm.txt")
        if self.current_query_obj:
            self.current_query_obj.songids_to_process = str(self.songs_not_found)[1:-1]
        else:
            self.current_query_obj.songids_to_process = ''
        self.current_query_obj.save()
        
