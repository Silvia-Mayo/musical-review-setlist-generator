'''
Sophia Morgan and Silvia Mayo
COMP 333
data_objects.py
'''
import csv
import numpy as np

class singer():
    '''Class singer contains the information for each singer profile using the generator'''
    def __init__(self, name = '', range = '', voice_type = ''):
        self.name = name
        self.range = range
        self.voice_type = voice_type
        
    def update_singer_profile(self):
        ''' A function to allow the user to make alterations to the singer profile
            that they are searching for.
            
            input: nothing
            returns: nothing'''
        return
            
    def display_singer_profile():
        ''' A function to display a specific singer profile.
        
            input: nothing
            returns: nothing'''
        return
        
        
class song():
    '''Class song contains the information for each song using the generator'''
    def __init__(self, name = '', length = 0, range = '', genre = '', show_title = ''):
        self.name = name
        self.length = length
        self.range = range
        self.genre = genre
        self.show_title = show_title
        
    def read_database(file_name : object) :
        with open(file_name) as csvfile:
            csv_read = csv.reader(csvfile, delimiter = '|')
            csv_list = list(csv_read)
            if len(csv_list) == 0: 
                return np.array([])
            csv_array = np.array(csv_list)
            return(csv_array)
        
    
    def is_suitable(self, singer):
        ''' Compares a singer profile to the song profiles and if the 
            attributes match, then this song is a match and will be 
            returned to the user.
            
            input: singer
            returns: Boolean'''
            
    def display_song_profile():
        ''' A function to display a specific song profile.
        
            input: nothing
            returns: nothing'''
        print(song.self.name)
        print(song.self.length)
        print(song.self.range)
        print(song.self.genre)
        print(song.self.show_title)
        return
    
