image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
          [30, 20, 20, 10, 10, 40, 40, 40],
          [10, 10, 20, 20, 10, 10, 10, 10],
          [10, 10, 30, 20, 20, 20, 20, 10],
          [40, 40, 10, 10, 10, 10, 10, 10]]

[[30, 30, 30, 30, 30, 30, 30, 40], 
[30, 20, 20, 30, 30, 40, 40, 40], 
[30, 30, 20, 20, 30, 30, 30, 30], 
[30, 30, 30, 20, 20, 20, 20, 30], 
[40, 40, 30, 30, 30, 30, 30, 30]]


def paint_fill(image, x, y, color):
	print(image[x][y])
	recur_fill(image,x,y,color,image[x][y])

def recur_fill(image,x,y,color,old_color):
	if x>len(image)-1 or x<0 or y<0 or y>len(image[0])-1:
		return
	if image[x][y]!=old_color:
		return 
	image[x][y]=color
	recur_fill(image,x-1,y,color,old_color)
	recur_fill(image,x+1,y,color,old_color)
	recur_fill(image,x,y+1,color,old_color)
	recur_fill(image,x,y-1,color,old_color)

paint_fill(image1,1,3,30)
paint_fill(image1,1,3,10)
paint_fill(image1,1,3,30)


print(image1)