#!/usr/bin/env python3

import tkinter.ttk

from tkinter import *
from matplotlib import style as ppstyle
from matplotlib import pyplot as plt

import taskmanager
from taskmanager import TaskList


class Application:

    def __init__(self, root):
        self.task_box = None
        self.tasks = TaskList()
        self.setup_dark_theme(root)
        self.setup_window(root)
        self.setup_layout()

    @staticmethod
    def setup_dark_theme(root):
        ppstyle.use('dark_background')
        tkstyle = tkinter.ttk.Style(root)
        root.tk.call('source', 'darktheme/azuredark.tcl')
        tkstyle.theme_use('azure')
        tkstyle.configure("Accentbutton", foreground='white')
        tkstyle.configure("Togglebutton", foreground='white')
        # tkstyle.configure("ListBox", foreground='white')
        return tkstyle

    @staticmethod
    def setup_window(root):
        root.title("TDPlanner - BooleanCube")
        window_width = 1200
        window_height = 800
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.resizable(False, False)

    def open_graph_window(self):
        plt.title = "Tasks Graph"
        plt.rc('font', size=14)
        plt.xlabel("Urgence")
        plt.ylabel("Importance")
        x = [t.urgence for t in self.tasks.task_list]
        y = [t.importance for t in self.tasks.task_list]
        plt.plot(x, y, 'ro')
        plt.grid()
        plt.show()

    def refresh_box(self):
        self.task_box.delete(0, END)
        for task in self.tasks.task_list:
            self.task_box.insert(END, f'{task.name} ({task.urgence},{task.importance})')

    def add_task(self, name, importance, urgence, window):
        self.tasks.add_task(name, importance, urgence)
        self.refresh_box()
        window.destroy()

    def open_add_window(self):
        add_window = Toplevel(root)
        add_window.title("Add Task")
        add_window.geometry("700x275")
        add_window.resizable(False, False)

        name_label = Label(add_window, text="Task Name: ", font="Verdana 14")
        name_label.place(x=30, y=30)
        task_name = Entry(add_window, width=50)
        task_name.insert(0, "Brief Description of Task")
        task_name.place(x=240, y=33)

        importance_label = Label(add_window, text="Importance Value: ", font="Verdana 14")
        importance_label.place(x=30, y=90)
        importance_value = IntVar(value=5)
        importance_slider = Scale(add_window, from_=0, to=10, orient='horizontal', variable=importance_value)
        importance_slider.place(x=240, y=75, width=408)

        urgence_label = Label(add_window, text="Urgence Value: ", font="Verdana 14")
        urgence_label.place(x=30, y=150)
        urgence_value = IntVar(value=5)
        urgence_slider = Scale(add_window, from_=0, to=10, orient='horizontal', variable=urgence_value)
        urgence_slider.place(x=240, y=133, width=408)

        ok_button = Button(add_window, command=lambda: self.add_task(task_name.get(), importance_value.get(),
                                                                     urgence_value.get(), add_window), text="Ok")
        ok_button.place(x=600, y=220)

    def reset_tasks(self, window):
        self.tasks.clear_tasks()
        self.refresh_box()
        window.destroy()

    def open_reset_window(self):
        reset_window = Toplevel(root)
        reset_window.title("Reset Tasks")
        reset_window.geometry("520x115")
        reset_window.resizable(False, False)
        reset_window.anchor("center")
        confirmation_text = Label(reset_window, font="Verdana 16 bold",
                                  text="Are you sure you want to reset all "
                                       "tasks?\n*This can not be undone!*")
        yes_button = Button(reset_window, command=lambda: self.reset_tasks(reset_window), text="Yes")
        confirmation_text.pack()
        Label(reset_window, text="").pack()
        yes_button.pack()

    def update_sort_importance(self, value):
        taskmanager.importance_weight = float(value)
        self.tasks.task_list.sort(reverse=True)
        self.refresh_box()

    def update_sort_urgence(self, value):
        taskmanager.urgence_weight = float(value)
        self.tasks.task_list.sort(reverse=True)
        self.refresh_box()

    def complete_task(self):
        if len(self.task_box.curselection()) < 1:
            return
        idx = self.task_box.curselection()[0]
        tid = self.tasks.task_list[idx].tid
        self.tasks.remove_task(tid)
        self.refresh_box()

    def setup_layout(self):
        todo_label = Label(root, text="To Do List:", font="Verdana 38 bold")
        todo_label.place(x=200, y=40)

        # task_box = SpacedListbox(root)
        # task_box.place(x=125, y=120, width=450, height=500)
        self.task_box = Listbox(root, selectmode=SINGLE, font="Verdana 16")
        self.task_box.place(x=125, y=120, width=450, height=500)
        scrollbar = Scrollbar(root)
        scrollbar.place(x=575, y=120, height=500)
        self.task_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_box.yview)
        add_button = Button(root, command=self.open_add_window, text="Add Task", width=14, height=2)
        add_button.place(x=125, y=650)
        complete_button = Button(root, text="Mark As Complete", width=16, height=2,
                                 command=lambda: self.complete_task())
        complete_button.place(x=280, y=650)
        reset_button = Button(root, command=self.open_reset_window, text="Reset Tasks", width=14, height=2)
        reset_button.place(x=450, y=650)

        settings_label = Label(root, text="Weightage Settings\n~~~~~~~~~~~~~~~~~", font="Verdana 26 bold")
        settings_label.place(x=650, y=150)
        importance_weight = DoubleVar(value=1.0)
        urgence_weight = DoubleVar(value=1.0)
        importance_label = Label(root, text="Importance Value Weightage: ", font="Verdana 16")
        importance_label.place(x=725, y=300)
        importance_slider = Scale(root, from_=0.0, to=1.0, orient='horizontal', variable=importance_weight,
                                  resolution=0.1,
                                  command=lambda val: self.update_sort_importance(val))
        importance_slider.place(x=725, y=330, width=340)
        urgence_label = Label(root, text="Urgence Value Weightage: ", font="Verdana 16")
        urgence_label.place(x=725, y=400)
        urgence_slider = Scale(root, from_=0.0, to=1.0, orient='horizontal', variable=urgence_weight,
                               resolution=0.1, command=lambda val: self.update_sort_urgence(val))
        urgence_slider.place(x=725, y=430, width=340)

        graph_button = Button(root, command=self.open_graph_window, text="Show Graph", width=12, height=2)
        graph_button.place(x=950, y=650)

        version_label = Label(root, text="v1.0.0", font="Verdana 8")
        version_label.place(x=1155, y=780)

        self.refresh_box()


root = Tk()
app = Application(root)

root.mainloop()
