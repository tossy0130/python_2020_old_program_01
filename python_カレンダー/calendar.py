import jpbizday
import datetime
import calendar

class calWidget(tk.Frame):
    def __init__(self, master = None, cnf = {}, **kw):

        tk.Frame.__init__(self, master, cnf, **kw)

root = tk.Tk()
root.title("calendar")
root.geometry('600x400')

# 作成したウィジットを配置
widget = calWidget(root)
widget.pack()

root.mainloop()