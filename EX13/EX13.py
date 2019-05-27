"""
Module can create mandelbrot set or julia fractals.

autor: Jaanus
"""
from PIL import Image


def color_select(n, iterations):
    """Choose a color for a pixel during an iteration."""
    mod = [n * 10, n + 10, n]
    color = [0, 0, 0]
    if n >= iterations or n == 0:
        return (0, 0, 0)
    for i in range(3):
        if n <= iterations / 3:
            color[i] = int(mod[i] % 255)
        elif n > iterations / 3 <= iterations * 2 / 3:
            color[i] = int(mod[(i + 1) % len(mod)] % 255)
        elif n > 2 * iterations / 3:
            color[i] = int(mod[(i + 2) % len(mod)] % 255)
        else:
            color[i] = 0
    return (color[0], color[1], color[2])


def mandelbrot(output_name, julia=False, cJulia=-0.70176 - 0.3842 * 1j):
    """Make Mandelbrot set or a Julia fractal.

    Arguments:
        output_name - string with the picure name and extension
        julia - boolean value, where True makes functon output Julia fractal
        cJulia - real number + imaginary number ;value of c in formula z = z ** 2 + c used when julia is True
    """
    size = (500, 500)
    img = Image.new('RGB', size, 'white')
    iterations = 500
    for ix in range(size[0]):
        x = ix * (4 / (size[0] - 1)) - 2
        for iy in range(size[1]):
            y = iy * (4 / (size[1] - 1)) - 2
            c = x + y * 1j
            z = c
            if julia:
                c = cJulia
            n = 0
            while abs(z) < 2 and n <= iterations:
                z = z ** 2 + c
                n += 1
            color = color_select(n, iterations)
            if ix == iy:
                print('x =', ix, 'y =', iy)
            img.putpixel((ix, iy), color)
    print('Done')
    img.save(output_name)


if __name__ == '__main__':
    mandelbrot('EX13_python_Jaanus.png', True, -0.677 + 0.09684j)
