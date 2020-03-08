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

    #Compression index for dictionary navigation
    compressionIndex = 1
    
    #define null character
    null = ''

    #Require program to begin with file
    inputFile = sys.argv[1]

    outputFile = open((inputFile + '.lz78'), "wb")

    #Open File to Compress
    with open(inputFile, "rb") as uncompressedFile:
        uncompressedFileContents = uncompressedFile.read()

    outputFile.write('0'+uncompressedFileContents[0])

    #create a dictionary with 0th element set as null
    currentCharacter = null
    compressionDictionary = {uncompressedFileContents[0] : str(compressionIndex)}
    uncompressedFileContents = uncompressedFileContents[1:]

    compressionIndex += 1
    #start reading file uncompressedFileContents
    for character in uncompressedFileContents:
        currentCharacter += character
        
        if currentCharacter not in compressionDictionary:
            compressionDictionary[currentCharacter] = str(compressionIndex)
            if len(currentCharacter) == 1:
                outputFile.write('0'+currentCharacter)
            else:
                outputFile.write(compressionDictionary[currentCharacter[0:-1]] + currentCharacter[-1])
            
            compressionIndex += 1
            currentCharacter = null

    outputFile.close()

if __name__ == '__main__':
    compress()
