# CorkPL
Cork Programming Language

## Introduction
CorkPL is an interpreted programming language that is written in Python 3.10+
I have been heavily inspired by [Code Pulse](https://www.youtube.com/channel/UCUVahoidFA7F3Asfvamrm7w) and have based my code off of his [Simple Math Interpreter](https://www.youtube.com/playlist?list=PLZQftyCk7_Sdu5BFaXB_jLeJ9C78si5_3) series and his [Make your own Programming Language](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD) series.

## Current Functionality
The current version is a maths interpreter, which supports the following operators:
- Addition/Subtraction e.g. 3+3 or 5-2
- Multiplication/Division e.g. 2*3 or 100/25
  - Divide by zero rejected with an error
- Modulus/Floor Divide e.g. 10%3 or 10//3
- Powers e.g. 3^3 or 25^0.5 (for square root)
  - Complex Numbers, i.e. roots of negative numbers, are rejected with an error
- Order of operations is used.
  - e.g. 1+2*3 evaluates to 7
- Brackets can be used to change this order
  - e.g. (1+2)*3 evaluates to 9

## What do I plan to add?
- Proper, consistent syntax - undecided on what this will be
- Variables
- Boolean Values/Operations
- Better error descriptions/handling
- Strings
- Lists (Arrays)
- Loading/Running Programs from files
- Functions/Subroutines

## How do you run it?
1. Download the code
2. Run the \_\_main__.py program
3. Have a play!
4. Let me know if anyone has any suggestions or any ideas on how to improve the code.

## Requirements
- Python 3.10+
