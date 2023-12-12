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
        self.singers = np.array([])
        return
        
    def sort_songs(self, key):
        ''' A function to sort the songs based on user input (in place)
        
            input: key for the song sorting
            returns: nothing'''
        np_songs = song.read_database('Test2_MT_Database.csv')
        column_sort = int(key) - 1
        sorted_songs = np.argsort(np_songs[:, column_sort])
        print (np_songs[sorted_songs])
        return (np_songs[sorted_songs])
        
    def sort_singers(self, key):
        ''' A function to sort the singers based on user input (in place)
        
            input: key for the singer sorting
            returns: nothing'''
        return

    def add_song(self):
        ''' A function to add a song to the database.
            input: song to be added
            returns: nothing'''
        file_path = 'Test2_MT_Database.csv'

        with open('Test2_MT_Database.csv', 'r', newline='') as csvfile:
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
        song_genre = input("What genre best describes this song?\nPlease choose from 'Folk', 'Jazz', 'Operatic', 'Pop-Rock', and 'R&B': ")
        song_is_group = bool(int(input("Is this song a group number (is there back-up singing)? Type 1 for yes and 0 for no: ")))
        song_musical = input("Enter the name of the musical this song is in: ")
        new_entry = [song_name + "|" + str(song_length) + "|" + str(song_ranges) + "|" + song_genre + "|" + str(song_is_group) + "|" + song_musical]
        existing_data.append(new_entry)
        with open(file_path, 'a', newline='') as csvfile:
            csvfile.write('\n')
            writer = csv.writer(csvfile)
            writer.writerow(new_entry)
        
    def add_singer(self, one_singer: singer):
        ''' A function to add a singer profile to the database.
        
            input: singer to be added
            returns: nothing'''
        self.singers = np.append(self.singers, [one_singer.name, one_singer.lohi, one_singer])
        return
        
    def search_by_singer_profile(self, one_singer: singer):
        '''A function that takes in a singer profile and returns a
           list of songs that are suited for that singer
           
           input: singer to be analyzed
           returns: song list'''
           
    def search_by_user_prefs(self, user_prefs):
        ''' A function that takes in user preferences and returns a 
            list of songs that are suited for that person
            
            input: user_prefs to be analyzed
            returns: song list'''
            
    def search_by_group_number(self, number: int):
        ''' A function that searches for songs that are suited for a 
            specific number of people.
            
            input: number of people, int
            returns: song list'''
            
    def songs_for_show(self, show):
        ''' A function that takes in a show and its length and other
            attributes if necessary and returns a list of songs that
            will fill the allotted time.
            
            input: show length
            returns: song list'''
        
    def get_user_input(self):
        ''' A function to get user input on what they are
            aiming to find by using this generator
            
            input: nothing
            returns: nothing'''
        return
