import os
import mysql.connector

from apps.endpoints.models import Song

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
            raise
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
    will update them based on the lyrics that are scraped.
    '''

    def __init__(self):
        self.songs_not_found = []

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):   
        if item.get('type') != 'lyrics':
            self.songs_not_found.append(item.get('song_id'))
        else:
            song = Song.objects.get(pk=item.get('song_id'))
            song.lyrics = item.get('lyrics')
            song.save()

    def close_spider(self, spider):
        # if spider.name == 'lyricraper_mxm':
            # os.remove("to_mxm.txt")
        
        # Remove log file if scraper ran flawlessly
        current_dir = os.path.dirname(os.path.realpath(__file__))
        logs_dir = os.path.abspath(os.path.join(current_dir, '../logs'))
        if not spider.save_logs:
            # os.remove(logs_dir)
            pass

        if self.songs_not_found:
            songs_not_found_str = ','.join(self.songs_not_found)
            spider.RecommendationObj.emptyLyricsSongIDs = songs_not_found_str
        else:
            spider.RecommendationObj.emptyLyricsSongIDs = ''
        spider.RecommendationObj.save()
        
