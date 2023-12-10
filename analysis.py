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
        return
        
    def sort_songs(self, key):
        ''' A function to sort the songs based on user input (in place)
        
            input: key for the song sorting
            returns: nothing'''
        song_list = song.read_database('Test_MT_Database.csv')
        return
        
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
        song_length = input("Enter the song length as an int in seconds: ")
        song_musical = input("Enter the name of the musical this song is in: ")
        new_entry = [song_name +"|"+ song_length +"|"+ song_musical]
        existing_data.append(new_entry)
        with open(file_path, 'a', newline='') as csvfile:
            csvfile.write('\n')
            writer = csv.writer(csvfile)
            writer.writerow(new_entry)
        
    def add_singer(self, one_singer: singer):
        ''' A function to add a singer profile to the database.
        
            input: singer to be added
            returns: nothing'''
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
