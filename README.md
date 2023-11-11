# My Third Code Review: Advanced Python

## Alex Wallace

## Description
For this project, I had to take two lists (contestants, labels), and ultimately find a dog to win a contest by assigning each contestant their own "points" value. First, I removed any dogs under the age of two from the contestants list. Then, I created a list of dictionaries using the 'labels' list as keys and the 'contestants' list as values. Then, I assigned points to each dog's dictionary. Each dog earned 1 point for being able to do tricks, and a point for each extra talent they possessed. After finding these point values, I took the dog with the most points and congratulated the dog on winning the contest! 

Overall, this project went pretty smoothly. It took me a really long time to figure out how to get the name of the winning dog from the dictionary with the most points, but I was able to use a lambda function wrapped in max() to find the dictionary with the largest 'points' value. After that, I was able to extract the dog's name from that dictionary and congratulate him on winning the pageant.

## Setup/Installation Requirements
In order to set this up, you will need to make a directory for your file and then switch over to that directory. Then, create a virtual environment for python 3 to work in. Change into your virtual environment using source venv/bin/activate. You will need to install the requirements.txt file (pip install -r requirements.txt). This will allow you to use jupyterlab.

## Known Bugs
There are no known bugs for this code. Since the 'points' values will never be strings, I didn't have to use try/except or anything when finding the winning dog. This code should work for any list of contestants using the same 'labels' list as keys for the dictionary created. 

## License
Copyright 2023 Alex Wallace

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.