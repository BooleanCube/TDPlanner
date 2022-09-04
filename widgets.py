from tkinter import *


class SpacedListbox(Frame):
    def __init__(self, parent, ipady=10, font="Verdana 14", ):
        Frame.__init__(self, parent)
        self.parent = parent

        self.config(relief='sunken', bd=2)
        self.ipady = ipady
        self.font = font

    def display(self, items):
        for widget in self.winfo_children():
            widget.destroy()

        for item in items:
            label = Label(self, text=item, anchor='w', font=self.font)
            label.pack(ipady=self.ipady, fill='x')

#    def insert(self, index, *elements):
#        last = len(self.__item_list) - 1
#        if index == 'end':
#            index = last
#        elif index >= len(self.__item_list):
#            index = last
#        temp_lst = []
#        if index != last:
#            temp_lst = self.__item_list[index:]
#            self.__item_list = self.__item_list[:index]
#        for item in elements:
#            self.__item_list.append(item)
#        self.__item_list += temp_lst
#        self.__refresh_items()
