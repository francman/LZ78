# __LZ78 Engine__

This program takes an input file and compresses it using Lempel-Ziv Algorithm from their 1978 paper.

## Setup

- Install Python and add to PATH - Python 3+ recommended
- Clone or Download this directory
- Open a terminal and navigate to the cloned folder.
- Run the following command: __pip install -r requirements.txt__ _This will install all required libraries, dependent on internet connection_

## How To Run

- Open a terminal application and navigate to the Engine's folder
- From the folder type the following command __python compress.py test.txt__
- To compress your own file, simply replace test.txt with your file.
- The compressed file will be [input file].lz78 e.g: __test.txt.lz78__

## Known Bugs

- The last coded token is lost during compressiong, this results is missing a characters after decompressing.
- LZ78 uses numbers in its token/dictionary, therefore, when your input string contains numbers - the program will very likely crash and stop decoding midway (when it encounters a number). Workaround not found yet.

## Test
 Input: ABAABABAABAB

 Expected Ouput (Compressed File): 0A0B1A2A4A4B3

 Obtained Output: 0A0B1A2A4A4B

 There is a token missing. From the above, token 3 is missing resulting in missed characters after decompression. Will fix this when I get the chance.

## Copyright Information

MIT License

The license and copyright information needed for attribution can be found in [LICENSE](https://github.com/francman/LZ78/blob/master/LICENSE) document.

The [LICENSE](https://github.com/francman/LZ78/blob/master/LICENSE) document is located in the root directory of the project.

The project is created in partial fulfillment of required coursework
from the Coding and Information Theory class at UMass Lowell
(EECE 5480) - Spring 2020.

## References
[1] J. Weitzen, - _Coding and Information Theory EECE 5480_, Spring 2020.

[2] R. B. Wells, - _Applied Coding and Information Theory for Engineers_, 1999.

[3] J. Ziv and A. Lempel, _"Compression of individual sequences via variable-rate coding,"_ in IEEE Transactions on Information Theory, vol. 24, no. 5, pp. 530-536, September 1978.

[4] M. Goemans, - _Lempel-Ziv Codes - 18.301A Lecture Notes_, April 2015.    http://math.mit.edu/~goemans/18310S15/lempel-ziv-notes.pdf

[5] D. Vladislav, - _python-LZ78_, July 2018. https://github.com/DyakoVlad/python-LZ78  


