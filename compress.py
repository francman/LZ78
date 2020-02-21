# Copyright (c) 2020 Frank Manu
#
# This source code is licensed under MIT license fount in the
# LICENSE file in the root directory of this source tree
#
# The script is created in fulfillment of required coursework
# from the Coding and Information Theory class at UMass Lowell
# EECE 5480 - Spring 2020

import sys

def compress():
    #Require program to begin with file
    inputFile = sys.argv[1]

    #Open File to Compress
    with open(inputFile) as uncompressedFile:
        uncompressedFileContents = uncompressedFile.read()

    #Create compression index
    compressionIndex = 0
    #define null character
    null = ''

    tokenArray=[]

    #create a dictionary with 0th element set as null
    currentCharacter = null
    compressionDictionary = {compressionIndex : currentCharacter}

    #start reading file uncompressedFileContents
    for character in uncompressedFileContents:
        if currentCharacter in compressionDictionary.values():
            currentCharacter+=character
        else:
            tokenArray.append(character)
            compressionIndex+=1
            compressionDictionary[compressionIndex] = currentCharacter
            currentCharacter = character

    print(compressionDictionary)
    #Read file for first element and add to dictionary.

if __name__ == '__main__':
    compress()
