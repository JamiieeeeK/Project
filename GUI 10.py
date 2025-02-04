import tkinter as tk
from tkinter import *
from tkinter import filedialog
#import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
import sympy as sp
from sympy import *
import csv

root = tk.Tk()
root.title("Graph Plotting - JK")
root.geometry("930x700")
root["bg"] = "lightgrey"


#COORDINATE OOP -----
class coordOOP:
    #private attributes as lists
    Xcoordinate = []
    Y1coordinate = []
    Y2coordinate = []

    #set up the methods that will update the list
    @classmethod #mehotds take the class itself
    def set_x(cls,x): #cls refer to the class itself
        cls.Xcoordinate = x
    @classmethod
    def set_y1(cls,y1):
        cls.Y1coordinate = y1
    @classmethod
    def set_y2(cls,y2):
        cls.Y2coordinate = y2
    #set up the methods that will return the list
    @classmethod
    def get_x(cls):
        return cls.Xcoordinate
    @classmethod
    def get_y1(cls):
        return cls.Y1coordinate
    @classmethod
    def get_y2(cls):
        return cls.Y2coordinate

#OOP: location, table_location, table
class locatOOP:
    location = 0
    gLocation = 0
    table = "x"
    table_location = 0

    @classmethod
    def set_locat(cls, Index):
        cls.location = Index
    @classmethod
    def get_locat(cls):
        return cls.location
    
    @classmethod
    def set_gLocat(cls, Index):
        cls.gLocation = Index
    @classmethod
    def get_gLocat(cls):
        return cls.gLocation

    @classmethod
    def set_tableX(cls, Index):
        cls.table = "x"
        cls.table_location = Index
    @classmethod
    def set_tableY(cls, Index, Column):
        if Column == 1:
            cls.table = "y1"
        elif Column == 2:
            cls.table = "y2"
        cls.table_location = Index
    @classmethod
    def get_table(cls):
        return cls.table
    @classmethod
    def get_tableLocate(cls):
        return cls.table_location
    
    
    

#EQUATION -----
def InitialField():
    for i in range(0, len(EntryField_list)):
        CreateField(i)
    EntryField_list[0].insert(1.0, 'sin(x)')

def newField(self=None):
    i = len(EntryField_list)
    EntryField_list.append(str(i+1))
    Appearance_field.append(str(i+1))
    Appearance_num.append(str(i+1))
    Colour_block.append('')
    ColorSetting.append('')
    Colour_list.append("#4f5f9c")
    COLOUR.append(tk.StringVar(root, value='#4f5f9c'))
    OpenColour.append(False)
    LineStyleSetting.append('')
    Style_list.append("solid")
    Style_block.append('')
    Style_choice.append('')
    OpenStyle.append(False)
    Equation_list.append('')
    Line_list.append(str(i+1))
    EntryField_list[i-1].unbind('<ButtonRelease-1>')
    CreateField(i)

def CreateField(I):
    EntryField_list[I] = tk.Text(field_frame, height=2, width=28, bg="whitesmoke", font=("Arial",15))
    EntryField_list[I].grid(row=I, column=1)
    EntryField_list[I].bind('<ButtonRelease-1>', newField)
    EntryField_list[I].bind('<KeyRelease>', GetEquation)
    EntryField_list[I].bind("<Button-1>", lambda x: locatOOP.set_locat(I))
    EntryField_list[I].bind("<Return>", lambda event: "break")
    EntryField_list[I].bind("<Tab>", lambda event: "break")
    
    Appearance_field[I] = tk.Frame(field_frame, height=51, width=58, bg='darkgrey')
    Appearance_field[I].grid(row=I, column=0)
    Appearance_field[I].grid_propagate(False)
    Appearance_num[I] = tk.Text(Appearance_field[I], height=1, width=5, bg="whitesmoke", font=("Arial",15))
    Appearance_num[I].grid(row=0, column=0, columnspan=5)#, padx=2, pady=2)
    Appearance_num[I].insert(1.0,f" {I+1}:")
    Appearance_num[I].config(state='disable')
    
    Colour_block[I] = tk.Frame(Appearance_field[I], height=24, width=24, bg="#4f5f9c", highlightbackground="black", highlightthickness=3)
    Colour_block[I].grid(row=1,column=0, columnspan=2, stick="w")
    Colour_block[I].bind("<Button-1>", lambda x: SelectColour(I))
    if str(ColorSetting[I-1])!= '':
        ColorSetting[I-1].lift()

    Style_block[I] = tk.Frame(Appearance_field[I], height=24, width=34, bg="white", highlightbackground="black", highlightthickness=2)
    Style_block[I].grid(row=1,column=2,columnspan=3,stick="w")
    Style_block[I].grid_propagate(False)
    Style_choice[I] = tk.Text(Style_block[I], height=1, width=3, bg="white")
    Style_choice[I].grid(row=0, column=0,padx=1 , stick="news")
    Style_choice[I].insert(1.0, "───")
    Style_choice[I].config(state='disable')
    Style_choice[I].bind("<Button-1>", lambda x: SelectStyle(I))
    if str(LineStyleSetting[I-1])!= '':
        LineStyleSetting[I-1].lift()
    try:
        if str(LineStyleSetting[I-2])!= '':
            LineStyleSetting[I-2].lift()
    except:
        pass

    Line_list[I] = tk.Button(field_frame, text="⋮", command=lambda: GradientLine(I), height=2, width=2, bg="whitesmoke", font=("Arial", 11))
    Line_list[I].grid(row=I, column=2)



#Colouring ---- 
COLOUR = [tk.StringVar(root, value='#4f5f9c')]
OpenColour = [False]

def SetColour(i):
    #check valid entry document error handling     
    try:
        #Colour_block[i].config(bg=f"{COLOUR[i].get()}")
        Colour_list[i] = COLOUR[i].get()
        Colour_list[i] = Colour_list[i].replace(" ", "")
        COLOUR[i].set(Colour_list[i])
        Colour_block[i].config(bg=Colour_list[i])
        GetEquation()
    except:
        ErrorMsg("wrong rgb") 
    SelectColour(i) #close the widget

def SelectColour(i):
    global ColorSetting
    if str(ColorSetting[i])=='':
        CreateColorFrame(i)        
    elif OpenColour[i] == False:
        ColorSetting[i].grid(row=int(i)+1,rowspan=2,column=0, columnspan=2,padx=2, stick="nw")
        OpenColour[i] = True
    elif OpenColour[i] == True:
        ColorSetting[i].grid_forget()
        OpenColour[i] = False

def CreateColorFrame(i):
    global OpenColor
    ColorSetting[i] = tk.Frame(field_frame, height=54, width=122, bg="whitesmoke", highlightbackground="lightgrey", highlightthickness=2)
    ColorSetting[i].grid(row=int(i)+1,rowspan=1,column=0, columnspan=2,padx=2, stick="nw")
    ColorSetting[i].grid_propagate(False)
    rgbLabel = tk.Label(ColorSetting[i], text=" rgb code:       ", width=11, font=("Arial",11), bg="whitesmoke")
    rgbLabel.grid(row=0, column=1, columnspan=1, stick="nw")
    rgbEntry = tk.Entry(ColorSetting[i], textvariable=COLOUR[i], width=10, font=("Arial",11))
    rgbEntry.grid(row=1, column=1, columnspan=3, pady=3, padx=3, stick="n")
    rgbEntry.bind("<Return>", lambda x: SetColour(i))
    OpenColour[i] = True


def ChangeStyle(style,line,i):
    Style_list[i] = style
    Style_choice[i].config(state='normal')
    Style_choice[i].delete(1.0, tk.END)
    Style_choice[i].insert(1.0, line)
    Style_choice[i].config(state='disable')
    GetEquation()
    SelectStyle(i)

OpenStyle = [False]
def SelectStyle(i):
    if str(LineStyleSetting[i])=='':
        CreateStyleFrame(i)
    elif OpenStyle[i] == False:
        LineStyleSetting[i].grid(row=int(i)+1,rowspan=2,column=0, columnspan=2,padx=2, stick="nw")
        OpenStyle[i] = True
    elif OpenStyle[i] == True:
        LineStyleSetting[i].grid_forget()
        OpenStyle[i] = False

def CreateStyleFrame(i):    
    LineStyleSetting[i] = tk.Frame(field_frame, height=78, width=125, bg="whitesmoke", highlightbackground="lightgrey", highlightthickness=2)
    LineStyleSetting[i].grid(row=int(i)+1,rowspan=2,column=0, columnspan=2,padx=2, stick="nw")
    LineStyleSetting[i].grid_propagate(False)
    LineStyleLabel = tk.Label(LineStyleSetting[i], text="line style:    ", width=13, font=("Arial",11), bg="whitesmoke")
    LineStyleLabel.grid(row=0, column=0, columnspan=3, stick="nwe")
    LineStyleLabel.grid_propagate(False)
    btn_solid = tk.Button(LineStyleSetting[i], text="───", command=lambda:ChangeStyle("solid","───",i), height=1, width=4, font=("Arial",8,"bold"))
    btn_solid.grid(row=1, column=0, padx=5)
    btn_dot = tk.Button(LineStyleSetting[i], text="····", command=lambda:ChangeStyle("dotted","···",i), height=1, width=4, font=("Arial",8,"bold"))
    btn_dot.grid(row=1, column=1)
    btn_dash = tk.Button(LineStyleSetting[i], text="----", command=lambda:ChangeStyle("dashed","---",i), height=1, width=4, font=("Arial",8,"bold"))
    btn_dash.grid(row=2, column=0, padx=5)
    btn_dado = tk.Button(LineStyleSetting[i], text="−·−·", command=lambda:ChangeStyle("dashdot","−·−",i), height=1, width=4, font=("Arial",8,"bold"))
    btn_dado.grid(row=2, column=1)
    OpenStyle[i] = True


    

#GRAPH ------
def format_func(value, tick_number):
    N = int(np.round(value / np.pi))  # Find the multiple of pi
    if N == 0:
        return '0'
    elif N == 1:
        return r'$\pi$'
    elif N == -1:
        return r'$-\pi$'
    else:
        return r'${0}\pi$'.format(N)



xmin = -90
xmax = 360
ymin = -1.5
ymax = 1.5
dragx = 0
dragy = 0
DoMin = -90
DoMax = 360
RaMin = -2
RaMax = 2

def InitialGraph():
    control_graph.grid_forget() #hide setting
    global setting
    global dragx, dragy
    global DoMin, DoMax, RaMin, RaMax
    setting = False

    #initial axis location
    ax.spines[['left','bottom']].set_position('zero')
    ax.spines[['right','top']].set_visible(False)
    plt.grid()

    #set up the default values
    if unit.get() == 'RADIAN': #for radian
        xmin = -2*np.pi
        xmax = 4*np.pi
        ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
        ax.xaxis.set_major_formatter(FuncFormatter(format_func))
        ax.tick_params(axis='x', direction='inout', length=4, width=1, colors='black')
    elif unit.get() == 'DEGREE': #for degree
        xmin = -90
        xmax = 360

    #range value is the same for different unit
    ymin = -5
    ymax = 5

    dragx = dragx/2.5
    dragy = dragy/2.5

    #set the axis to the correct range     
    ax.set(xlim=(DoMin-dragx, DoMax-dragx), ylim=(RaMin+dragy, RaMax+dragy))
    xValue_slider.configure(from_=DoMin-dragx, to=DoMax-dragx)


    #set the axises to the correct position according to the graph 
    if RaMin+dragy >= 0: #x axis stick to the bottom
        ax.spines['top'].set_position(('axes',0.00))
        ax.spines['top'].set_visible(True)
        ax.spines['bottom'].set_visible(False)
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
    elif RaMin+dragy < 0: #x axis locate normally at 0
        ax.spines['bottom'].set_visible(True)
        ax.spines['top'].set_visible(False)
        ax.xaxis.set_ticks_position("bottom")
        ax.xaxis.set_label_position("bottom")
    if RaMax+dragy <= 0: #x axis stick to the top
        ax.spines['bottom'].set_position(('axes',1.00))
        
    if DoMin-dragx >= 0: #y axis stick to the left
        ax.spines['right'].set_position(('axes', 0.00))
        ax.spines['right'].set_visible(True)
        ax.spines['left'].set_visible(False)
        ax.yaxis.set_ticks_position("right")
        ax.yaxis.set_label_position("right")
    elif DoMin-dragx <0: #y axis locate normally at 0
        ax.spines['left'].set_visible(True)
        ax.spines['right'].set_visible(False)
        ax.yaxis.set_ticks_position("left")
        ax.yaxis.set_label_position("left")
    if DoMax-dragx <= 0: #y axis stick to the right
        ax.spines['left'].set_position(('axes', 1.00))

    #set up the axis label
    ax.set_xlabel(str(LabelX.get()) + "     ", loc="right")
    ax.set_ylabel(str(LabelY.get()) + "   ", loc="top")
    canvas.draw()

def ErrorMsg(display):
    error_message.grid(row=0, column=18)
    error_message.config(text=f"*Error: {display}")


def ChangeRadian(*args):
    DomainMin.set(round((-2*np.pi),1))
    DomainMax.set(round((4*np.pi),1))
    RangeMin.set(-2)
    RangeMax.set(2)
    SetDoRan()


def ChangeDegree(*args):
    DomainMin.set(-90)
    DomainMax.set(360)
    RangeMin.set(-2)
    RangeMax.set(2)
    SetDoRan()


#TRIG? ----
def is_trig(eq):
    trig_functions = [sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc, sp.asin, sp.acos, sp.atan, sp.acot, sp.asec, sp.acsc]
    for func in trig_functions:
        try:
            if eq.has(func):
                return True
        except:
            return False
    return False
#----------

def is_valid_expression(expr):
    try:
        sp.sympify(expr)
        return True
    except (sp.SympifyError, SyntaxError):
        return False


def Graph2(Equation, SolveFor, colour, style):
    InitialGraph()
    global y_vals, x_vals, DomainMin, DomainMax
    x_vals = []
    y_vals = []
    xMin = int(round(DoMin,0))-10
    xMax = int(round(DoMax,0))+10
    yMin = int(round(RaMin,0))-10
    yMax = int(round(RaMax,0))+10
    linspaceX = (xMax-xMin)*200
    linspaceY = (yMax-yMin)*200
    plotted = False
    try:
        if SolveFor == 'y':
            if isinstance(Equation, (int, float, sp.Integer, sp.Float)):
                y_val = float(Equation)
                x_vals = np.linspace(xMin, xMax, linspaceX)
                y_vals = np.full_like(x_vals, y_val)
            else:     
                f_np = sp.lambdify(x, Equation, 'numpy')
                if is_trig(Equation) == True:
                    xR_vals = np.linspace(xMin,xMax,linspaceX)
                    y_vals = f_np(xR_vals)

                    if unit.get() == "RADIAN":
                        x_vals = xR_vals
                    elif unit.get() == "DEGREE":
                        x_vals = np.degrees(xR_vals)
                else:
                    x_vals = np.linspace(xMin,xMax,linspaceX)
                    y_vals = f_np(x_vals)

            replacelogln = ""
            if str(Equation).index("log(") != -1:
                indexlog = str(Equation).index("log(")
                equation = str(Equation)
                endplace = indexlog + 4
                replacelogln = equation[0:indexlog] + "ln(" + equation[endplace:len(equation)]
                Equation = replacelogln
        elif SolveFor == 'x':
            if isinstance(Equation, (int, float, sp.Integer, sp.Float)):
                # Equation is a simple assignment like x = 2
                x_val = float(Equation)
                y_vals = np.linspace(yMin,yMax,linspaceY)
                x_vals = np.full_like(y_vals, x_val)
            else:
                f_np = sp.lambdify(y, Equation, 'numpy')  
                if is_trig(Equation):
                    yR_vals = np.linspace(yMin,yMax,linspaceY)
                    x_vals = f_np(yR_vals)

                    if unit.get() == "RADIAN":
                        y_vals = yR_vals
                    elif unit.get() == "DEGREE":
                        y_vals = np.degrees(yR_vals)
                else:
                    y_vals = np.linspace(yMin,yMax,linspaceY)
                    x_vals = f_np(y_vals)
            ax.axvline(x=float(Equation), linestyle=style, label=f"x = {str(Equation)}", color=colour)
            ax.legend()
            plotted = True


    except Exception as e:
        ErrorMsg("Equation: Invalid expression (5)")
    try:
        if x_vals is not None and y_vals is not None:
            if plotted == False:
                Equation = sp.factor(Equation)
                ax.plot(x_vals, y_vals, linestyle=style, label=f"{SolveFor} = {Equation}", color=colour)
                ax.legend()
        error_message.grid_forget()
    except:
        ErrorMsg("Equation: Invalid expression (6)")
    try:
        for i in range(0, len(Point)):
            ax.plot(Point[i][0], Point[i][1], '.', color="black")
    except:
        pass
    canvas.draw()

x, y, z = sp.symbols('x y z')
f = Function('f')(x)
g = Function('g')(x)
h = Function('h')(x)
solve_for = ''

Xintercept = []
Yintercept = []
#Calculate point of interception -----
def PtOfIntercept(expr, solve_for):
    Xintercept = []
    Yintercept = []
    equation = str(expr)
    if "x" in equation:
        # for x = 0
        Yintercept_pt = expr.subs(x,0)
        Xintercept.append(0)
        Yintercept.append(Yintercept_pt)
        #for y = 0
        eq = sp.factor(expr)
        domainMin = DoMin #get the domain values
        domainMax = DoMax
        #print(domainMax) #variable check
        if unit.get() == "DEGREE" and is_trig(eq) == True: #convert into radian if is degree
            domainMin = sp.rad(domainMin)
            domainMax = sp.rad(domainMax)
        #print(domainMin) #variable check
        Xintercept_pts = list(sp.solveset(sp.Eq(eq,0),x, domain=sp.Interval(domainMin, domainMax)))
        #print(Xintercept_pts)
        for i in range(0, len(Xintercept_pts)):
            item = Xintercept_pts[i]
            if not item.is_real:
                Xintercept_pts[i] = float(sp.re(item.evalf()))
            
                
        for item in Xintercept_pts: 
           if item != 0: #prevent duplication
                Xintercept.append(item) #add value to the list
                Yintercept.append(0) #root with y value = 0
                  

    elif solve_for == "x":
        Xintercept.append(eq)
        Yintercept.append(0)
    elif solve_for == "y":
        Xintercept.append(0)
        Yintercept.append(eq)
        
    if unit.get() == "DEGREE":
        Xintercept = ChangePi(Xintercept)

    return Xintercept, Yintercept


        
def ChangePi(list):
    i = -1
    for item in list:
        i += 1
        if "pi" in str(item):
            list[i] = sp.deg(item)         
    return list


plotforinter = False
def PlotIntercept():
    global plotforinter
    if plotforinter == False:
        plotforinter = True
    elif plotforinter == True:
        plotforinter = False
    GetEquation()
 


#PROCESS_GRAPH -----
def GetEquation(*args):
    global plotforinter
    ax.clear()
    canvas.draw()

    for i in range(0,len(EntryField_list)-1):
        Equation_list[i] = EntryField_list[i].get("1.0", tk.END).strip()
        equation = ChangeSymbol(Equation_list[i])
        equation = ChangeFunc(equation)
        try:
            result, solve_for = Equation(equation)
            print("result:", result)
            colour = Colour_list[i]
            style = Style_list[i]
            Graph2(result, solve_for, colour, style)
            if plotforinter == True:
                Xintercept, Yintercept = PtOfIntercept(result, solve_for)
        except:
            pass
            #ErrorMsg("Equation: Invalid expression")
    if plotforinter == True:
        print("x intercept:", Xintercept)
        print("y intercept: ", Yintercept)
        print("--------------")
        PlotCoordinate(Xintercept, Yintercept, "black")

    if len(num_xvalues) >= 2:
        PlotCoordinate(coordOOP.get_x(), coordOOP.get_y1(), y1_rgb.get())
        PlotCoordinate(coordOOP.get_x(), coordOOP.get_y2(), y2_rgb.get())
                
    else:
        pass

def ChangeSymbol(equation):
    if "π" in equation:
        replace_pi = equation
        replace_pi = replace_pi.replace("π", "3.1415926")
        return replace_pi
    if "|" in equation:
        replace_abs = equation
        while "|" in replace_abs:
            first_index = replace_abs.find("|")
            replace_abs = replace_abs[:first_index]+"abs("+replace_abs[first_index+1:]
            second_index = replace_abs.find("|")
            replace_abs = replace_abs[:second_index]+")"+replace_abs[second_index+1:]
        return replace_abs
    else:
        return equation
        
def ChangeFunc(equation):
    if "f(x)" in equation:
        equation = equation.replace("f(x)", "y")
    elif "g(x)" in equation:
        equation = equation.replace("g(x)", "y")
    elif "h(x)" in equation:
        equation = equation.replace("h(x)", "y")

    #print(equation)
    return equation
    



def Equation(Entry):
    Entry = Entry.replace(" ", "")
    solve_for = ''
    Equal = True

    #splitting the Entry into two parts in the eq
    if '=' in Entry:
        lhs_str, rhs_str = Entry.split('=')
        if not is_valid_expression(lhs_str) or not is_valid_expression(rhs_str):
            ErrorMsg("Equation: Invalid expression (1)")
            return
        lhs = sp.sympify(lhs_str.strip())
        rhs = sp.sympify(rhs_str.strip())
        eq = sp.Eq(lhs, rhs)
        #if "f(x)" in Entry or "g(x)" in Entry or "h(x)" in Entry :
        #    eq = rhs
    else:
        if not is_valid_expression(Entry):
            ErrorMsg("Equation: Invalid expression (2)")
            return
    print("eq:", eq)
   
        
    #identify solving for which variable
    if "=" in Entry:
        if "y" in Entry: #or "f(x)" in Entry or "g(x)" in Entry or "h(x)" in Entry:
            solve_for = 'y'
        elif "x" in Entry : #x is the domain
            solve_for = 'x'
            eq = sp.solve(eq,x) #put x the subject, can be removed!?
            eq = eq[0] #x^2 = 4, x = -2, FIX!, if remove, solve in line 603, return positive 
    elif "=" not in Entry:
        Equal = False
        solve_for = 'y'

    print("Equal =", Equal, "solve for =", solve_for)

#white box testing in this procedure, test through every kind of graph that might stimulate each part
#if problem found, fix it
#if some part never used, remove them -> code efficient

    try:
        if Equal == False: #solving for y
            result = eq
            return result, solve_for
        else: #have equal sign
            result = sp.solve(eq, solve_for) #solve and put subject
            if len(result) == 2: 
                return result[1], solve_for #returned the positive y^2 = 4, y = 2
            return result[0], solve_for #only one solution
        error_message.grid_forget()
    except NotImplementedError as e:
        # Handle equation types not supported by SymPy
        ErrorMsg("Error: SymPy does not support solving this type of equation")
        return 0, 0
    
    except Exception as e: #can be anykind of error
        ErrorMsg("Equation: Invalid expression (4)")
        result = eq #if invalid, why still returning something
        return result, solve_for #print

        

#Calculate Values --------
def CalY(eq):
    global xpoint, ypoint
    if is_trig(eq) == True:
        if unit.get() == "DEGREE":
            xRpoint = sp.rad(xpoint)
            ypoint = eq.subs(x, xRpoint).evalf()
            ypoint = round(ypoint, 3)
        elif unit.get() == "RADIAN":
            ypoint = eq.subs(x, xpoint).evalf()
            ypoint=round(ypoint,3)
    else:
            ypoint = eq.subs(x, xpoint)
            ypoint = round(ypoint,2)
    eq = ''
    
    if str(ypoint)[-12:] == "000000000000":
        ypoint = float(str(ypoint)[:-12])
        
    if str(ypoint)== "nan":
        return "null"
    return ypoint

def CalGradient(eq):
    global xpoint, ypoint, gradient
    differentiate = sp.diff(eq,x)
    if is_trig(differentiate) == True:
        if unit.get() == "DEGREE":
            xRpoint = sp.rad(xpoint)
            gradient = differentiate.subs(x,xRpoint) * (3.1415926/180)
        elif unit.get() == "RADIAN":
            gradient = differentiate.subs(x, xpoint)
    else:
        gradient = differentiate.subs(x,xpoint)
    if LineType == "NORMAL":
        gradient = -1*(1/gradient)
    gradient = round(gradient, 3)
    if str(gradient)== "nan":
        return "null"
    return gradient


#AddLine to Field --------
Point = []
def AddLine(*args):
    global xpoint, ypoint, gradient
    LineEq = f"y-{ypoint} = {gradient}*(x-{xpoint})"
    LineEq, solve_for = Equation(LineEq)
    i = len(EntryField_list)-1
    EntryField_list[i].insert(1.0, LineEq)
    
    Point.append([xpoint,ypoint])
    canvas.draw()
    
    newField()

#TANGENT/NORMAL LINE -----
xpoint=000.00
ypoint=00.000
gradient=0.000
eq = ''
xValue = tk.StringVar(root, value='0.000')
LineType = "TANGENT"
def SetX(self):
    global xpoint, xValue, xValue_slider
    xpoint = float(xValue.get())
    xValue_slider.set(xpoint)
    
def GetX(self):
    global xpoint, xValue_slider, xValue
    xpoint = float(xValue_slider.get())
    xValue.set(xpoint)
    CalLine()

def CalLine(*args):
    global xpoint, xValue_slider, xValue_label, line_setting, point, gradient_label, gradient
    eq = EntryField_list[locatOOP.get_gLocat()].get("1.0", tk.END).strip()
    eq = ChangeSymbol(eq)
    try:
        eq, solve_for = Equation(eq)
    except:
        ErrorMsg("Empty Field")
        return 
    if solve_for == 'y':
        ypoint = CalY(eq)
        xValue_label.config(text=f"  line intercept at x: {xpoint} y: {ypoint} ")
        point, = ax.plot(xpoint,ypoint, '.', color="black")
        canvas.draw()
        point.remove()
        gradient = CalGradient(eq)
        gradient_label.config(text=f" gradient = {gradient}  ")
        
    else:
        xValue_label.config(text=f"  line intercept at x: {xpoint} y: null ")
        gradient_label.config(text=f" gradient = 0  ")
    


#whitebox, check printing correct location: Eq: index, Table: column, row
#Alternative, call GradientLine(I) instead, and set loction with in GradientLine

SetLine = True
def GradientLine(I):
    global line_setting,SetLine
    if SetLine == True:
        line_setting.grid(row=2, rowspan=3, column=1, columnspan=3, padx=2, pady=2)
        SetLine = False
        locatOOP.set_gLocat(I)
    elif SetLine == False:
        line_setting.grid_forget()
        SetLine = True

def ChangeType(*args):
    global LineType, TLine_button, TLine_menu
    if LineType == "TANGENT":
        TLine_button.config(text="NORMAL")
        TLine_menu.entryconfig(0, label="Tangent", command=ChangeType)
        LineType = "NORMAL"
    elif LineType == "NORMAL":
        TLine_button.config(text="TANGENT")
        TLine_menu.entryconfig(0, label="Normal", command=ChangeType)
        LineType = "TANGENT"
    CalLine()

    

    
def lineFrame(*args):
    global GradientLine_Frame, line_setting, xValue_label, xValue_slider, xValue_enter, gradient_label, TLine_button, TLine_menu
    Label = tk.Label(line_setting, text="Tangent/Normal Line", bg="whitesmoke", font=14)
    Label.grid(row=0, column=1, columnspan=6, pady=5)
    xValue_label = tk.Label(line_setting, text=f"  line intercept at x: {xpoint} y: {ypoint} ", bg="whitesmoke", font=12)
    xValue_label.grid(row=1, column=1, columnspan=5, stick="w")
    xValue_label.grid_propagate(False)
    xValue_slider = tk.Scale(line_setting, from_=-90.0, to=360.0, resolution=0.0001, command=GetX, bg="whitesmoke", width=15, length=275, font=12, orient=HORIZONTAL)
    xValue_slider.set(0)
    xValue_slider.grid(row=2, rowspan=3, column=1, columnspan=5, padx=5, stick="w")
    xValue_enter = tk.Entry(line_setting, width=7, textvariable=xValue, font=9)
    xValue_enter.grid(row=4, column=6, padx=7)
    xValue_enter.bind("<Return>", SetX)
    line_setting.bind("<Return>", line_setting.grid_forget())
    gradient_label = tk.Label(line_setting, text=f"  gradient = {gradient}  ", bg="whitesmoke", font=12)
    gradient_label.grid(row=5, column=1, columnspan=2, stick="w")
    TLine_button = tk.Menubutton(line_setting, text="TANGENT", width=10, font=("Arial", 11, "bold"), bg="whitesmoke", fg="black", relief="raised")
    TLine_button.grid(row=5, column=5, columnspan=2)
    TLine_menu = Menu(TLine_button, tearoff=0, bg="whitesmoke", font=("Arial", 11))
    TLine_menu.add_command(label="Normal", command=ChangeType)
    TLine_button.config(menu=TLine_menu)
    LineEnter_button = tk.Button(line_setting, text="ENTER", command= lambda:AddLine(), height=1, width=8, font=("Arial", 11, "bold"))
    LineEnter_button.grid(row=6, column=3, columnspan=2, pady=4)

                     
#----------
#GRAPH SETTING ----
DomainMin = tk.StringVar(root, value=-90)
DomainMax = tk.StringVar(root, value=360)
RangeMin = tk.StringVar(root, value=-2)
RangeMax = tk.StringVar(root, value=2)
LabelX = tk.StringVar(root)
LabelX.set("x axis")
LabelY = tk.StringVar(root)
LabelY.set("y axis")

def SetDoRan(*args):
    global DoMin, DoMax, RaMin, RaMax
    try:
        DoMin = float(DomainMin.get().replace(" ", "") )
        DoMax = float(DomainMax.get().replace(" ", "") )
        RaMin = float(RangeMin.get().replace(" ", "") )
        RaMax = float(RangeMax.get().replace(" ", "") )
        GetEquation()
    except:
        if unit.get() == 'RADIAN':
            DomainMin.set(round((-2*np.pi),1))
            DomainMax.set(round((4*np.pi),1)) 
        elif unit.get() == 'DEGREE':
            DomainMin.set(-90.0)
            DomainMax.set(360.0)
        RangeMin.set(-5)
        RangeMax.set(5)
        SetDoRan()


setting = False
def SetGraph():
    global setting
    if setting == False:
        control_graph.grid(row=2, rowspan=3, column=2, columnspan=3)
        setting = True
    elif setting == True:
        control_graph.grid_forget()
        setting = False
        
def SetGraph_Entries():
    global control_graph
    DomainMin_label = tk.Label(control_graph, text="x min value:    ", bg = "whitesmoke", font=10)
    DomainMin_label.grid(row=0, column=1, padx=10)
    domain_min_entry = tk.Entry(control_graph,width=12, textvariable=DomainMin, font=("Arial",12))
    domain_min_entry.grid(row=1, column=1, padx=6, pady=5)
    domain_min_entry.bind("<Return>", SetDoRan)

    DomainMax_label = tk.Label(control_graph, text="x max value:  ", font=10, bg="whitesmoke")
    DomainMax_label.grid(row=0, column=2, padx=10)
    domain_max_entry = tk.Entry(control_graph,width=12, textvariable=DomainMax, font=("Arial",12))
    domain_max_entry.grid(row=1, column=2, padx=6, pady=5)
    domain_max_entry.bind("<Return>", SetDoRan)

    RangeMin_label = tk.Label(control_graph, text="y min value:    ", font=10, bg="whitesmoke" )
    RangeMin_label.grid(row=2, column=1, padx=10)
    range_min_entry = tk.Entry(control_graph,width=12, textvariable=RangeMin, font=("Arial",12))
    range_min_entry.grid(row=3, column=1, padx=6, pady=5)
    range_min_entry.bind("<Return>", SetDoRan)

    RangeMax_label = tk.Label(control_graph, text="y max value:  ", font=10, bg="whitesmoke")
    RangeMax_label.grid(row=2, column=2, padx=10)
    range_max_entry = tk.Entry(control_graph,width=12, textvariable=RangeMax, font=("Arial",12))
    range_max_entry.grid(row=3, column=2, padx=6, pady=5)
    range_max_entry.bind("<Return>", SetDoRan)

    xLabel_label = tk.Label(control_graph, text="x axis label:  ", font=10, bg="whitesmoke")
    xLabel_label.grid(row=4, column=1, padx=10)
    xLabel_entry = tk.Entry(control_graph, width=12, textvariable=LabelX, font=("Arial",12))
    xLabel_entry.grid(row=5, column=1, padx=6, pady=5)
    xLabel_entry.bind("<Return>", SetDoRan)
    
    yLabel_label = tk.Label(control_graph, text="y axis label:  ", font=10, bg="whitesmoke")
    yLabel_label.grid(row=4, column=2, padx=10)
    yLabel_entry = tk.Entry(control_graph, width=12, textvariable=LabelY, font=("Arial",12))
    yLabel_entry.grid(row=5, column=2, padx=6, pady=5)
    yLabel_entry.bind("<Return>", SetDoRan)

    Enter = tk.Button(control_graph, text="-- Enter --", command=SetDoRan, font=("Arial",12, "bold"))
    Enter.grid(row=6, column=1, columnspan=2, pady=5)

def OnDrag(event):
    global originalx, originaly
    #save original location x and y
    originalx = event.x
    originaly = event.y
def drag_graph(event):
    global originalx, originaly
    global dragx, dragy
    #calculate the changes (drag)
    dragx = canvas.get_tk_widget().winfo_x() - originalx + event.x
    dragy = canvas.get_tk_widget().winfo_y() - originaly + event.y
    InitialGraph()
    canvas.draw()

def UpdateDrag(event):
    global DoMin, DoMax, RaMin, RaMax, dragx, dragy
    DomainMin.set(DoMin-dragx)
    DomainMax.set(DoMax-dragx)
    RangeMin.set(RaMin+dragy)
    RangeMax.set(RaMax+dragy)
    #update the values
    DoMin = DoMin-dragx
    DoMax = DoMax-dragx
    RaMin = RaMin+dragy
    RaMax = RaMax+dragy
    #reset drag
    dragx = 0
    dragy = 0
    GetEquation()

    
#--------
#CHANGE PAGE ----
page = "EQUATION"
def ShowTable(*args):
    global page, bestFit_menu, SetLine
    TGraph_button.config(text="TABLE")
    TGraph_menu.entryconfig(0, label="Equation", command=ShowEquation)
    scroll_table.grid(row=1, column=1, rowspan=6, columnspan=8, pady=4, stick="n")
    v_table.grid(row=1, rowspan=6,column=0, stick="nsw", pady=4)
    h_table.grid(row=6, column=1, columnspan=8, stick="sew", pady=4)
    scroll_canvas.grid_forget()
    v_field.grid_forget()
    page = "TABLE"
    Intercept_button.config(text="BEST FIT LINE")
    Intercept_button.config(menu=bestFit_menu)
    Intercept_button.unbind("<Button-1>")
    if SetLine == False:
        line_setting.grid_forget()
        SetLine = True
    

def ShowEquation(*args):
    global page
    TGraph_button.config(text="EQUATION")
    TGraph_menu.entryconfig(0,label="Table", command=ShowTable)
    scroll_canvas.grid(row=1, column=1, rowspan=6, columnspan=8, pady=4, stick="n")
    v_field.grid(row=1, rowspan=6,column=0, stick="nsw", pady=4)
    scroll_table.grid_forget()
    v_table.grid_forget()
    h_table.grid_forget()
    page = "EQUATION"
    Intercept_button.config(text="INTERCEPTION")
    Intercept_button.config(menu="")
    Intercept_button.bind("<Button-1>", lambda event: PlotIntercept())

    
    
#---------
#Process coordinate ----
def PlotCoordinate(Xlist, Ylist, colour):
    x = 0
    y = 0
    InitialGraph()

    for i in range(0,len(Xlist)):
        try:
            x = float(Xlist[i])
            y = float(Ylist[i])
            ax.plot(x, y, '.', color=colour)
        except:
            if Xlist[i] == "" or Ylist[i] == "":
                ErrorMsg("")#Table: empty")
            else:
                ErrorMsg("Table: Invalid expression")
        canvas.draw()
    

#Table Field ----
Col = "X"              
def ActY1(*args):
    global Col
    global y1_coordinate, num_y1values, y1_colour
    y1_coordinate.config(state="normal", bd=1, bg="#FDFDFD")
    y1_coordinate.insert(1.0, "   y₁")
    y1_coordinate.config(state="disable")
    #unbind
    for I in range(0, len(num_y1values)):
        num_y1values[I].unbind("<<Modified>>")
        num_y1values[I].config(bg="#FDFDFD")
        num_y2values[I].config(bd=1)
    Col = "Y1"
    y1_colour.grid(row=1, column=4, pady=4, padx=4, sticky="e")
    
        
def ActY2(*args):
    global Col
    global y2_coordinate, num_y2values, y2_colour
    y2_coordinate.config(state="normal", bd=1, bg="#FDFDFD")
    y2_coordinate.insert(1.0, "   y₂")
    y2_coordinate.config(state="disable")
    #unbind
    for I in range(0, len(num_y2values)):
        num_y2values[I].unbind("<<Modified>>")
        num_y2values[I].config(bd=1, bg="#FDFDFD")
    Col = "Y2"
    y2_colour.grid(row=1, column=6, pady=4, padx=4, sticky="e")
        
num_xvalues = []
num_y1values = []
num_y2values = []
y1_rgb = tk.StringVar(root, "#626c8d")
y2_rgb = tk.StringVar(root, "#736a58")
OpenY1 = False
OpenY2 = False
def YColour(column):
    global OpenY1, ColourFrameY1
    global OpenY2, ColourFrameY2
    if column == 1:
        if OpenY1 == False:
            ColourFrameY1.grid(row=2, rowspan=2, column=3, columnspan=2, sticky="ne")
            OpenY1 = True
        elif OpenY1 == True:
            ColourFrameY1.grid_forget()
            OpenY1 = False
    elif column == 2:
        if OpenY2 == False:
            ColourFrameY2.grid(row=2, rowspan=2, column=5, columnspan=2, sticky="ne")
            OpenY2 = True
        elif OpenY2 == True:
            ColourFrameY2.grid_forget()
            OpenY2 = False

def SetYrgb(column):
    if column == 1:
        y1_colour.config(bg=y1_rgb.get())
    elif column == 2:
        y2_colour.config(bg=y2_rgb.get())
    GetCoordinate()

def coordinates(*args):
    global x_coordinate, y1_coordinate, y2_coordinate, y1_colour, y2_colour, ColourFrameY1, ColourFrameY2
    x_coordinate = tk.Text(coordinate_frame, height=1, width=8, bg="#FDFDFD", font=("Arial",17))
    x_coordinate.grid(row=1, column=1, columnspan=2)
    x_coordinate.insert(1.0, "   x")
    x_coordinate.config(state="disable")

        
    y1_coordinate = tk.Text(coordinate_frame, height=1, width=8, bd=0, bg="whitesmoke", font=("Arial",17))
    y1_coordinate.grid(row=1, column=3, columnspan=2)
    #y1_coordinate.insert(1.0, "   y₁")
    y1_coordinate.config(state="disable")
    y1_colour = tk.Frame(coordinate_frame, height=25, width=25, bg="#626c8d", highlightbackground="#353535", highlightthickness=3)
    y1_colour.grid(row=1, column=3, pady=4, padx=4, sticky="e")
    y1_colour.grid_forget()
    y1_colour.bind("<Button-1>", lambda x: YColour(1))
    ColourFrameY1 = tk.Frame(coordinate_frame, height=25, width=100, bg="lightgrey")
    ColourFrameY1.grid(row=2, rowspan=2, column=3, columnspan=2, sticky="ne")
    ColourFrameY1.grid_forget()
    ColourEntryY1 = tk.Entry(ColourFrameY1, textvariable=y1_rgb, width=10, font=("Arial",11))
    ColourEntryY1.grid(row=1, column=1, columnspan=3, pady=3, padx=3, stick="n")
    ColourEntryY1.bind("<Return>", lambda x: SetYrgb(1))
    
    y2_coordinate = tk.Text(coordinate_frame, height=1, width=8, bd=0, bg="whitesmoke", font=("Arial",17))
    y2_coordinate.grid(row=1, column=5, columnspan=2)
    y2_coordinate.config(state="disable")
    y2_colour = tk.Frame(coordinate_frame, height=25, width=25, bg="#736a58", highlightbackground="#353535", highlightthickness=3)
    y2_colour.grid(row=1, column=5, pady=4, padx=4, sticky="e")
    y2_colour.grid_forget()
    y2_colour.bind("<Button-1>", lambda x: YColour(2))
    ColourFrameY2 = tk.Frame(coordinate_frame, height=25, width=100, bg="lightgrey")
    ColourFrameY2.grid(row=2, rowspan=2, column=5, columnspan=2, sticky="ne")
    ColourFrameY2.grid_forget()
    ColourEntryY2 = tk.Entry(ColourFrameY2, textvariable=y2_rgb, width=10, font=("Arial",11))
    ColourEntryY2.grid(row=1, column=1, columnspan=5, pady=3, padx=3, stick="n")
    ColourEntryY2.bind("<Return>", lambda x: SetYrgb(2))

    NewCoordinate()

def NewCoordinate(*args):
    global ColourFrameY1
    i = len(num_xvalues)
    num_xvalues.append(f"{i+1}")
    num_y1values.append(f"{i+1}")
    num_y2values.append(f"{i+1}")
        
    num_xvalues[i] = tk.Text(coordinate_frame, height=1, width=8, bg="#FDFDFD", font=("Arial", 17))
    num_xvalues[i].grid(row=i+2, column=1, columnspan=2)
    num_xvalues[i].bind('<ButtonRelease-1>',NewCoordinate)
    num_xvalues[i].bind('<KeyRelease>',GetCoordinate)
    num_xvalues[i].bind("<Return>", lambda event: "break")
    num_xvalues[i].bind("<Button-1>", lambda x: locatOOP.set_tableX(i))
    
    
    num_y1values[i] = tk.Text(coordinate_frame, height=1, width=8, bg="whitesmoke", font=("Arial", 17))
    num_y1values[i].grid(row=i+2, column=3, columnspan=2)
    num_y1values[i].bind('<ButtonRelease-1>',NewCoordinate)
    num_y1values[i].bind('<KeyRelease>',GetCoordinate)
    num_y1values[i].bind("<Return>", lambda event: "break")
    num_y1values[i].bind("<Button-1>", lambda x: locatOOP.set_tableY(i, 1))
    


    num_y2values[i] = tk.Text(coordinate_frame, height=1, width=8, bd=0, bg="whitesmoke", font=("Arial", 17))
    num_y2values[i].grid(row=i+2, column=5, columnspan=2)
    num_y2values[i].bind('<ButtonRelease-1>',NewCoordinate)
    num_y2values[i].bind('<KeyRelease>',GetCoordinate)
    num_y2values[i].bind("<Return>", lambda event: "break")
    num_y2values[i].bind("<Button-1>", lambda x: locatOOP.set_tableY(i, 2))


    if i > 0:
        num_xvalues[i-1].unbind('<ButtonRelease-1>')
        num_y1values[i-1].unbind('<ButtonRelease-1>')
        num_y2values[i-1].unbind('<ButtonRelease-1>')

    if Col == "Y2":
        num_y1values[i].config(bg="#FDFDFD")
        num_y2values[i].config(bd=1, bg="#FDFDFD")
    elif Col == "Y1":
        num_y1values[i].config(bd=1,bg="#FDFDFD")
        num_y2values[i].config(bd=1)
        num_y2values[i].bind("<<Modified>>", ActY2)
    else:
        num_y1values[i].config(bd=1, bg="whitesmoke")
        num_y2values[i].config(bd=0, bg="whitesmoke")
        num_y1values[i].bind("<<Modified>>", ActY1)
        num_y2values[i].bind("<<Modified>>", ActY2)

    if i==0:
        ColourFrameY1.lift()
        ColourFrameY2.lift()

line1 = None
line2 = None

def PlotFit(column):
    global line1, line2, fitLine
    global y1_rgb, y2_rgb
    X1list = coordOOP.get_x().copy()
    X2list = coordOOP.get_x().copy()
    Y1list = coordOOP.get_y1().copy()
    Y2list = coordOOP.get_y2().copy()

    if column=="Y1": #if plotting for y1
        while True:
            try:
                Index = Y1list.index('') #find the index of the empty item
                Y1list.pop(Index) #remove them from the list
                X1list.pop(Index)
            except ValueError: #no more empty
                break
        X1list = np.array(X1list, dtype=float) #convert into numpy version
        Y1list = np.array(Y1list, dtype=float)
        X = X1list 
        Y = Y1list
    elif column=="Y2": #separate into different part 
        while True:
            try:
                Index = Y2list.index('')
                Y2list.pop(Index)
                X2list.pop(Index)
            except:
                  break
        X2list = np.array(X2list, dtype=float)
        Y2list = np.array(Y2list, dtype=float)
        X = X2list
        Y = Y2list

    if fitLine.get() == "LINEAR":
        m, c = np.polyfit(X, Y, 1)
        #print(m,c)
        x = np.linspace(-10, 20, 300)
        T = m*x + c
    elif fitLine.get() == "QUADRATIC":
        a, b, c = np.polyfit(X, Y, 2)
        #print(a, b, c)
        x = np.linspace(-10,20,300)
        T = a*x**2 + b*x + c
    elif fitLine.get() == "CUBIC":
        a, b, c, d = np.polyfit(X, Y, 3)
        #print(a, b, c, d)
        x = np.linspace(-10,20,300)
        T = a*x**3 + b*x**2 + c*x + d
    elif fitLine.get() == "EXPONENTIAL":
        Index = np.where(Y == 0)
        Y = np.delete(Y, Index)
        X = np.delete(X, Index)
        
        logY = np.log(Y)
        b, logA = np.polyfit(X, logY, 1)
        a = np.exp(logA)
        #print(a, b)
        x = np.linspace(-10,20,300)
        T = a*np.exp(b*x)
    elif fitLine.get() == "SCATTER":
        x = X
        y = Y
        
        

    if line1 and column == "Y1": #remove the previous one before the new one
        line1.remove()
    if line2 and column == "Y2":
        line2.remove()

        
    if column=="Y1": #for y1
        if fitLine.get() == "SCATTER": #scatter graph
            line1, = ax.plot(x, y, color=y1_rgb.get(), label="y1") 
        else:
            line1, = ax.plot(x, T, '-', color=y1_rgb.get(), label="y1")
    elif column=="Y2": #for y2
        if fitLine.get() == "SCATTER": #scatter graph
            line2, = ax.plot(x, y, color=y2_rgb.get(), label="y2")
        else:
            line2, = ax.plot(x, T, '-', color=y2_rgb.get(), label="y2")
    ax.legend()
    canvas.draw()


    
    

def GetCoordinate(*args):
    I = len(num_xvalues)
    global y1_rgb, y2_rgb
    Xlist = []
    Y1list = []
    Y2list = []
    for i in range(0,I-1):
        xValues = num_xvalues[i].get("1.0", tk.END).strip()
        if "π" in xValues:
            xValues = xValues.replace("π", "3.1415926")
        y1Values = num_y1values[i].get("1.0", tk.END).strip()
        y2Values = num_y2values[i].get("1.0", tk.END).strip()
        if "π" in y1Values:
            y1Values = y1Values.replace("π", "3.1415926")
        if "π" in y2Values:
            y2Values = y2Values.replace("π", "3.1415926")
        try:
            xValues = simplify(xValues)
            y1Values = simplify(y1Values)
        except: 
            pass
        Xlist.append(xValues)
        Y1list.append(y1Values)
        try:
            xValues = simplify(xValues)
            y2Values = simplify(y2Values)
        except:
            pass
        Y2list.append(y2Values)
    coordOOP.set_x(Xlist)
    coordOOP.set_y1(Y1list)
    coordOOP.set_y2(Y2list)

        
    try:
        if len(EntryField_list) >= 2:
            GetEquation()
        else:
            ax.clear()
            canvas.draw()
            InitialGraph()
            PlotCoordinate(coordOOP.get_x(), coordOOP.get_y1(), y1_rgb.get())
            PlotCoordinate(coordOOP.get_x(), coordOOP.get_y2(), y2_rgb.get()) 

            
    except:
        ErrorMsg("Invalid Value Entered")



#----------
#SYMBOL MENU ------
open_menu = False
def ActivateMenu():
    global open_menu
    if open_menu == False:
        SymbolMenu()
        
    elif open_menu == True:
        CloseSymbolMenu()
        open_menu = False
        
def SymbolMenu():
    global open_menu
    global symbol
    symbol = tk.Tk()
    symbol.title("Symbol Menu")
    symbol.geometry("550x610")
    symbol["bg"] = "lightgrey"
    symbol_frame = tk.Frame(symbol,height="585",width="540", bg="whitesmoke")
    symbol_frame.grid(row=1, column=1, padx=5, pady=5)
    SymbolText = tk.Text(symbol, height="26", width="43", bg="whitesmoke")
    SymbolText.grid(row=1, column=1)#, stick="nsew")
    text_1 =" Operator    Name               Example" + "\n" + "  +          Addition           x+y" + "\n" + "  -          Subtraction        x-y" + "\n"
    text_2 ="  *          Multiplication     x*y" + "\n" + "  /          Devision           x/y" + "\n" + "  **         Exponentiation     x**y" + "\n" + "  ^          Exponentiation     x^y" + "\n"
    text_3 ="  sin(x)     sine               sin(x)" + "\n" + "  cos(x)     cosine             cos(x)" + "\n" + "  tan(x)     tangent            tan(x)" + "\n" + "  trig^2     square             sin(x)^2" + "\n"
    text_4 ="  ^(1/2)     square root        x^(1/2)" + "\n" + "  ^(1/□)     root               x^(1/5)" + "\n"          
    text_5 ="  exp(□)     exponential        exp(x)" + "\n" + "  ln(□)      natural logarithm  ln(x)" + "\n"
    text_6 ="  log(□)     logarithm          log10(x)" + "\n" + "  log□(□)    logarithm base□    log2(x)" + "\n" + "  |x|        absolute value     |x|" + "\n" + "  abs(x)     absolute value     abs(x)" + "\n"

    SymbolText.insert(1.0, text_6)
    SymbolText.insert(1.0, text_5)
    SymbolText.insert(1.0, text_4)
    SymbolText.insert(1.0, text_3)
    SymbolText.insert(1.0, text_2)
    SymbolText.insert(1.0, text_1)

    open_menu = True
    symbol.mainloop()

    
    
def CloseSymbolMenu():
    global open_menu
    global symbol
    try:
        symbol.destroy()
    except:
        pass
    open_menu = False
    
    
#--------------
#CLEAR content ----
def clear(*args):
    global EntryField_list, Appearance_field, Line_list, Point, ColorSetting, LineStyleSetting
    global num_xvalues, num_y1values, num_y2values, x_coordinate, y_coordinate, Col, Y1coordinate, Y2coordinate
    global Xintercept, Yintercept, plotforinter
    for i in range(0, len(EntryField_list)):
        #EntryField_list[i].delete(1.0,"end")
        EntryField_list[i].destroy()
        Appearance_field[i].destroy()
        Line_list[i].destroy()
    Col="x"
    for i in range(0,len(num_xvalues)):
        num_xvalues[i].destroy()
        num_y1values[i].destroy()
        num_y2values[i].destroy()
    y1_coordinate.config(bd=0)
    y2_coordinate.config(bd=0)
    

    ColorSetting.remove('')
    LineStyleSetting.remove('')
    for i in range(0,len(ColorSetting)):
        try:
            ColorSetting[i].destroy()
        except:
            pass
    for i in range(0, len(LineStyleSetting)):
        try:
            LineStyleSetting[i].destroy()
        except:
            pass

    EntryField_list = ['1']
    Appearance_field = ['1']
    Appearance_num = ['1']
    Equation_list = ['']
    Line_list = ['1']
    num_xvalues = []
    num_y1values = []
    num_y2values = []
    coordOOP.set_x([])
    coordOOP.set_y1([])
    coordOOP.set_y2([])
    Point = []
    Colour_block = ['']
    ColorSetting = ['']
    Colour_list = [''] 
    COLOUR = []
    COLOUR.append(tk.StringVar(root, value='#000000'))
    Style_block = ['']
    Style_list = ['solid']
    Style_choice = ['']
    LineStyleSetting = ['']
    OpenColour = [False]
    Style_list = ['']
    line_setting.grid_forget()
    plotforinter = False
    Xintercept = []
    Yintercept = []
    LabelX.set("x axis")
    LabelY.set("y axis")
    InitialField()
    ax.clear()
    canvas.draw()
    InitialGraph()
    coordinates()



#store function -------
def StoreCSV(*args):
    Store_list=[]
    for i in range(0,len(EntryField_list)-1):
        Equation_list[i] = EntryField_list[i].get(1.0, tk.END).strip()
        if Equation_list[i] != "":
            Store_list.append(Equation_list[i])

    Xlist = []
    Y1list = []
    Y2list = []

    Xlist = coordOOP.get_x().copy()
    Y1list = coordOOP.get_y1().copy()
    Y2list = coordOOP.get_y2().copy()
        
    # Open the save file dialog to choose the file location and name
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    
    if file_path:  # Proceed if the user selected a file location
        # Write data to the selected file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Equation:"])
            for content in Store_list:
                writer.writerow([content])
                #print(content)
            writer.writerow(["TableX:"])

            for content in Xlist:
                writer.writerow([content])
            writer.writerow(["TableY1:"])
            for content in Y1list:
                writer.writerow([content])
            writer.writerow(["TableY2:"])
            for content in Y2list :
                writer.writerow([content])
                
        
        print(f"CSV file saved as: {file_path}")
        print("----------------------------------------------------")
        


# Column variable to keep track of which section (Equation, TableX, or TableY) is currently being read
column = "Equation"
def OpenCSV(*args):
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(title="Open CSV file", filetypes=[("CSV files", "*.csv")])
    print("------------------------------------------------")
    print(f"CSV file opend from: {file_path}")
    clear() # Clear previous data in the application
    EntryField_list[0].delete("1.0", tk.END)
    if file_path:
        with open(file_path, mode="r") as file: # Open the CSV file in read mode
            reader = csv.reader(file)
            I1 = 0 #Index variable for num_y1values entries
            I2 = 0
            for row in reader:
                if row==['Equation:']:
                    column="Equation"
                elif row==['TableX:']:
                    column="TableX"
                elif row==['TableY1:']:
                    column="TableY1"
                elif row==['TableY2:']:
                    column="TableY2"
                elif column=="Equation":
                    if row != [""]:
                        i = len(EntryField_list)
                        EntryField_list[i-1].insert("1.0", row)
                        newField()
                elif column=="TableX":
                    i = len(num_xvalues)
                    if row == [""]:
                        num_xvalues[i-1].insert("1.0", "")
                    else:
                        num_xvalues[i-1].insert("1.0", row)
                    NewCoordinate()
                elif column=="TableY1":
                    if row == [""]:
                        num_y1values[I1].insert("1.0", "")
                    else:
                        num_y1values[I1].insert("1.0", row)
                    I1 += 1
                elif column =="TableY2":
                    if row == [""]:
                        num_y2values[I2].insert("1.0", "")
                    else:
                        num_y2values[I2].insert("1.0", row)
                    I2 += 1
    GetCoordinate()


    

#------------
#FRAMES ---------
#1. equations
scroll_canvas = Canvas(root, height="500", width="400", bg="whitesmoke")
scroll_canvas.grid(row=1, column=1, rowspan=6, columnspan=8, pady=4, stick="n")
scroll_canvas.grid_propagate(False)


field_frame = tk.Frame(scroll_canvas)
field_frame.grid(row=1,column=1, sticky="nwes")
field_frame.bind("<Configure>", lambda e:scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
scroll_canvas.create_window((0,0), window=field_frame,anchor="nw")


v_field = tk.Scrollbar(root, orient="vertical", bg="grey")
v_field.grid(row=1, rowspan=6,column=0, stick="nsw", pady=4)
v_field.config(command=scroll_canvas.yview)
scroll_canvas.config(yscrollcommand=v_field.set)
#2. table
scroll_table = Canvas(root, height="500", width="400", bg="whitesmoke")
scroll_table.grid(row=1, column=1, rowspan=6, columnspan=8, pady=4, stick="n")
scroll_table.grid_propagate(False)
scroll_table.grid_forget()

table_frame = tk.Frame(scroll_table, bg="whitesmoke")
table_frame.grid(row=1,column=1,sticky="nwes")
table_frame.bind("<Configure>", lambda e:scroll_table.configure(scrollregion=scroll_table.bbox("all")))
scroll_table.create_window((0,0), window=table_frame,anchor="nw")

coordinate_frame = tk.Frame(table_frame)
coordinate_frame.grid(row=0, column=0, padx=20, pady=20)

v_table = tk.Scrollbar(root, orient="vertical", bg="grey")
v_table.grid(row=1, rowspan=6,column=0, stick="nsw", pady=4)
v_table.grid_forget()
v_table.config(command=scroll_table.yview)
scroll_table.config(yscrollcommand=v_table.set)

h_table = tk.Scrollbar(root, orient="horizontal", bg="grey")
h_table.grid(row=6, column=1, columnspan=8, stick="sew", pady=4)
h_table.grid_forget()
h_table.config(command=scroll_table.xview)
scroll_table.config(xscrollcommand=h_table.set)
coordinates()

#3. graph 
graph_frame = tk.Frame(root, height="500", width="500", bg="silver")
graph_frame.grid(row=1, column=9, rowspan=6, columnspan=10, padx=5, pady=4)
graph_frame.grid_propagate(False)
#SET UP GRAPH -----
plt.style.use('_mpl-gallery')
fig,ax = plt.subplots()
fig = Figure(figsize=(5, 4.25))
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master = graph_frame)
canvas.get_tk_widget().grid(row=1, rowspan=5, column=1, columnspan=5)
canvas.get_tk_widget().bind("<Button-1>", OnDrag)
canvas.get_tk_widget().bind("<B1-Motion>", drag_graph)
canvas.get_tk_widget().bind("<ButtonRelease-1>", UpdateDrag)
canvas.get_tk_widget().grid_propagate(False)
toolbar=NavigationToolbar2Tk(canvas,graph_frame, pack_toolbar=False)
toolbar.update()
toolbar.grid(row=6, column=1, columnspan=5, pady=5, sticky="ew")

control_graph = tk.Frame(graph_frame, height=602, width=502, bg="whitesmoke", highlightbackground="grey", highlightthickness=2)
control_graph.grid(row=3, rowspan=3, column=3, columnspan=3)
SetGraph_Entries()

line_setting = tk.Frame(graph_frame, height=203, width=423, bg="whitesmoke", highlightbackground="grey", highlightthickness=3)
line_setting.grid(row=2, rowspan=3, column=2, columnspan=3)
line_setting.grid_propagate(False)
lineFrame()


    
#SAVE ------------
def ExportGraph():
    toolbar.save_figure()


#4. menubar
top_bar = tk.Frame(root, height="40", width="930", bg="dimgrey")
top_bar.grid(row=0, column=0, columnspan=19, sticky="new")
top_bar.grid_propagate(False)

error_message = tk.Label(root, text=" ",height="1", width="30", bg="dimgrey", font=("Arial", 12))
error_message.grid(row=0, column=18)

option_button = tk.Menubutton(top_bar, text="OPTION", width=7, font=("Arial",12,"bold"), bg="dimgrey", fg="white", relief="raised")
option_button.grid(row=0, rowspan=2, column=0, padx=5, pady=5)
option_menu = Menu(option_button, tearoff=0, bg="#e6e6e6", font=12)
option_menu.add_command(label="Clear Graph", command=clear)
option_menu.add_command(label="Open File", command=lambda: OpenCSV())
option_menu.add_separator()
option_menu.add_command(label="Export Graph", command=lambda: ExportGraph())
option_menu.add_command(label="Save Formula", command=lambda: StoreCSV())
option_button.config(menu=option_menu)



TGraph_button = tk.Menubutton(top_bar, text="EQUATION", width=10, font=("Arial",12, "bold"), bg="dimgrey", fg="white", relief="raised")
TGraph_button.grid(row=0, rowspan=2, column=1, padx=5, pady=5)
TGraph_menu = Menu(TGraph_button, tearoff=0, bg="#e6e6e6", font=12)
TGraph_menu.add_command(label="Table", command=ShowTable)
TGraph_button.config(menu=TGraph_menu)

unit = tk.StringVar()
unit.set("DEGREE")
unit_button = tk.Menubutton(top_bar, text="UNIT", width=5, font=("Arial",12, "bold"), bg="dimgrey", fg="white", relief="raised")
unit_button.grid(row=0, rowspan=2, column=2, padx=3, pady=5)
unit_menu = Menu(unit_button, tearoff=0, bg="#e6e6e6", font=12)
unit_menu.add_radiobutton(label="Radian", variable=unit, value="RADIAN", command=ChangeRadian)
unit_menu.add_radiobutton(label="Degree", variable=unit, value="DEGREE", command=ChangeDegree)
unit_button.config(menu=unit_menu)


Setting_button = tk.Button(top_bar, text="SETTING", command=SetGraph, width=7, font=("Arial", 12, "bold"), bg="dimgrey", fg="white")
Setting_button.grid(row=0, rowspan=2, column=3, padx=3, pady=5)

Symbol_button = tk.Button(top_bar, text="SYMBOL MENU", command=ActivateMenu, width=12, font=("Arial", 12, "bold"), bg="dimgrey", fg="white")
Symbol_button.grid(row=0, rowspan=2, column=4, padx=3, pady=5)

Intercept_button = tk.Menubutton(top_bar, text="INTERCEPTION", width=13, font=("Arial", 12, "bold"), bg="dimgrey", fg="white", relief="raised")
Intercept_button.grid(row=0, rowspan=2, column=5, padx=3, pady=5)
Intercept_button.bind("<Button-1>", lambda event: PlotIntercept())

fitLine = tk.StringVar()
fitLine.set("LINEAR")
bestFit_menu = Menu(Intercept_button, tearoff=0, font=10)
bestFit_menu.add_command(label="Y1", command= lambda: PlotFit("Y1"))
bestFit_menu.add_command(label="Y2", command= lambda: PlotFit("Y2"))
bestFit_menu.add_separator()
bestFit_menu.add_radiobutton(label="Linear", variable=fitLine, value="LINEAR")
bestFit_menu.add_radiobutton(label="Quadratic", variable=fitLine, value="QUADRATIC")
bestFit_menu.add_radiobutton(label="Cubic", variable=fitLine, value="CUBIC")
bestFit_menu.add_radiobutton(label="Exponential", variable=fitLine, value="EXPONENTIAL")
bestFit_menu.add_separator()
bestFit_menu.add_radiobutton(label="Scatter", variable=fitLine, value="SCATTER")


#Add To Calculation------
calculation = ""
value = ""
def AddValue(symbol):
    if page == "EQUATION":
        calculation = EntryField_list[locatOOP.get_locat()].get("1.0", tk.END).strip()
        calculation += symbol
        EntryField_list[locatOOP.get_locat()].delete(1.0, "end")
        EntryField_list[locatOOP.get_locat()].insert(1.0, calculation)
        GetEquation()
    elif page == "TABLE":
        if locatOOP.get_table() == "x":
            value = num_xvalues[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value += symbol
            num_xvalues[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_xvalues[locatOOP.get_tableLocate()].insert(1.0, value)
            GetCoordinate()
        elif locatOOP.get_table() == "y1":
            value = num_y1values[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value += symbol
            num_y1values[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_y1values[locatOOP.get_tableLocate()].insert(1.0, value)
            GetCoordinate()
        elif locatOOP.get_table() == "y2":
            value = num_y2values[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value += symbol
            num_y2values[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_y2values[locatOOP.get_tableLocate()].insert(1.0, value)
            GetCoordinate()

def DelValue():
    if page == "EQUATION":
        calculation = EntryField_list[locatOOP.get_locat()].get("1.0", tk.END).strip()
        if calculation[len(calculation)-4:len(calculation)] == "sin(" or calculation[len(calculation)-4:len(calculation)] == "cos(" or calculation[len(calculation)-4:len(calculation)] == "tan(":
            calculation = calculation[0:len(calculation)-4]
        elif calculation[len(calculation)-4:len(calculation)] == "f(x)" or calculation[len(calculation)-4:len(calculation)] == "g(x)" or calculation[len(calculation)-4:len(calculation)] == "h(x)":
            calculation = calculation[0:len(calculation)-4]
        elif calculation[len(calculation)-3:len(calculation)] == "ln(":
            calculation = calculation[0:len(calculation)-3]
        elif calculation[len(calculation)-4:len(calculation)] == "log(" or calculation[len(calculation)-4:len(calculation)] == "exp(":
            calculation = calculation[0:len(calculation)-4]
        else:
            calculation = calculation[0: len(calculation)-1]
        EntryField_list[locatOOP.get_locat()].delete(1.0, "end")
        EntryField_list[locatOOP.get_locat()].insert(1.0, calculation)
        GetEquation()
    elif page == "TABLE":
        if locatOOP.get_table() == "x":
            value = num_xvalues[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value = value[0:len(value)-1]
            num_xvalues[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_xvalues[locatOOP.get_tableLocate()].insert(1.0, value)
        elif locatOOP.get_table() == "y1":
            value = num_y1values[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value = value[0:len(value)-1]
            num_y1values[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_y1values[locatOOP.get_tableLocate()].insert(1.0, value)
        elif locatOOP.get_table() == "y2":
            value = num_y2values[locatOOP.get_tableLocate()].get("1.0", tk.END).strip()
            value = value[0:len(value)-1]
            num_y2values[locatOOP.get_tableLocate()].delete(1.0, "end")
            num_y2values[locatOOP.get_tableLocate()].insert(1.0, value)
        GetCoordinate()
        


def ClearValue():
    if page == "EQUATION":
        EntryField_list[locatOOP.get_locat()].delete(1.0,"end")
        GetEquation()
    elif page == "TABLE":
        if locatOOP.get_table() == "x":
            num_xvalues[locatOOP.get_tableLocate()].delete("1.0", "end")
        elif locatOOP.get_table() == "y1":
            num_y1values[locatOOP.get_tableLocate()].delete("1.0", "end")
        elif locatOOP.get_table() == "y2":
            num_y2values[locatOOP.get_tableLocate()].delete("1.0", "end")
        GetCoordinate()
        
        
    

#KeyBoard -------
Keyboard_Shading = tk.Frame(root, height="192", width="927", bg="grey43")
Keyboard_Shading.grid(row=6, rowspan=3, column=0, columnspan=20)
Keyboard_Shading.grid_propagate(False)
Keyboard_Canvas = tk.Frame(Keyboard_Shading, height="190", width="925", bg="#ebe7e6")
Keyboard_Canvas.grid(row=6, rowspan=3, column=0, columnspan=20, padx=2, pady=2)
Keyboard_Canvas.grid_propagate(False)
#Keyboard_Shading.grid_forget()

functions_frame = tk.Frame(Keyboard_Canvas, height="180", width="400", bg="#f0eae9")
functions_frame.grid(row=1, rowspan=4, column=1, columnspan=4, padx=5, pady=5)
functions_frame.grid_propagate(False)
numbers_frame = tk.Frame(Keyboard_Canvas, height="180", width="393", bg="#f0eae9")
numbers_frame.grid(row=1, rowspan=4, column=5, columnspan=3, padx=5, pady=5)
numbers_frame.grid_propagate(False)
general_frame = tk.Frame(Keyboard_Canvas, height="180", width="100", bg="#f0eae9")
general_frame.grid(row=1, rowspan=4, column=8, columnspan=3, padx=5, pady=5)
general_frame.grid_propagate(False)

btn_sin = tk.Button(functions_frame, text="sin", command=lambda: AddValue("sin("), height=2, width=10, font=("Arial",9))
btn_sin.grid(row=1,column=1)
btn_cos = tk.Button(functions_frame, text="cos", command=lambda: AddValue("cos("), height=2, width=10, font=("Arial",9))
btn_cos.grid(row=1,column=2)
btn_tan = tk.Button(functions_frame, text="tan", command=lambda: AddValue("tan("), height=2, width=10, font=("Arial",9))
btn_tan.grid(row=1,column=3)
btn_OB = tk.Button(functions_frame, text="(", command=lambda: AddValue("("), height=2, width=10, font=("Arial",9))
btn_OB.grid(row=1,column=4)
btn_CB = tk.Button(functions_frame, text=")", command=lambda: AddValue(")"), height=2, width=10, font=("Arial",9))
btn_CB.grid(row=1,column=5)

btn_fx = tk.Button(functions_frame, text="f(x)", command=lambda: AddValue("f(x)"), height=2, width=10, font=("Arial",9))
btn_fx.grid(row=2,column=1)
btn_gx = tk.Button(functions_frame, text="g(x)", command=lambda: AddValue("g(x)"), height=2, width=10, font=("Arial",9))
btn_gx.grid(row=2,column=2)
btn_hx = tk.Button(functions_frame, text="h(x)", command=lambda: AddValue("h(x)"), height=2, width=10, font=("Arial",9))
btn_hx.grid(row=2,column=3)
btn_x = tk.Button(functions_frame, text="x", command=lambda: AddValue("x"), height=2, width=10, font=("Arial",9))
btn_x.grid(row=2,column=4)
btn_y = tk.Button(functions_frame, text="y", command=lambda: AddValue("y"), height=2, width=10, font=("Arial",9))
btn_y.grid(row=2,column=5)

btn_exp = tk.Button(functions_frame, text="e", command=lambda: AddValue("exp("), height=2, width=10, font=("Arial",9))
btn_exp.grid(row=3,column=1)
btn_ln = tk.Button(functions_frame, text="ln(", command=lambda: AddValue("ln("), height=2, width=10, font=("Arial",9))
btn_ln.grid(row=3,column=2)
btn_e = tk.Button(functions_frame, text="E", command=lambda: AddValue("E"), height=2, width=10, font=("Arial",9))
btn_e.grid(row=3,column=3)
btn_log10 = tk.Button(functions_frame, text="log(", command=lambda: AddValue("log10("), height=2, width=10, font=("Arial",9))
btn_log10.grid(row=3,column=4)
btn_log = tk.Button(functions_frame, text="log□(", command=lambda: AddValue("log"), height=2, width=10, font=("Arial", 9)) 
btn_log.grid(row=3,column=5)
                    
btn_power = tk.Button(functions_frame, text="x^", command=lambda: AddValue("^"), height=2, width=10, font=("Arial",9))
btn_power.grid(row=4,column=1)
btn_square = tk.Button(functions_frame, text="x²", command=lambda: AddValue("^2"), height=2, width=10, font=("Arial",9))
btn_square.grid(row=4,column=2)
btn_cube = tk.Button(functions_frame, text="x³", command=lambda:AddValue("^3"), height=2, width=10, font=("Arial",9))
btn_cube.grid(row=4, column=3)
btn_abs = tk.Button(functions_frame, text="|x|", command=lambda:AddValue("|"), height=2, width=10, font=("Arial", 9))
btn_abs.grid(row=4, column=4)
btn_pi = tk.Button(functions_frame, text="π", command=lambda:AddValue("π"), height=2, width=10, font=("Arial", 9))
btn_pi.grid(row=4, column=5)
btn_blank = tk.Button(functions_frame, text="", height=1, width=130, font=("Arial",4))
btn_blank.grid(row=5, column=1, columnspan=5)
btn_blank.config(state=tk.DISABLED)

#²π

btn_7 = tk.Button(numbers_frame, text="7", command=lambda: AddValue("7"), height=2, width=11, font=("Arial",10))
btn_7.grid(row=1,column=1)
btn_8 = tk.Button(numbers_frame, text="8", command=lambda: AddValue("8"), height=2, width=11, font=("Arial",10))
btn_8.grid(row=1,column=2)
btn_9 = tk.Button(numbers_frame, text="9", command=lambda: AddValue("9"), height=2, width=11, font=("Arial",10))
btn_9.grid(row=1,column=3)
btn_4 = tk.Button(numbers_frame, text="4", command=lambda: AddValue("4"), height=2, width=11, font=("Arial",10))
btn_4.grid(row=2,column=1)
btn_5 = tk.Button(numbers_frame, text="5", command=lambda: AddValue("5"), height=2, width=11, font=("Arial",10))
btn_5.grid(row=2,column=2)
btn_6 = tk.Button(numbers_frame, text="6", command=lambda: AddValue("6"), height=2, width=11, font=("Arial",10))
btn_6.grid(row=2,column=3)
btn_1 = tk.Button(numbers_frame, text="1", command=lambda: AddValue("1"), height=2, width=11, font=("Arial",10))
btn_1.grid(row=3,column=1)
btn_2 = tk.Button(numbers_frame, text="2", command=lambda: AddValue("2"), height=2, width=11, font=("Arial",10))
btn_2.grid(row=3,column=2)
btn_3 = tk.Button(numbers_frame, text="3", command=lambda: AddValue("3"), height=2, width=11, font=("Arial",10))
btn_3.grid(row=3,column=3)
btn_0 = tk.Button(numbers_frame, text="0", command=lambda: AddValue("0"), height=2, width=11, font=("Arial",10))
btn_0.grid(row=4,column=1)
btn_dot = tk.Button(numbers_frame, text=".", command=lambda: AddValue("."), height=2, width=11, font=("Arial",10))
btn_dot.grid(row=4,column=2)
btn_equal = tk.Button(numbers_frame, text="=", command=lambda: AddValue("="), height=2, width=11, font=("Arial",10))
btn_equal.grid(row=4,column=3)

btn_divide = tk.Button(numbers_frame, text="÷", command=lambda: AddValue("/"), height=2, width=11, font=("Arial",10))
btn_divide.grid(row=1,column=4)
btn_times = tk.Button(numbers_frame, text="x", command=lambda: AddValue("*"), height=2, width=11, font=("Arial",10))
btn_times.grid(row=2,column=4)
btn_minus = tk.Button(numbers_frame, text="-", command=lambda: AddValue("-"), height=2, width=11, font=("Arial",10))
btn_minus.grid(row=3,column=4)
btn_add = tk.Button(numbers_frame, text="+", command=lambda: AddValue("+"), height=2, width=11, font=("Arial",10))
btn_add.grid(row=4,column=4)

btn_delete = tk.Button(general_frame, text="DEL", command=lambda:DelValue(), height=2, width=11, font=("Arial",10))
btn_delete.grid(row=1,column=1)
btn_clear = tk.Button(general_frame, text="CLEAR", command=lambda:ClearValue(), height=2, width=11, font=("Arial", 10))
btn_clear.grid(row=2, column=1)

btn_hide = tk.Button(general_frame, text="▼", command=lambda:HideKeyBoard(), height=2, width=11, font=("Arial", 10))
btn_hide.grid(row=4, column=1, pady=43)

btn_show = tk.Button(root, text="▲", command=lambda:ShowKeyBoard(), height=2, width=11, font=("Arial", 10))
btn_show.grid(row=6, column=18, columnspan=2, padx=12, pady=3, stick="es")
btn_show.grid_forget()


def HideKeyBoard():
    Keyboard_Shading.config(height="30")
    Keyboard_Shading.grid(row=6, column=0, columnspan=20,pady = 4, stick="s")
    btn_show.grid(row=6, column=18, columnspan=2, padx=12, pady=3, stick="es")

def ShowKeyBoard():
    Keyboard_Shading.config(height="192")
    Keyboard_Shading.grid(row=6, rowspan=3, column=0, columnspan=20)
    btn_show.grid_forget()
    


#ARRAY FOR EQUATION FIELDS ----
EntryField_list = ['1']
Appearance_field = ['1']
Appearance_num = ['1']
Colour_block = ['']
ColorSetting = ['']
Colour_list = ["#4f5f9c"]
Style_list = ["solid"]
Style_block = ['']
Style_choice = ['']
LineStyleSetting = ['']
Equation_list = ['']
Line_list = ['1']

#--------


InitialField()
InitialGraph()
root.mainloop()
