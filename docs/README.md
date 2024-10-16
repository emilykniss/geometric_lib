
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`


# General Description

The 'geometric_lib' project provides a set of functions for calculating geometric parameters of various shapes, such as circles and squares. The main functions include calculating the area and perimeter of shapes.


# Description of each function with call examples
## def calc()
 - Calculates the value of the specified function for the given figure with the given dimensions.

 - Arguments:
fig (str): The name of the figure (e.g. 'circle' or 'square').
func (str): The name of the function (e.g. 'perimeter' or 'area').
size (list): The dimensions of the figure passed to the function (e.g. [radius] for a circle).

 - Returns:
None: Prints the result to the screen.

 - Example:
>>> calc('circle', 'area', [5])
area of ​​circle is 78.54

## def area()
 - Calculates the area of ​​a triangle using Heron's formula.

 - Arguments:
a (float): Length of the first side of the triangle.
b (float): Length of the second side of the triangle.
c (float): Length of the third side of the triangle.

 - Returns:
float: Semiperimeter of the triangle.

 - Example:
>>> area(3, 4, 5)
6.0

## def perimeter()
 - Calculates the perimeter of a triangle.

 - Arguments:
a (float): Length of the first side of the triangle.
b (float): Length of the second side of the triangle.
c (float): Length of the third side of the triangle.

 - Returns:
float: The perimeter of the triangle.

 - Example:
>>> perimeter(3, 4, 5)
12.0



# Project change history with commit hashes
$ git log --pretty=format:"%h - %s" --no-merges | tail -n +2
d76db2a - Add calculate.py
51c40eb - Doc updated for triangle
d080c78 - Triangle added
d078c8d - Docs added
8ba9aeb - Circle and square added

