import cv2

#configurable parameters
sourc = '1132490.jpg'
destination = 'NewImage.png'
scale_percent = 50

src = cv2.imread(sourc,cv2.IMREAD_UNCHANGED)

#calculate the 50 percent of original dimensions

new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

#resize image

output = cv2.resize(src,(new_width, new_height))
cv2.imwrite(destination, output)