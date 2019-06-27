# Polygons
Answers to Polygons questions

### Requirements
* Python 3.7.3
* Polygon 3.0.8 (`pip install Polygon3`)
* Tkinter 
* Pickle 

### Content
* CustomPolygon.py – contains classes Polygon and Rectangle

* data.txt – contains backup of data

* (first, second, python)_question_data.pickle – contains objects used for examples

* main.py – results of test work


### How to use

To start script execute the current package in the following way

```
$ python main.py
```

It will create a window with three buttons, each corresponds to a question of the test.
 
* **First question** shows result of the expression (**A** NOT **B**) OR (**B** NOT **A**) / (**A** OR **B**) NOT (**A** AND **B**) / **A** XOR **B**.

* **Second question** finds gates between POLY(red) and OD(blue) areas and highlights gates with width < 2.5 with yellow colour.

* **Python question** recreates given scheme using custom class Polygon and Rectangle.