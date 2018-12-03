from cImage import*

def cs(orig,inc):
    width=orig.getWidth()
    height=orig.getHeight()
    win=ImageWin("CS",width*2,height*2)
    orig.draw(win)
    neworig = EmptyImage(width*2,height*2)
    
    for y in range(height):
        for x in range(width):
            
            oldpixel=orig.getPixel(x,y)
            redNew=oldpixel.getRed()+(oldpixel.getRed()*inc)
            greenNew=oldpixel.getGreen()+(oldpixel.getGreen()*inc)
            blueNew=oldpixel.getBlue()+(oldpixel.getBlue()*inc)
                     
            if(redNew>255):
                redNew = 255
            if(redNew<0):
                redNew = 0
            if(greenNew>255):
                greenNew = 255
            if(greenNew<0):
                greenNew = 0
            if(blueNew>255):
                blueNew = 255
            if(blueNew<0):
                blueNew = 0
                     
            new_pixel=Pixel(redNew, greenNew, blueNew)
            neworig.setPixel(x+x, y+y, new_pixel)
            neworig.setPixel(x+x+1,y+y, new_pixel)
            neworig.setPixel(x+x, y+y+1, new_pixel)
            neworig.setPixel(x+x+1, y+y+1, new_pixel)
            
    neworig.draw(win)
    #image directory here
img = cs(Image("#image directory here"),"brigthens amount: Ex. 1 or .5 etc")
                     
cs(img)
