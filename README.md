# Musical Review Setlist Generator
Generates setlists for Broadway-themed musical reviews based on specified criteria.

## Overview

A musical review is a performance of many songs, usually from the musical theater canon. The selection of those songs is largely dependent on factors like the number of performers and their vocal ranges, as well as pereferred stylistic emphasis or variation within the genre. The programatic ordering of the songs is also dependent upon aspects such as energy level and emotional context. My proposed project would take criteria for all these aspects as input and output a setlist suitable for the musical group of the user.

## Proposed Features

1. Module that analyzes inputted singer ranges and determines appropriate songs
2. Module that analyzes stylistic priorities of the user such as genre
3. Module that allows the user to browse and interact with the song database
4. Module that takes in specified length of show and outputs a suitable setlist

## Stakeholders and Intended Users

Users: Any director or participant in a musical review looking to craft a show. A general background in musical theater or understanding of the content is helpful to comprehend the results. Access to sheet music and musicians or instrumentals is often fundamental for putting together a show, but not strictly necessary to benefit from the software.

Stakeholders: Sheet music distributors, composers/lyricists, artistic directors, audiences, musical theater programs or schools, and voice coaches are just some of the people who could concern themselves with this product. More generally, this could be helpful for anyone who is regularly searching for the appropriate music, whether this be for the user themselves, or for a customer providing this service for another population.

## How To Run The Musical Review Setlist Generator
## Prerequisites and installation instructions
1. Install Python 3
2. Download all the files in this repository

## Instructions on how to run the project
1. Navigate to the file user_interface.py and run the file.
2. You will be prompted with a series of options on how to use this setlist generator. Based on your choices, the generator will act accordingly. This project is text-based and all user interaction occurs in the terminal.

## Future directions and suggestions for additional features
1. Ordering a setlist based on mood, feeling, dance, and group number. Originally, we set out to implement this, however we soon realized that classifying all of this is extremely subjective and out of our scope. A way to handle this could be using a spotify api or another platform that has already done this, or that has the technology or ai ability to do so. 
2. Tkinter user interface. Currently the user interface is entirely text based, however we think that for the average person to be able to comfortably use this, having a more user-friendly and prettier interface would be useful.
3. Having the songs downloaded and ready to play as the user browses the database of songs. This could involve just a snippet of the song, or the entire song, as this could be very helpful for people discovering new songs through our project.
