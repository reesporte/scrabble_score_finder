# scrabble_score_finder

Simple TKinter application to get the validity and score of any English word. Letter scores and distributions were taken from [this article](https://en.wikipedia.org/wiki/Scrabble_letter_distributions). `word_list.txt` comes from [this list](http://pages.cs.wisc.edu/~o-laughl/csw15.txt). Keep in mind that if the inputted word doesn't fit into the letter distributions from the above article or isn't in the above word list, it will be rejected as invalid. Word distributions can be changed in `scoring.py`.

#### Use:
Download the source and run:
```
python3 app.py
```
Then input any word and the app will print either the score or "Invalid word".

#### To use your own word list:
Just download the word list to the current directory and name it word_list.

#### For use in your own application:
```
>> from scoring import score
>> score("this") # 7
>> score("is") # 2
>> score("test") # 4
>> score("of") # 5
>> score("scoring") # 10
>> score("functionality") # 21

>> from scoring import is_word_valid
>> is_word_valid("a") # False
>> is_word_valid("eccentric") # True
```
