'''
Sophia Morgan and Silvia Mayo
COMP 333
user_interface.py
'''

from data_objects import *
from analysis import *
import csv
import numpy as np
from unit_test import gen_unit_test


class generator():
    ''' A class generator to display all information to the use and allow
        the user to take action.'''
        
    def __init__(self):
        ''' Initialize the generator

            input: nothing
            returns: nothing
        '''
        self.a = Analysis()
        self.song_list = song.read_database('MT_Database.csv')

    def add_singer(self):
        ''' A function to add a singer profile to the database.
        
            input: nothing
            returns: nothing
        '''
        name = input("Enter the name of the singer: ")
        lohi = input("Enter their voice range: ")
        self.a.add_singer(singer(name = name, lohi = lohi))
        return
    
    def modify_singer(self):
        ''' A function to modify an existing singer profile

            input: nothing
            returns: nothing
        '''
        some_singers = self.a.search_for_singer(input("Please type in a keyword to search for the singer: "))
        if len(some_singers) == 1:
            singer_to_modify = some_singers[0]
        else:
            for one_singer in some_singers:
                print(one_singer[:2])
                if input("Is this the singer you want to modify? (y: yes, n: no) ") == 'y':
                    singer_to_modify = one_singer
                    break
        self.a.singers.remove(singer_to_modify)
        self.a.singers.append(singer_to_modify[-1].update_singer_profile())
        return
    
    def display_singers(self):
        ''' A function to display all the current singers
        
            input: nothing
            returns: nothing
        '''
        self.a.display_singers()
        print('\n')
        return
        
    def user_search(self, keyword):
        ''' A function to allow the user to search for any song in the database.

            input: keyword (to search all fields), name, range
            return: np.array of songs matching the keyword
        '''
        index = np.where(self.song_list == keyword)
        result = self.song_list[index[0], :]
        print(result)
        return result
    
    def get_user_input(self):
        ''' A function to get user input on what they are
            aiming to find by using this generator
            
            input: nothing
            returns: setlist'''

        search_by_genre = input("Would you like to consider genre when building your setlist? (y: yes, n: no) ")
        if search_by_genre == 'y':
            setlist = self.a.songs_by_genre(self.song_list)
        
        search_by_singer_ranges = input("Would you like to generate a setlist base on singer profiles? (y: yes, n: no) ")
        if search_by_singer_ranges == 'y':
            setlist = self.a.songs_by_singers(self.song_list)
        
        search_by_timetime = input("Would you like to generate a setlist based on the length of your show? (y: yes, n: no) ")
        if search_by_timetime == 'y':
            setlist = self.a.songs_by_time(setlist)
        print (setlist)
        return (setlist)
    
    def unit_tests(self):
        '''
        UNIT TESTS
        '''
                
                
        test1 = generator.user_search(self,'Agony')
        test1_expected = np.array([['Agony', 147, "['D3-F4', 'C3-F4']", 'Operatic', False, 'Into the Woods']])
        print(test1_expected)
        if np.array_equal(test1, test1_expected):
                    print("test 1 passed!")
        else: print("test 1 failed")
        print("\n")

        print("Test 2: \n")
        test2 = generator.user_search(self,'')
        test2_expected = np.empty(test2.shape)
        print(test2_expected)
        if np.array_equal(test2, test2_expected):
                    print("test 2 passed!")
        else: print("test 2 failed")
        print("\n")
        
        print("Test 3\n")
        test3 = Analysis.songs_by_genre(self,self.song_list)
        print(test3)
                
        print("Test 4 \n")
        test4 = Analysis.songs_by_time(self,self.song_list)
        print(test4)
        
        print("Test 5\n")
        test5 = Analysis.add_song(self, 'Test2_MT_Database.csv')
        print(test5)
                    
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
            print("2: Browse all songs")
            print("3: Add a new song")
            print("4: Add a new singer profile")
            print("5: Modify an existing singer profile")
            print("6: Display all the current singers")
            print("7: Generate setlist based on my prefs")
            print("8: Quit")
            print("\n")
            
            user_action = input("Enter a number: ")
            if user_action == '1':
                key = input("Search for a song by singer, group number, show: ")
                generator.user_search(self, key)
            elif user_action == '2':
                print("How would you like to display the songs?")
                print("1: Alphabetically by song")
                print("2: From shortest to longest by length")
                print("3: Alphabetically by genre")
                print("4: All non-group numbers first")
                print("5: Alphabetically by musical")
                sort_by = input("Enter a number: ")
                Analysis.sort_songs(self, sort_by, 'MT_Database.csv')
            elif user_action == '3':
                Analysis.add_song(self, 'MT_Database.csv')
            elif user_action == '4':
                generator.add_singer(self)
            elif user_action == '5':
                generator.modify_singer(self)
            elif user_action == '6':
                generator.display_singers(self)
            elif user_action == '7':
                generator.get_user_input(self)
            elif user_action == '8':
                generator.unit_tests(self)
                stop_generator = 0
             
if __name__ == '__main__':
    print("Running the generator ...")
    user_interface = generator()
    user_interface.run_generator()