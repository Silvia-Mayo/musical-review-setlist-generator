'''
Sophia Morgan and Silvia Mayo
COMP 333
data_objects.py
'''
import csv
import numpy as np


class note_range():
    '''Class note_range allows the program to interpret a string
    representing a range of musical notes numerically and meaningfully'''
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def get_num(note):
        '''Takes a string of a musical note and its octave and matches it to an integer
        
            input: a string of a note
            returns: an integer representing the note'''
        scale = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
        octave = int(note[-1])
        letter = note[:-1]
        try:
            scale_no = scale.index(letter)
        except:
            if letter == 'B#':
                scale_no = 0
                octave += 1
            elif letter == 'Db':
                scale_no = 1
            elif letter == 'D#':
                scale_no = 3
            elif letter == 'Fb':
                scale_no = 4
            elif letter == 'E#':
                scale_no = 5
            elif letter == 'Gb':
                scale_no = 6
            elif letter == 'Ab':
                scale_no = 8
            elif letter == 'A#':
                scale_no = 10
            elif letter == 'Cb':
                scale_no = 11
                octave -= 1
        num = scale_no + 12 * octave
        return num

    def contains_range(self, song_range):
        '''Takes in a note_range object to compare to self and determine if a singer can sing a song
        
            input: note_range object of a song (self is presumably a singer)
            output: boolean'''
        if note_range.get_num(self.low) <= note_range.get_num(song_range.low):
            if note_range.get_num(self.high) >= note_range.get_num(song_range.high):
                return True
        return False

class singer():
    '''Class singer contains the information for each singer profile using the generator'''
    def __init__(self, name = '', voice_range = ''):
        self.name = name
        self.lohi = lohi
        [low, high] = lohi.split('-')
        self.voice_range = note_range(low, high)
        
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
        print('       Name:', self.name)
        print('Vocal Range:', self.lohi)
        return
        
        
class song():
    '''Class song contains the information for each song using the generator'''
    def __init__(self, name = '', length = 0, lohi = '', genre = '', show_title = ''):
        self.name = name
        self.length = length
        self.lohi = lohi
        [low, high] = lohi.split('-')
        self.note_range = note_range(low, high)
        self.genre = genre
        self.show_title = show_title
        
    def read_database(file_name : object) :
        '''
        Function to read the csv file and convert it to an np array
        input: CSV file
        output: np array'''
        with open(file_name) as csvfile:
            csv_read = csv.reader(csvfile, delimiter = '|')
            csv_list = list(csv_read)
            if len(csv_list) == 0: 
                return np.array([])
            csv_array = np.array(csv_list)
            return(csv_array)
        
    
    def is_suitable(self, one_singer):
        ''' Compares a singer profile to the song profiles and if the 
            attributes match, then this song is a match and will be 
            returned to the user.
            
            input: singer
            returns: Boolean'''
        return one_singer.voice_range.contains_range(self.note_range)
            
    def display_song_profile():
        ''' A function to display a specific song profile.
        
            input: nothing
            returns: nothing'''
        print('  Name:', self.name)
        print('Length:', self.length, 'seconds (' + str(self.length // 60) + 'min', str(self.length % 60) + 's)')
        print(' Range:', self.lohi)
        print(' Genre:', self.genre)
        print('  Show:', self.show_title)
        return
    
