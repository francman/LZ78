# Copyright (c) 2020 Frank Manu
#
# This source code is licensed under MIT license fount in the
# LICENSE file in the root directory of this source tree
#
# The script is created in fulfillment of required coursework
# from the Coding and Information Theory class at UMass Lowell
# EECE 5480 - Spring 2020

import sys

def decompress():

    #Compression index for dictionary navigation
    decompressionIndex = 0

    #Require program to begin with file
    inputFile = sys.argv[1]

    #define null character
    null = ''
    
    #Open File to Decompress
    with open(inputFile, "rb") as compressedFile:
        compressedFileContents= compressedFile.read()
    outputFile = open((inputFile + '.uncompressed'), "wb")
    decompressionDictionary = {'0': '', '1': compressedFileContents[1]}
    outputFile.write(decompressionDictionary['1'])
    compressedFileContents = compressedFileContents[2:]

    currentCharacter = null

    decompressionIndex = 2

    for character in compressedFileContents:
        if character in '1234567890':
            currentCharacter += character
        else:
            decompressionDictionary[str(decompressionIndex)] = decompressionDictionary[currentCharacter] + character
            outputFile.write(decompressionDictionary[currentCharacter] + character)
            currentCharacter = null
            decompressionIndex += 1

    outputFile.close()
    

if __name__ == '__main__':
    decompress()
