import tkinter as tk
import math
import sympy as sp

calculation = ""
answer = 0

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_entry.delete(1.0, "end") #delete content of the textresult field
    text_entry.insert(1.0, calculation) #print content of the equation 
    

def evaluate_calculation():
    global calculation
    global answer
    try:
        expr = sp.sympify(calculation)
        answer = sp.N(expr, 5)
        text_result.delete(1.0, "end") #delete content 
        text_result.insert(1.0, f"Answer = {answer}") #print result
        calculation = ""
    except:
        clear_field() #if no result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "Error*") #print error
        

def clear_field():
    global calculation
    calculation = ""
    text_entry.delete(1.0, "end")

def delete():
    global calculation
    calculation = calculation[0: len(calculation)-1]
    text_entry.delete(1.0, "end")
    text_entry.insert(1.0, calculation)

def get_answer():
    global answer
    add_to_calculation(answer)

def squarert():
    global calculation
    global answer
    answer = round(math.sqrt(answer),5)
    calculation += str(answer)
    text_entry.delete(1.0, "end")
    text_entry.insert(1.0, calculation)

def pi():
    add_to_calculation(sp.pi)
    

#input
#create the object
root = tk.Tk()
root.title("GUI Calculator")

#The tab size (X,Y)
root.geometry("325x350")
#The field show execution
text_entry = tk.Text(root, height=2, width=18,font=("Arial", 24))
text_entry.grid(columnspan=30)
text_result = tk.Text(root, height=1, width=18,font=("Arial", 24))
text_result.grid(columnspan=30)

#numbers' button
#command, the thing it does when press the button
#with lambda, it wont immediately call the function
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Airal",14))
btn_1.grid(row=4, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Airal",14))
btn_2.grid(row=5, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Airal",14))
btn_3.grid(row=5, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Airal",14))
btn_4.grid(row=5, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Airal",14))
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Airal",14))
btn_6.grid(row=4, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Airal",14))
btn_7.grid(row=3, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Airal",14))
btn_8.grid(row=3, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Airal",14))
btn_9.grid(row=3, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Airal",14))
btn_0.grid(row=6, column=1)
btn_pt = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial",14))
btn_pt.grid(row=6, column=2)

#operators' button
btn_times = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Airal",14))
btn_times.grid(row=3, column=4)
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Airal",14))
btn_div.grid(row=3, column=5)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Airal",14))
btn_plus.grid(row=4, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Airal",14))
btn_minus.grid(row=4, column=5)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Airal",14))
btn_open.grid(row=2, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Airal",14))
btn_close.grid(row=2, column=2)
btn_poly= tk.Button(root, text="^", command=lambda: add_to_calculation("^"), width=5, font=("Airal",14))
btn_poly.grid(row=5, column=4)
btn_exp = tk.Button(root, text="e", command=lambda: add_to_calculation("2.718281828459045"), width=5, font=("Airal",14))
btn_exp.grid(row=5, column=5)
btn_10 = tk.Button(root, text="x10^", command=lambda: add_to_calculation("E"), width=5, font=("Airal",14))
btn_10.grid(row=6, column=3)
btn_pie = tk.Button(root, text="π", command=lambda: pi(), width=5, font=("Airal",14))
btn_pie.grid(row=2, column=3)

btn_clear = tk.Button(root, text="DEL", command=clear_field, height=1, width=5, font=("Airal",14))
btn_clear.grid(row=2, column=4)
btn_equals = tk.Button(root, text="=", command=lambda: evaluate_calculation(), height=1, width=5, font=("Airal",14))
btn_equals.grid(row=6, column=5)
btn_ans = tk.Button(root, text="ANS", command=lambda: get_answer(), height=1, width=5, font=("Airal",14))
btn_ans.grid(row=6, column=4)
btn_ac = tk.Button(root, text="AC", command=lambda:delete(), width=5, font=("Airal",14))
btn_ac.grid(row=2, column=5)

                        
#input
#run the main loop
root.mainloop()

