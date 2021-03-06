import Screenshot
import Mouse
import cv2
import numpy as np
import RandTime


def get_mini_map_mask(low,high, template=None):
    # coords for the minimap
    x1 = 571
    y1 = 29
    x2 = 710
    y2 = 180
    mini_map = Screenshot.shoot(x1,y1,x2,y2,'hsv')
    # applies mask
    mask = cv2.inRange(mini_map, low, high)
    return mask, x1, y1

def find_self():
    low_white = np.array([0,0,255])
    upper_white = np.array([1,255,255])

    mask,mmx, mmy = get_mini_map_mask(low_white,upper_white)

    _, contours, _ = cv2.findContours(mask.copy(), 1,2)

    for cnt in contours:
        M = cv2.moments(cnt)
        print(cv2.contourArea(cnt))
        if cv2.contourArea(cnt) == 4:
            #centroid from img moments
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print(cx,cy)

    cv2.imshow('img', mask)
    cv2.waitKey(0)


def findFishingIcon():
    #fish color
    low = np.array([93,119,84])
    high = np.array([121,255,255])
    mask, mm_x, mm_y = get_mini_map_mask(low, high)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        x += mm_x
        y += mm_y
        x2 = x + w
        y2 = y + h
        Mouse.randMove(x,y,x2,y2,1)
        run= 0
        RandTime.randTime(1,0,0,1,9,9)
        return 0
    return 1

def findBankIcon(offset=0, *args):
    # bank hue range
    low = np.array([21,157,173])
    high = np.array([25,178,221])
    mask, mm_x, mm_y = get_mini_map_mask(low, high)

    #cv2.imshow('mask', mask)
    #cv2.waitKey(0)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        try:
            if args[0] == "n":
                x += mm_x
                y += mm_y - offset
                x2 = x + w
                y2 = y + (h/2) 
                Mouse.randMove(x,y,x2,y2,1)
                #Mouse.moveTo(x,y)
                RandTime.randTime(1,0,0,1,9,9)
                return
        except:
            pass

        x += mm_x
        y += mm_y
        x2 = x + w
        y2 = y + h
        Mouse.randMove(x,y,x2,y2,1)
        RandTime.randTime(1,0,0,1,9,9)
        return

def find_mining_icon(offset=0,*args):
    """needs work, not fucntional, copy pasted from findBankIcon"""
    # bank hue range
    low = np.array([26,160,176])
    high = np.array([27,244,228])
    mask, mm_x, mm_y = get_mini_map_mask(low, high)

    #cv2.imshow('mask', mask)
    #cv2.waitKey(0)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if args[0] == "n":
            x += mm_x
            y += mm_y - offset
            x2 = x + w
            y2 = y + (h/2) 
            Mouse.randMove(x,y,x2,y2,1)
            #Mouse.moveTo(x,y)
            RandTime.randTime(1,0,0,1,9,9)
            return

        x += mm_x
        y += mm_y
        x2 = x + w
        y2 = y + h
        Mouse.randMove(x,y,x2,y2,1)
        RandTime.randTime(1,0,0,1,9,9)
        return

def find_furnance(offset=0,*args):
    """finds the inner orange in furnance icon on minimap"""
    # furnance hue range
    low = np.array([10,211,244])
    high = np.array([23,229,255])
    mask, mm_x, mm_y = get_mini_map_mask(low, high)


    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(mask,kernel,iterations = 1)

    #cv2.imshow('mask', dilation)
    #cv2.waitKey(0)
    #return

    _, contours, _ = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        try:
            # clicks north of the icon
            if args[0] == "n":
                x += mm_x
                y += mm_y - offset
                x2 = x + w
                y2 = y + (h/2) 
                Mouse.randMove(x,y,x2,y2,1)
                #Mouse.moveTo(x,y)
                RandTime.randTime(1,0,0,1,9,9)
                return
        except:
            pass

        x += mm_x
        y += mm_y
        x2 = x + w
        y2 = y + h
        Mouse.randMove(x,y,x2,y2,1)
        RandTime.randTime(1,0,0,1,9,9)
        return



if __name__ == "__main__":
    find_self()
