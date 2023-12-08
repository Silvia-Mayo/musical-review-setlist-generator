'''
Sophia Morgan and Silvia Mayo
COMP 333
data_objects.py
'''
import csv
import numpy as np
from unit_test import gen_unit_test


class note_range():
    '''Class note_range allows the program to interpret a string
    representing a range of musical notes numerically and meaningfully'''
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def get_num(note: str):
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

    def contains_range(self, song_range: 'note_range'):
        '''Takes in a note_range object to compare to self and determine if a singer can sing a song
        
            input: note_range object of a song (self is presumably a singer)
            output: boolean'''
        if note_range.get_num(self.low) <= note_range.get_num(song_range.low):
            if note_range.get_num(self.high) >= note_range.get_num(song_range.high):
                return True
        return False

class singer():
    '''Class singer contains the information for each singer profile using the generator'''
    def __init__(self, name = '', lohi = ''):
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
            
    def display_singer_profile(self):
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
        
    def read_database(file_name: object) :
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
        
    
    def is_suitable(self, one_singer: singer):
        ''' Compares a singer profile to the song profiles and if the 
            attributes match, then this song is a match and will be 
            returned to the user.
            
            input: singer
            returns: Boolean'''
        return one_singer.voice_range.contains_range(self.note_range)
            
    def display_song_profile(self):
        ''' A function to display a specific song profile.
        
            input: nothing
            returns: nothing'''
        print('  Name:', self.name)
        print('Length:', self.length, 'seconds (' + str(self.length // 60) + 'min', str(self.length % 60) + 's)')
        print(' Range:', self.lohi)
        print(' Genre:', self.genre)
        print('  Show:', self.show_title)
        return

g_n = [('C0', 0), ('F#1', 18), ('Gb1', 18), ('D#3', 39), ('Fb3', 40),
       ('C4', 48), ('A4', 57), ('Cb5', 59), ('B#4', 60), ('B#9', 120)]

for (inp, out) in g_n:
    gen_unit_test(note_range.get_num, inp, out)

c_r = [(('C4', 'G5'), ('G4', 'C5'), True), (('Cb4', 'B#4'), ('B#3', 'Cb5'), True),
       (('G#4', 'A#4'), ('A4', 'A4'), True), (('Db4', 'Cb5'), ('Fb4', 'B#4'), False),
       (('F0', 'F1'), ('C4', 'G5'), False), (('F3', 'C6'), ('Bb2', 'G4'), False),
       (('F3', 'C6'), ('C4', 'G5'), True), (('C4', 'G5'), ('F3', 'C6'), False),
       (('E#2', 'Bb3'), ('Fb2', 'G3'), False), (('E#2', 'Bb3'), ('F2', 'G3'), True)]

for ((l1, h1), (l2, h2), b) in c_r:
    gen_unit_test(note_range(l1, h1).contains_range, note_range(l2, h2), b)

songs = [song('Bring Him Home', 195, 'E3-A4', 'Operatic', 'Les Miserables'),
         song('Freeze Your Brain', 173, 'Db3-G4', 'Pop-Rock', 'Heathers'),
         song('Green Finch and Linnet Bird', 144, 'C4-G5', 'Operatic', 'Sweeney Todd'),
         song('Mein Herr', 200, 'G3-D5', 'Jazz', 'Cabaret'),
         song('Pulled', 179, 'C4-E5', 'Pop-Rock', 'The Addams Family')]

Olivia = singer('Olivia', 'Bb3-A5')
Georgia = singer('Georgia', 'F3-E5')
Alex = singer('Alex', 'Eb3-D5')
David = singer('David', 'A2-G4')
Patrick = singer('Patrick', 'C2-D4')

singers = [[Georgia, Alex], [Olivia, David], [Patrick, Olivia], [David, Alex], [Patrick, Georgia]]

for i in range(5):
    for n in range(2):
        gen_unit_test(songs[i].is_suitable, singers[i][n], bool(n))