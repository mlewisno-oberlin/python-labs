#!/usr/bin/env python3
import math
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk

class Picture():
    
    ##
    # Constructor. Creates Picture either by passing in the path of an image file as param
    # or by passing in a tuple in the format of (x, y) to indicate the size of a blank image. 
    # Example 1: Picture("image.jpg") constructs Picture from image.jpg 
    # Example 2: Picture((500, 500)) constructs Picture with a blank image of size 500*500
    def __init__(self, param):
        # Check if parameter is the right type, because we can't
        # overload functions
        if isinstance(param, tuple) and len(param) == 2:
            self.image = Image.new('RGB', (param))
        elif isinstance(param, str):
            self.image = Image.open(param)
        else:
            raise TypeError('Parameter to Picture() should be a string or 2-tuple!')
        # Default values for pen
        self.pen_color = (0, 0, 0)
        self.pen_position = (0, 0)
        self.pen_width = 1
        self.pen_rotation = 0
        # Pixel data of the image
        self.pixel = self.image.load()
        # Draw object of the image
        self.draw = ImageDraw.Draw(self.image)
        # The main window, if we are displaying an image. If
        # this is None, the window is closed. Otherwise, it
        # is open.
        self.root = None
    
    ##
    # Get the width of the picture
    # @return The width of the picture.
    def getWidth(self):
        return self.image.size[0]
    
    ##
    # Get the height of the picture
    # @return The height of the picture
    def getHeight(self):
        return self.image.size[1]
    
    ##
    # Display the picture.
    def display(self):
        # If we're already displaying an image, destroy it
        if self.root:
            self.root.destroy()
            self.root = None
        self.root = tk.Tk()
        frame = tk.Frame(self.root, width=self.image.size[0], height=self.image.size[1])
        img = ImageTk.PhotoImage(self.image)
        label = tk.Label(frame, image=img)
        # This line ensures that Python doesn't try to garbage collect
        # our photo, due to a bug in Tk.
        label.image = img
        label.pack()
        frame.pack()
    
    ##
    # Close the picture.
    def close(self):
        if self.root:
            self.root.destroy()
            self.root = None
    
    ##
    # Get the color of a pixel at a given coordinate.
    # @param x The x coordinate of the pixel.
    # @param y The y coordinate of the pixel.
    # @return A 3-tuple(?) containing the R, G, B values of pixel at x,y.
    def getPixelColor(self, x, y):
        return self.pixel[x, y]
    
    ##
    # Get the red value of pixel at a given coordinate.
    # @param x The x coordinate of the pixel.
    # @param y The y coordinate of the pixel.
    # @return Integer value containing the red at given pixel.
    def getPixelRed(self, x, y):
        return self.pixel[x, y][0]
    
    ##
    # Get the blue value of pixel at a given coordinate.
    # @param x The x coordinate of the pixel.
    # @param y The y coordinate of the pixel.
    # @return Integer value containing the blue at given pixel.
    def getPixelBlue(self, x, y):
        return self.pixel[x, y][2]
    
    ##
    # Get the green value of pixel at given coordinates.
    # @param x The x coordinate of the pixel.
    # @param y The y coordinate of the pixel.
    # @return Integer value containing the green at given pixel.
    def getPixelGreen(self, x, y):
        return self.pixel[x, y][1]
    
    ##
    # Set pixel to a given color.
    # @param x The x coordinate of the pixel.
    # @param y The y coordinate of the pixel.
    # @param r The new red value.
    # @param g The new green value.
    # @param b The new blue value.
    def setPixelColor(self, x, y, r, g, b):
        self.pixel[x, y] = (r, g, b)
        
    ##
    # Set the red value of a pixel at a given coordinate.
    # @param x The x value of the pixel.
    # @param y The y value of the pixel.
    # @param val The new red value of the pixel.
    def setPixelRed(self, x, y, val):
        green = self.pixel[x, y][1]
        blue = self.pixel[x, y][2]
        self.pixel[x, y] = (val, green, blue)
    
    ##
    # Set the blue value of a pixel at a given coordinate.
    # @param x The x value of the pixel.
    # @param y The y value of the pixel.
    # @param val The new blue value of the pixel.
    def setPixelBlue(self, x, y, val):
        red = self.pixel[x, y][0]
        green = self.pixel[x, y][1]
        self.pixel[x, y] = (red, green, val)
    
    ##
    # Set the green value of a pixel at a given coordinate.
    # @param x The x value of the pixel.
    # @param y The y value of the pixel.
    # @param val The new green value of the pixel.
    def setPixelGreen(self, x, y, val):
        red = self.pixel[x, y][0]
        blue = self.pixel[x, y][2]
        self.pixel[x, y] = (red, val, blue)
    
    ##
    # Change the color of the pen.
    # @param r The new red value.
    # @param g The new green value.
    # @param b THe new blue value.
    def setPenColor(self, r, g, b):
        self.pen_color = (r, g, b)
    
    ##
    # Change the coordinates of the pen.
    # @param x The new x-coordinate.
    # @param y The new y-coordinate.
    def setPosition(self, x, y):
        self.setPenX(x)
        self.setPenY(y)
    
    ##
    # Change the x-coordinate of the pen.
    # @param x The new x-coordinate.
    def setPenX(self, x):
        self.pen_position = (x, self.pen_position[1])

    ##
    # Change the y-coordinate of the pen.
    # @param y The new y-coordinate.
    def setPenY(self, y):
        self.pen_position = (self.pen_position[0], y)
    
    ##
    # Get the width of the pen.
    def getPenWidth(self):
        return self.pen_width
        
    ##
    # Set the width of the pen.
    # @param width The new width of the pen.
    def setPenWidth(self, width):
        self.pen_width = width
    
    ##
    # Rotate the pen.
    # @param theta Amount to rotate the pen by.
    def rotate(self, theta):
        self.pen_rotation += theta
        self.pen_rotation %= 360
    
    ##
    # Set the direction of the pen.
    # @param theta The new direction of the pen, which is the 
    def setDirection(self, theta):
        self.pen_rotation = theta
        self.pen_rotation %= 360

    ##
    # Return the direction of the pen.
    # @return The current direction in degrees of the pen.
    def getDirection(self):
        return self.pen_rotation
    
    ##
    # Draw forward by a given amount.
    # @param distance The number of pixels to draw forward.
    def drawForward(self, distance):
        radian = math.radians(self.pen_rotation)
        endX = self.pen_position[0] + math.cos(radian)*distance
        endY = self.pen_position[1] + math.sin(radian)*distance
        end = (endX, endY)
        self.draw.line((self.pen_position, end), fill=self.pen_color, width = self.pen_width)
        self.pen_position = end

    ##
    # Draw a line segment from the given start to end
    # @param startX The x-coordinate of the start
    # @param startY The y-coordinate of the start
    # @param endX The x-coordinate of the end
    # @param endY The y-coordinate of the end
    def drawLine(self, startX, startY, endX, endY):
        self.draw.line(((startX, startY),(endX, endY)), fill=self.pen_color, width = self.pen_width)

    ##
    # Draw the outline of a circle.
    # @param x The x-coordinate of the center of the circle.
    # @param y The y-coordinate of the center of the circle.
    # @param radius The radius of the circle.
    def drawCircle(self, x, y, radius):
        if (self.pen_width == 1):
            self.draw.ellipse((x-radius/2, y-radius/2,
                               x+radius/2, y+radius/2),
                              outline=self.pen_color)
        elif (self.pen_width < radius):
            for r in range(0, self.pen_width):
                tempRadius=radius-r
                self.draw.ellipse((x-tempRadius/2, y-tempRadius/2, x+tempRadius/2, y+tempRadius/2), outline=self.pen_color)
        else:
            self.drawCircleFill(x, y, radius)

    ##
    # Draw a circle.
    # @param x The x-coordinate of the center of the circle.
    # @param y The y-coordinate of the center of the circle.
    # @param radius The radius of the circle.
    def drawCircleFill(self, x, y, radius):
        self.draw.ellipse((x-radius/2, y-radius/2,
                           x+radius/2, y+radius/2),
                          fill=self.pen_color)
    
    ##
    # Fill a polygon
    # @param xs A list of the x-coordinates?
    # @param ys A list of the y-coordinates?
    def fillPoly(self, xs, ys):
        self.draw.polygon(list(zip(xs, ys)), fill=self.pen_color)
        
    ##
    # Draw the outline of a polygon.
    # @param xs A list of the x-coordinates
    # @param ys A list of the y-coordinates.
    def drawPoly(self, xs, ys):
        if (self.pen_width == 1):
            self.draw.polygon(list(zip(xs, ys)), outline=self.pen_color)
        else:
            numVertices = len(list(xs))
            for x in range(0, numVertices-1):
                self.drawLine(xs[x], ys[x],xs[x+1], ys[x+1])
            self.drawLine(xs[numVertices-1], ys[numVertices-1], xs[0], ys[0])
    
    ##
    # Draw a (filled in) rectangle
    # @param x The x-coordinate of the upper left hand corner rectangle
    # @param y The y-coordinate of the upper left hand corner rectangle.
    # @param w The width of the rectangle
    # @param h The height of the rectangle.
    def drawRectFill(self, x, y, w, h):
        self.draw.rectangle(((x, y), (x+w, y+h)), fill=self.pen_color)

    ##
    # Draw the outline of a rectangle
    # @param x The x-coordinate of the upper left hand corner rectangle
    # @param y The y-coordinate of the upper left hand corner rectangle.
    # @param w The width of the rectangle
    # @param h The height of the rectangle.
    def drawRect(self, x, y, w, h):
        if (self.pen_width == 1):
            self.draw.rectangle(((x, y), (x+w, y+h)), outline=self.pen_color)
        elif (int((self.pen_width+1)/2)>=w or int((self.pen_width+1)/2)>=h):
            self.drawRectFill(x, y, w, h)
        else:
            for r in range(0, int((self.pen_width+1)/2)):
                self.draw.rectangle(((x+r, y+r), (x-r+w, y-r+h)), outline=self.pen_color)
    
    ##
    # Draw a string (words!)
    # @param x The x coordinate of the (upper left hand?) corner of the string.
    # @param y The y-coordinate of the (upper left hand?) corner of the string.
    # @param string The string to be written to the picture.
    def drawString(self, x, y, string):
        self.draw.text((x, y), string, fill=self.pen_color)

    ##
    # Save the file.
    # @param filename The name of the new file.
    def writeFile(self, filename):
        self.image.save(filename)