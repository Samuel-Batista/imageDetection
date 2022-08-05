import cv2 as cv



def scan_line(img, start_pos, color, color_range, dir_x = False, regressive = False):
    HEIGHT, WIDHT, _ = img.shape
    pixels = range(HEIGHT - start_pos[1])

    if dir_x:
        pixels = range(WIDHT - start_pos[0])
    
    if regressive:
        pixels.reverse()
    
    x = start_pos[0]
    y = start_pos[1]

    for p in pixels:
        if dir_x:
            x = p
        else:
            y = p
            
        b, g, r = img[y-1:y, x-1:x][0][0][0]
        b1, g1, r1 = color

        if abs(b1 - b) <= color_range and abs(g1 - g) <= color_range and abs(r1 - r) <= color_range:
            return p
    
    return None
