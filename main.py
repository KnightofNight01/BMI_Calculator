import tkinter

result_label = None

def BMI_Calculator():
    try:
        kilo = float(user_kilo_entry.get())
        boy = float(user_boy_entry.get())
        bmi = kilo / (boy * boy)
        result_label = tkinter.Label(window_01, text=bmi)
        result_label.grid(row=6, column=3)
        if bmi < 18.5:
            kilo_label = tkinter.Label(window_01, text="Sıska")
            kilo_label.grid(row=7, column=3)
        elif bmi >= 18.5 and bmi <= 24.9:
            kilo_label = tkinter.Label(window_01, text="kafi")
            kilo_label.grid(row=7, column=3)
        elif bmi >= 25 and bmi <= 29.9:
            kilo_label = tkinter.Label(window_01, text="hop dikkat et")
            kilo_label.grid(row=7, column=3)
        elif bmi >= 30 and bmi <= 34.9:
            kilo_label = tkinter.Label(window_01, text="hala kurtarabilirsin")
            kilo_label.grid(row=7, column=3)
        else:
            kilo_label = tkinter.Label(window_01, text="sana noldu yaww")
            kilo_label.grid(row=7, column=3)

    except ValueError:
        except_value=tkinter.Label(text="Sayı gir plsss.")
        except_value.grid(row=8, column=3)






window_01 = tkinter.Tk()
window_01.title("BMI Calculator")
window_01.minsize(width=300,height=300)

#labels
enter_kilo = tkinter.Label(text="Kilonuzu Girin (kg):")
enter_kilo.grid(row=0,column=3)
enter_boy = tkinter.Label(text="Boyunuzu Girin (m):")
enter_boy.grid(row=2,column=3)
#entries
user_kilo_entry = tkinter.Entry(window_01)
user_kilo_entry.grid(row=1,column=3)
user_boy_entry = tkinter.Entry(window_01)
user_boy_entry.grid(row=4,column=3)

#buton
button_01 = tkinter.Button(window_01, text="calculate", command=BMI_Calculator)
button_01.grid(row=5,column=3)



#gelişebilir


window_01.mainloop()