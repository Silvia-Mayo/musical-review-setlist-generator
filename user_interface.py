'''
Sophia Morgan and Silvia Mayo
COMP 333
user_interface.py
'''

from data_objects import *
import csv
import numpy as np


class generator():
    ''' A class generator to display all information to the use and allow
        the user to take action.'''
        
    def __init__(self):
        ''' Initialize the generator

            input: nothing
            returns: nothing
        '''
        
    def display_all_songs(self):
        ''' A function to display all the songs that the generator has
            in its database

            input: nothing
            returns: nothing
        '''
        return
            
    def add_song(self):
        ''' A function to add a song to the database.
        
            input: nothing
            returns: nothing
        '''
        name = input("Enter the name of the song: ")
        length = input("Enter the length of the song in seconds: ")
        voice_range = input("Enter the voice range of the song: ")
        genre = input("Enter the genre of this song: ")
        show_title = input("Enter the show that this song is in: ")
        song(self, name = name, length = length, voice_range = voice_range, genre = genre, show_title = show_title)
        return
    

    def add_singer_profile(self):
        ''' A function to add a singer profile to the database.
        
            input: nothing
            returns: nothing
        '''
        name = input("Enter the name of the singer: ")
        voice_range = input("Enter their voice range: ")
        voice_type = input("Enter their voice type: ")
        singer(self, name = name, voice_range = voice_range, voice_type = voice_type)
        return
        
    def user_search(self, keyword, kind = 'both', name = '', range = ''):
        ''' A function to allow the user to search for any song or singer
            profile in the database.

            input: keyword (to search all fields), kind (either 'song', 'singer', or both), name, range
            return: nothing, will print results
        '''
                    
    def run_generator(self):
        ''' A function to run the generator based on user input. 
            The goal of this is to look like a survey in which the
            user is asked a few questions on what they are trying to 
            achieve and then the generator will give them what they are
            looking for.
        
            input: nothing
            returns: nothing
        '''
        
        print("Welcome to the Musical Review Setlist Generator!")
        stop_generator = 1
        while stop_generator != 0:
            print("What would you like to do?")
            print("1: Search for a song")
            print("2: Display all songs")
            print("3: Add a new song")
            print("4: Add a new user profile")
            print("5: Add a new singer profile")
            print("6: Generate setlist based on my prefs")
            print("\n")
            
            user_action = input("Enter a number: ")
            if user_action == '1':
                key = input("Search for a song by singer, group number, show: ")
                self.generator.user_search(key)
            if user_action == '2':
                self.generator.display_all_songs
            if user_action == '3':
                self.analysis.add_song
            if user_action == '4':
                self.singer.update_singer_profile
            if user_action == '5':
                self.generator.add_singer_profile
            if user_action == '6':
                user_prefs = self.analysis.get_user_input
                self.analysis.search_by_user_prefs(user_prefs)
            
            

