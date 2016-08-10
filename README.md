# godelnumber

*godelnumber* is a basic and easy to use script which provides routines for generating Gödel numbering, also known as Gödel encoding.

##What is Gödel numbering?
You can learn more about Gödel numbering here:
https://en.wikipedia.org/wiki/G%C3%B6del_numbering

##godel_number(array)
The `godel_number(array)` routine generates a Gödel number out of an array of numbers (which can be numberical representation of
ASCII encoding, or any other sort of encoding).

**Example use:**

`godel_number([3, 5])`

`godel_number([84, 69, 83, 84])` : generates the Gödel encoding of the decimal ASCII representation of the word "test"

