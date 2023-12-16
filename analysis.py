''' 
Sophia Morgan and Silvia Mayo
COMP 333
analysis.py
A file to actually run the analysis for the generator.
'''

import csv
import numpy as np
from data_objects import *


class Analysis():
    '''The generator will run analysis on the user inputted information
       and will return a setlist.'''
       
    
    def __init__(self):
        ''' A function to intialize the class analysis.
        
            input: nothing
            returns: nothing'''
        self.singers = []
        return
        
    def sort_songs(self, key):
        ''' A function to sort the songs based on user input (in place)
        
            input: key for the song sorting
            returns: np.array of sorted songs'''
        np_songs = song.read_database('MT_Database.csv')
        column_sort = int(key)
        if key in '12':
            column_sort -= 1
        sorted_songs = np.argsort(np_songs[:, column_sort])
        print (np_songs[sorted_songs])
        return (np_songs[sorted_songs])

    def add_song(self):
        ''' A function to add a song to the database.
            input: song to be added
            returns: nothing'''
        file_path = 'MT_Database.csv'

        with open('MT_Database.csv', 'r', newline='') as csvfile:
                csv_read = csv.reader(csvfile)
                existing_data = list(csv_read)
        song_name = input("Enter the song name: ")
        ms_list = input("Enter the song length in the minute:seconds format: ").split(':')
        song_length = int(ms_list[0]) * 60 + int(ms_list[1])
        song_ranges = []
        v_range = input("Type a vocal range (the lowest and highest notes separated by a hyphen)\
                        for each soloist in the song. Press 'Enter' when done: ")
        while v_range:
            song_ranges.append(v_range)
            v_range = input("Type a vocal range (the lowest and highest notes separated by a hyphen)\
                            for each soloist in the song. Press 'Enter' when done: ")
        song_genre = input("What genre best describes this song?\nPlease choose from 'Folk', 'Jazz', 'Operatic', 'Pop', 'Rock', and 'R&B': ")
        song_is_group = bool(int(input("Is this song a group number (is there back-up singing)? Type 1 for yes and 0 for no: ")))
        song_musical = input("Enter the name of the musical this song is in: ")
        new_entry = [song_name + "|" + str(song_length) + "|" + str(song_ranges) + "|" + song_genre + "|" + str(song_is_group) + "|" + song_musical]
        existing_data.append(new_entry)
        with open(file_path, 'a', newline='') as csvfile:
            csvfile.write('\n')
            writer = csv.writer(csvfile)
            writer.writerow(new_entry)
        return
        
    def add_singer(self, one_singer: singer):
        ''' A function to add a singer profile to the database.
        
            input: singer to be added
            returns: nothing'''
        self.singers.append([one_singer.name, one_singer.lohi, one_singer])
        return
        
    def display_singers(self):
        ''' A function to display all the singers
        
            input: nothing
            returns: nothing'''
        for row in self.singers:
            print(row[0] + ':', row[1])
        return
    
    def search_for_singer(self, keyword):
        ''' A function to allow the user to search for any singer in the database by name.

            input: keyword
            return: np.array of singers matching the keyword
        '''
        result = []
        for row in self.singers:
            if keyword in row[0]:
                result.append(row)
        return result
        
    def songs_by_singer_profile(self, song_list, one_singer: singer):
        ''' A function that takes in a song databaes to choose from and a singer profile
            and returns a list of songs that are suited for that singer
           
            input: song database to be considered, singer
            returns: list of songs'''
        setlist = []
        for row in song_list:
            for range_str in eval(row[2]):
                if one_singer.voice_range.contains_range(note_range(range_str)):
                    setlist.append(row)
                    break
        return setlist
        
    def songs_by_singers(self, song_list):
        ''' A function that returns a list of songs suited to the singer profiles currently added
            
            input: song database to be considered
            returns: np.array of songs'''
        if self.singers:
            setlist = self.songs_by_singer_profile(song_list, self.singers[0][-1])
            if len(self.singers) > 1:
                for profile in self.singers[1:]:
                    for s in self.songs_by_singer_profile(song_list, profile[-1]):
                        if s[0] not in np.array(setlist):
                            setlist.append(s)
        else:
            setlist = []
        setlist = np.array(setlist)
        return setlist
           
    def songs_by_genre(self, song_list):
        ''' A function that takes in a song database to choose from,
            and asks the user which genre to filter by
            
            input: song database to be considered
            returns: np.array of songs'''

        print("These are the possible genres:\n1: Folk\n2: Jazz\n3: Operatic\n4: Pop\n5: Rock\n6: R&B")
        genre = input("Enter a genre (number): ")
        if genre == '1':
            index = np.where(song_list == 'Folk')
        elif genre == '2':
            index = np.where(song_list == 'Jazz')
        elif genre == '3':
            index = np.where(song_list == 'Operatic')
        elif genre == '4':
            index = np.where(song_list == 'Pop')
        elif genre == '5':
            index = np.where(song_list == 'Rock')
        elif genre == '6':
            index = np.where(song_list == 'R&B')
        setlist = np.array(song_list[index[0], :])
        return setlist
            
    def songs_by_time(self, setlist):
        ''' A function that takes in a show and its length and other
            attributes if necessary and returns a list of songs that
            will fill the allotted time.
            
            input: show length
            returns: np.array of songs'''
        time = int(input("Enter length of your show in seconds: "))
        sl = []
        start_time = 0
        np.random.shuffle(setlist)
        for songs in setlist:
            name,length,srange,style,group,show = songs
            if (int(length) + start_time) <= time:
                sl.append(songs)
                start_time = start_time + int(length)
        setlist = np.array(sl)
        return setlist
        
    