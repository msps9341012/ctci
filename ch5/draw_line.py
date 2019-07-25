def draw_line(screen, width, x1, x2, y):
    index_start = y*width + x1
    line_width = x2 - x1 + 1
    for i in xrange(line_width):
        screen[index_start + i] = 255
 
screen = []
blank_byte = 0
filled_byte = 255
width = 8
height = 3

for i in xrange(width * height):
    screen.append(blank_byte)

print(screen) 

draw_line(screen,64,20,42,1)

print(screen) 



