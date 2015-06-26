import turtle



url = "http://en.wikipedia.org/wiki/Hilbert_curve"
pro_url="http://www.soc.napier.ac.uk/~andrew/hilbert.html"






def gothru(pts, spd=10):
    """simple function to draw blue line thru given set of points"""
    t = turtle.Turtle()
    t.speed(spd)
    t.penup()
    t.goto(pts[0])
    t.pendown()
    t.pencolor('blue')
    t.pensize(2)
    for i in pts[1:]:
        t.goto(i)

def gotru(ps, spd=10):
    """same as gothru but w/ orange line"""
    u = turtle.Turtle()
    u.speed(spd)
    u.penup()
    u.goto(ps[0])
    u.pendown()
    u.pencolor('orange')
    u.pensize(2)
    for i in ps[1:]:
        u.goto(i)
    

def hl(sm):
    """
    takes sm - the set of points comprising the hilbert curve from the last iteration at 25% overall size.
    returns the set of points for the current iteration.
    basically, it places the previous (smaller) figure formed by sm into view 4 times, centered on
    each quadrant & rotated/reflected appropriately
    """
    a = []
    b = []
    c = []
    d = []
    for i in sm:
        pta = (-1.0*i[1] - 100.0, i[0] - 100.0)
        a.append(pta)     #a in reverse order
        ptb = (i[0]-100.0, i[1]+100.0)
        b.append(ptb)
        ptc = (i[0]+100.0, i[1]+100.0)
        c.append(ptc)
        ptd = (i[1], -1.0*i[0])
        ptd = (ptd[0]+100.0, ptd[1]-100.0)
        d.append(ptd)
    d = d[::-1]
    aa = []
    dd = []
    for p in d:
        aa.append((p[0]-200.0, p[1]))
    for p in a:
        dd.append((p[0]+200.0, p[1]))
    d = dd[::-1]
    return aa + b + c + d



def it(pts, spd=8):
    """
    takes a set of points
    performs the work of calculating the next iteration's vertices
    returns the new set of points

    also calls gotru function, drawing iteration in orange
    """
    sml = []
#    print(pts)
    for i in range(len(pts)):
#        print(i, pts[i])
        x = pts[i][0]*0.50
        y = pts[i][1]*0.50
        tpl = (x, y)
#        print(tpl)
        sml.append(tpl)
#    print(sml)
    gotru(sml, spd)
    newset = hl(sml)
    return newset

    
    
    

def it_sim(pts):
    """
    simpler version of it (iteration step) function;
    no drawing side-effect
    """
    sml = []
    for i in range(len(pts)):
        x = pts[i][0]*0.50
        y = pts[i][1]*0.50
        tpl = (x, y)
        sml.append(tpl)
    newset = hl(sml)
    return newset


def h(n):
    """
    draws iteration n
    and also draws extra orange lines along the way (prev iterations)
    """

    t=turtle.Turtle()
    pts = [(-100.0, -100.0), (-100.0, 100.0), (100.0, 100.0), (100.0, -100.0)]
    if n == 0:    
        gothru(pts, spd=3)
        return
    else:
        while n > 0:
            if n > 5:
                spd = 0
            elif 3 < n < 6:
                spd = 10
            elif n == 3:
                spd = 6
            elif n == 2:
                spd = 5
            pts = it(pts, spd)
            n -= 1
        gothru(pts)
        return



def hilcurve(n):
    """
    draws iteration n, w/o drawing any extra orange lines along the way
    """
    t = turtle.Turtle()
    pts = [(-100.0, -100.0), (-100.0, 100.0), (100.0, 100.0), (100.0, -100.0)]
    if n == 0:    
        gothru(pts)
        return
    else:
        while n > 0:
             pts = it_sim(pts)
             n -= 1
        gothru(pts)
        return
    


def demo(itStart, itEnd, pauseTime=1.2):
    """
    This demos my hilbert curve drawing script, drawing the hilbert curve
    iterations specified. It draws iteration spec'd by itStart and continues up
    through itEnd
    """
    import time
    for n in range(itStart, itEnd+1):
        print("Hilbert Curve iteration \# %s " % str(n), end="")
        for nn in range(3):
            time.sleep(pauseTime/3.0)
            print('.', end='')
        print("")
        sc = turtle.Screen()
        sc.clearscreen()
        hilcurve(n)
    return

def txtUI():
    print("welcome to hilbert_curve by Nathan Smith\nThis python app draws a fractal called the Hilbert Curve\n")
    print("Options: \n(1)Cleaner/single color demo\n(2)Two color demo\n(3)Draw single iteration (single color)\n(4)Draw single iteration(2 color method)\n(5)Learn more about the Hilbert Curve on Wikipedia \n(6)Quit")
    nput = input("Make your selection: ")
    try:
        nput = int(nput)
    except TypeError:
        print("no valid input recognized")
        return txtUI()
    if nput == 1:
        demo(1,6)
    elif nput == 2:
        h(4)
    elif nput == 3:
        t = input("Pick iteration to draw (recommend integer 2-8): ")
        try:
            t = int(t)
        except TypeError:
            print("no valid input recognized")
            return txtUI()
        hilcurve(t)
    elif nput == 4:
        t = input("Pick iteration to draw (recommend integer 2-8): ")
        try:
            t = int(t)
        except TypeError:
            print("no valid input recognized")
            return txtUI()
        h(t)
    elif nput == 5:
        import webbrowser
        webbrowser.open(url, new=1)
    elif nput == 6:
        return
    d = input("Go again (y)? ")
    if d.lower() == 'y':
        print("\n\n")
        sc=turtle.Screen()
        sc.clearscreen()
        return txtUI()
    else:
        return


if __name__ == '__main__':
    txtUI()
