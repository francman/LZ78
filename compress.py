# Copyright (c) 2020 Frank Manu
#
# This source code is licensed under MIT license fount in the
# LICENSE file in the root directory of this source tree
#
# The script is created in fulfillment of required coursework
# from the Coding and Information Theory class at UMass Lowell
# EECE 5480 - Spring 2020

def compress():

    #Require program to begin with file
    inputFile = argv[1]

    #Open File to Compress
    with open(inputFile) as uncompressedFile:
        uncompressedFileContents = uncompressedFile.read()

    #Create compression index
    compressionIndex = 0

    #create null character
    null = ''

    #Assign null as the new character
    newCharacter = null

    #create a dictionary with 0th element
    compressionDictionary = {compressionIndex:newCharacter}

    #start reading file uncompressedFileContents
    for character in uncompressedFileContents:
        currentCharacter = newCharacter + character

        if currentCharacter in compressionDictionary.values():
            newCharacter = currentCharacter
        else:
            compressionIndex+=1
            compressionDictionary[compressionIndex] = newCharacter
            newCharacter = character

    #Read file for first element and add to dictionary.




if __name__ == '__main__':
    compress()
