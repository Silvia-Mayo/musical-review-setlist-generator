'''
Sophia Morgan and Silvia Mayo
COMP 333
user_interface.py
'''

from data_objects import *
from analysis import *
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
        
    def display_all_songs():
        ''' A function to display all the songs that the generator has
            in its database

            input: nothing
            returns: np.array of all the songs in the database
        '''
        song_list = song.read_database('Test_MT_Database.csv')
        print(song_list)
        return song_list

    def add_song():
        ''' A function to add a song to the database.
        
            input: nothing
            returns: nothing
        '''
        name = input("Enter the name of the song: ")
        length = input("Enter the length of the song in seconds: ")
        lohi = input("Enter the voice range of the song: ")
        genre = input("Enter the genre of this song: ")
        show_title = input("Enter the show that this song is in: ")
        a = Analysis()
        a.add_song(song(name = name, length = int(length), lohi = lohi, genre = genre, show_title = show_title))
        return
    

    def add_singer():
        ''' A function to add a singer profile to the database.
        
            input: nothing
            returns: nothing
        '''
        name = input("Enter the name of the singer: ")
        lohi = input("Enter their voice range: ")
        a = Analysis()
        a.add_singer(singer(name = name, lohi = lohi))
        return
      
    '''def user_search(self, keyword, kind = 'both', name = '', range = ''):'''
  
    def user_search(keyword):
        ''' A function to allow the user to search for any song in the database.

            input: keyword (to search all fields), name, range
            return: np.array of songs matching the keyword
        '''
        song_list = song.read_database('MT_Database.csv')
        index = np.where(song_list == keyword)
        result = song_list[index[0], :]
        print(result)
        return result
                    
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
            print("4: Add a new singer profile")
            print("5: Generate setlist based on my prefs")
            print("6: Quit")
            print("\n")
            
            user_action = input("Enter a number: ")
            if user_action == '1':
                key = input("Search for a song by singer, group number, show: ")
                generator.user_search(key)
            if user_action == '2':
                print("How would you like to display the songs?")
                print("1: Alphabetically by song")
                print("2: From shortest to longest by length")
                print("3: Alphabetically by musical")
                sort_by = input("Enter a number: ")
                Analysis.sort_songs(self,sort_by)
            if user_action == '3':
                Analysis.add_song(self)
            if user_action == '4':
                generator.add_singer()
            if user_action == '5':
                Analysis.get_user_input(self)
            if user_action == '6':
                stop_generator = 0
                
if __name__ == '__main__':
    print("Running the generator ...")
    user_interface = generator()
    user_interface.run_generator()

    def unit_tests():
        '''
        UNIT TESTS
        
        Hi Professor Roberts,
        
        These unit tests will run automatically after you quit the generator above.
        The functions I tested include user_search and display_all_songs. Unfortunately,
        I am having an issue comparing np arrays and all of these instances return false 
        even when I am sure that they are the same, so I will have to look into that more later.
        Additionally, there are a lot of extra spaces in our database csv files which I will have 
        to fix later, but for now, these tests account for these inconsistencies as we are still
        building our full database.
        
        UPDATE: The functions and tests have been modified, so they should now all pass.'''


        print("Test 1: \n")
        test1 = generator.user_search(' Hadestown')
        test1_expected = np.array([["All I've Ever Known " ,' 243 ' ,' Hadestown'],
        ['Epic III ' ,' 351 ' ,' Hadestown'],
        ['Flowers ' ,' 211 ' ,' Hadestown'],
        ['Hey, Little Songbird ' ,' 212 ' ,' Hadestown'],
        ["Livin' It Up on Top " ,' 329 ', ' Hadestown'],
        ['Our Lady of the Underground ' ,' 324 ' ,' Hadestown'],
        ['Wait for Me ' ,' 214 ' ,' Hadestown'],
        ['Way Down Hadestown ' ,' 300 ' ,' Hadestown'],
        ['We Raise Our Cups ' ,' 125 ' ,' Hadestown'],
        ['Wedding Song ' ,' 213 ' ,' Hadestown'],
        ['When the Chips Are Down ' ,' 134 ', ' Hadestown'],
        ['Why We Build the Wall ', ' 240 ' ,' Hadestown']])
        print("\n")

        print("test 1 expected = ", test1_expected)
        if np.array_equal(test1, test1_expected):
            print("test 1 passed!")
        else: print("test 1 failed")
        print("\n")
        
        print("Test 2: \n")
        test2 = generator.user_search(' 140 ')
        test2_expected = np.array([['Angel of Music ' ,' 140 ', ' The Phantom of the Opera'],
                                ['My Favorite Things ' ,' 140 ' ,' The Sound of Music']])
        print("\n")

        print("test 2 expected = ", test2_expected)
        if np.array_equal(test2, test2_expected):
            print("test 2 passed!")
        else: print("test 2 failed")
        
        print("\n")
        
        test3 = generator.user_search('Agony ')
        test3_expected = np.array([['Agony ' ,' 147 ', ' Into the Woods']])
        print(test3_expected)
        if np.array_equal(test3, test3_expected):
            print("test 3 passed!")
        else: print("test 3 failed")
        print("\n")

        print("Test 4: \n")
        test4 = generator.user_search('')
        test4_expected = np.empty(test4.shape)
        print(test4_expected)
        if np.array_equal(test4, test4_expected):
            print("test 4 passed!")
        else: print("test 4 failed")
        print("\n")

        print("Test 5: \n")
        test5 = generator.display_all_songs()
        test5_expected = np.array([['Bring Him Home', '195', "['E3-A4']", 'Operatic', 'False', 'Les Miserables'],
                                    ['Freeze Your Brain', '173', "['Db3-G4']", 'Pop-Rock', 'False', 'Heathers'],
                                    ['Green Finch and Linnet Bird', '144', "['C4-G5']", 'Operatic', 'False', 'Sweeney Todd'],
                                    ['Mein Herr', '200', "['G3-D5']", 'Jazz', 'False', 'Cabaret'],
                                    ['Pulled', '179', "['C4-E5']", 'Pop-Rock', 'False', 'The Addams Family']])
        
        print(test5_expected)
        print("\n")
        if np.array_equal(test5, test5_expected):
            print("test 5 passed!")
        else: print("test 5 failed")
        print("\n")
        
    unit_tests()