'''
Sophia Morgan and Silvia Mayo
COMP 333
data_objects.py
'''

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
        return
    
