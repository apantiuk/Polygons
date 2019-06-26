import tkinter
import Polygon

WIDTH = 1000
HEIGHT = 500


def draw_polygon(canv, polygon):
    draw_points = []
    for x, y in polygon.points:
        draw_points.append((x * 10 + WIDTH/2, -y *10 + HEIGHT/2))
    canv.create_polygon(draw_points, fill=polygon.layer, width=2)


def main():
    main_window = tkinter.Tk()
    canv = tkinter.Canvas(main_window, width=WIDTH, height=HEIGHT)
    canv.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT)
    canv.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2)
    draw_polygon(canv, Polygon.pol)
    draw_polygon(canv, Polygon.rect1)
    draw_polygon(canv, Polygon.rect2)
    canv.pack()
    main_window.mainloop()


if __name__ == '__main__':
    main()
