import tkinter
import CustomPolygon
import Polygon
import pickle

WIDTH = 800
HEIGHT = 600
MAX_AREA_WIDTH = 2.5

canvas = None


def main():
    main_window = tkinter.Tk()
    set_window(main_window)
    main_window.mainloop()


#####
# Setting window and drawing functions
#####

def set_window(main_window):
    global canvas
    canvas = tkinter.Canvas(main_window, width=WIDTH, height=HEIGHT, background='black')
    draw_axes()

    button_first = tkinter.Button(main_window, text='First question', command=first_question)
    button_second = tkinter.Button(main_window, text='Second question', command=second_question)
    button_python = tkinter.Button(main_window, text='Python question', command=python_question)

    button_first.grid(row=0, column=0)
    button_second.grid(row=0, column=1)
    button_python.grid(row=0, column=2)
    canvas.grid(row=1, column=0, columnspan=3)


def draw_axes():
    canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill='white')
    canvas.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, fill='white')


def scale_x(x):
    return x * 10 + WIDTH/2


def scale_y(y):
    return -y * 10 + HEIGHT/2


def draw_custom_polygon(polygon):
    """Draw a polygon.

    Gets points of an instance of CustomPolygon.Polygon, scales and draws them as a polygon

    :param polygon:
    :type polygon: CustomPolygon.Polygon
    :return: nothing
    :rtype: None
    """
    if not isinstance(polygon, CustomPolygon.Polygon):
        return
    draw_points = []
    for x, y in polygon.points:
        draw_points.append((scale_x(x), scale_y(y)))
    canvas.create_polygon(draw_points, fill=polygon.layer, width=1)


def draw_custom_rectangle(rectangle):
    """Draw a rectangle

    Gets two points of an instance of Custom.Rectangle, scale and draws them as a rectangle

    :param rectangle:
    :type rectangle: CustomPolygon. Rectangle
    :return: nothing
    :rtype: None
    """

    if not isinstance(rectangle, CustomPolygon.Rectangle):
        return
    (x0, y0), (x1, y1) = rectangle.top_left_point, rectangle.bottom_right_point

    canvas.create_rectangle(scale_x(x0), scale_y(y0), scale_x(x1), scale_y(y1), fill=rectangle.layer, width=1)


def draw_polygon(polygon, colour='blue'):
    """Draw a polygon.

    Gets all contours of polygon and then scales and draws them in given colour.

    :param polygon:
    :type polygon: Polygon.Polygon
    :param colour:
    :type: str
    :return: nothing
    :rtype: None
    """

    # check if polygon has contours
    if not isinstance(polygon, Polygon.Polygon) or not polygon:
        return

    draw_points = []
    for contour_num in range(len(polygon)):
        for x, y in polygon.contour(contour_num):
            draw_points.append((scale_x(x), scale_y(y)))

        canvas.create_polygon(draw_points, fill=colour, width=1)
        draw_points.clear()


#####
# Tasks
#####

def first_question():
    """ Solution to question 1.

    Uses operations AND (&), OR (|) and NOT (-) to generate given coloured shape.
    Figures A and B are drawn in blue, and the resulting figure is coloured red.

    :return: Nothing
    :rtype: None
    """

    canvas.delete('all')
    draw_axes()

    with open('first_question_data.pickle', 'rb') as file:
        polA, polB = pickle.load(file)  # file contains two objects of type Polygon.Polygon

    result = (polA - polB) | (polB - polA)  # (A NOT B) OR (B NOT A)

    # Other variants of solution
    #result = (polA | polB) - (polA & polB)  # (A OR B) NOT (A AND B)
    #result = polA ^ polB # A XOR B

    draw_polygon(polA)
    draw_polygon(polB)
    draw_polygon(result, 'red')


def second_question():
    """ Solution to question 2.

    Loads a list of shapes, divides it into POLY (red) and OD (blue)
    lists and finds a common area (gate) between each pair of POLY and OD areas.
    If the width of the resulting gate is less than MAX_AREA_WIDTH, then the gate
    will be coloured yellow, otherwise – grey.

    :return: Nothing
    ;:rtype; None
    """

    canvas.delete('all')
    draw_axes()

    with open('second_question_data.pickle', 'rb') as file:
        areas = pickle.load(file)   # file contains list of tuples (Polygon.Polygon, 'colour')

    for area in areas:
        draw_polygon(area[0], area[1])

    polys = [area for area in areas if area[1] == 'red']
    ods = [area for area in areas if area[1] == 'blue']
    gates = []

    for poly in polys:
        for od in ods:
            gate = poly[0] & od[0]
            if gate:  # check is gate has contours
                gates.append(gate)

    for gate in gates:
        xmin, xmax, ymin, ymax = gate.boundingBox()
        if min(xmax - xmin, ymax - ymin) < MAX_AREA_WIDTH:
            draw_polygon(gate, 'yellow')
        else:
            draw_polygon(gate, 'grey')


def python_question():
    """ Solution to python question.

    Draws given red polygon and yellow rectangles using Custom class

    :return: Nothing
    :rtype: None
    """

    canvas.delete('all')
    draw_axes()

    with open('python_question_data.pickle', 'rb') as file:
        # file contains one CustomPolygon.Polygon and two CustomPolygon.Rectangle
        poly, rectangle1, rectangle2 = pickle.load(file)

    draw_custom_polygon(poly)
    draw_custom_rectangle(rectangle1)
    draw_custom_rectangle(rectangle2)


if __name__ == '__main__':
    main()
