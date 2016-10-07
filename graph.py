def get_y (equation, x):
    l = []
    for char in equation:
        l+=char
    n = 0
    while n < len(l):
        if l[n] == "x":
            l[n] = x
        n+=1
    r = ""
    for char in l:
        r+=str(char)
    return eval(r)
def values (equation, min, max, step):
    x = min
    yvals = []
    while x<=max:
        yvals += [get_y (equation, x)]
        x+=step
    return yvals
def yminimum (ylist):
    return min(ylist)
def ymaximum (ylist):
    return max(ylist)
def ystep (ymin= -10,ymax=10,height=40.0):
    return (float(ymax)-float(ymin))/height
def graph (equation, xmin=False, xmax=False, xstep = False, ymin=False, ymax = False, ystep = False):
    if not xmin:
        xmin = -10
    if not xmax:
        xmax = 10
    if not xstep:
        xstep = (xmax-xmin)/150
    if not ymin:
        ymin = yminimum(values(equation, xmin, xmax, xstep))
    if not ymax:
        ymax = ymaximum(values(equation, xmin, xmax, xstep))
    if not ystep:
        ystep = (ymax-ymin)/40
    y = ymax-ystep/2
    ys=values(equation, xmin, xmax, xstep)
    max_legend_length = int(max(len(str(ymin)),len(str(ymax))))
    bunt = True
    if (xmax-xmin)/xstep+max_legend_length+5>150:
        print ("The x-step is ", ((xmax-xmin)/xstep)/(150+100)," times too small. Please enter in a new value.")
        bunt = False
    while y>= ymin+ystep/2 and bunt:
        row = str(y)+ " "*(max_legend_length+3-len(str(y)))+"|"
        for value in ys:
            if value<y+ystep/2 and value >=y-ystep/2:
                row+="*"
            else:
                row +=" "
        print (row)
        y-=ystep
    if bunt:
        print ((max_legend_length+3)*" ",int((xmax-xmin)/xstep)*"-")
graph ("14*(x)-5",0,100,1.0)
