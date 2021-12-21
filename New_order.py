import tkinter as tk
from tkinter import*
from tkinter import messagebox

import datetime as dt

import receipt

#       classes which will be show frame
import Return


# classes for some actions
import order_save
from shop_data import get_rate,get_totalItems
from validation import validate_number_of_items

LARGE_FONT = ("Verdana", 12)

class New_order(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # variables for grid
        self.y = ()
        self.row = 0

        #Customer Variables
        self.name = StringVar()
        self.addr = StringVar()
        self.phn = StringVar()
        self.issue_date = StringVar()

        #items A variable
        self.serhi = IntVar()
        self.eint = IntVar()
        self.tile = IntVar()
        self.mitti = IntVar()
        self.rait = IntVar()
        self.semant = IntVar()
        self.bajri = IntVar()

        # Items B variables
        self.items = {
            'electronic_vaibrator': ['وائیبریٹر بجلی والا',IntVar()],
            'grander': ['گرینڈر',IntVar()],
            'dril_machine': ['ڈرل مشین',IntVar()],
            'ghori_4ft': ['گھوڑی4فٹ',IntVar()],
            'ghori_5ft': ['گھوڑی5فٹ',IntVar()],
            'ghori_8ft': ['گھوڑی8فٹ',IntVar()],
            'ghori_10ft': ['گھوڑی10فٹ',IntVar()],
            'serhi_10ft': ['سیڑھی 10 تا 20 فٹ',IntVar()],
            'serhi_25ft': ['سیڑھی 25 اور 30 فٹ',IntVar()],
            'folding_serhi':['فولڈنگ سیڑھی',IntVar()],
            'folding_seat': ['فولڈنگ سیٹ',IntVar()],
            'large_lohaPlate': ['لوہاپلیٹ بڑی',IntVar()],
            'small_lohaPlate': ['لوہاپلیٹ چھوٹی',IntVar()],
            'hand_rerhi': ['ہاتھ ریڑھی',IntVar()],
            'demp_farma': ['ڈیمپ والا فرما',IntVar()],
            'phata_7ft': ['پھٹا7فٹ',IntVar()],
            'baly': ['بالے',IntVar()],
            'bans': ['بانس',IntVar()],
            'drum': ['ڈرم',IntVar()],
            'damosa': ['دموسہ',IntVar()],
            'karahi': ['کڑاہی',IntVar()],
            'belcha':['بیلچہ',IntVar()],
            'genti': ['گینتی',IntVar()],
            'kassi': ['کسسی',IntVar()],
            'panji': ['پنجی',IntVar()],
            'wadan': ['ودان',IntVar()],
            'cheni_hathora': ['چھینی ہتھوڑا',IntVar()],
        }
        # Rikshaw variables
        self.riksaw_number = [1,2,3]
        self.select_rikshaw = StringVar()
        self.select_rikshaw.set('rikshaw number')

        self.rikshaw_rent = IntVar()

        # controller.geometry("1650x800+0+40")
        controller.state("zoomed")
        controller.title("Mian building Material saria store")
        self.bg_color = "#074463"
        Label(self, text="میاں بلڈنگ میٹیریئل سریا سٹور", font=("times new roman", 30, "bold"),
                      bg=self.bg_color, fg="white", bd=12, relief=GROOVE, pady=2).pack(fill=X)
        # ---------------------------------------------- Menu ----------------------------------------
        self.menu(parent, controller)

        # ---------------------------------------------- Customer details Frame ----------------------------------------
        self.customer_details()
        # ---------------------------------------------- Items ----------------------------------------
        self.show_items_frame()

        #  ----------------------------------------------create Bill Buttun----------------------------------------

        Button(self, text="Create Bill", width=20, font="arial 12 bold", bd=7, bg="yellow",
               command=lambda: self.call_bill_area()).place(x=360, y=670)

        #  ----------------------------------------------Refresh Buttun----------------------------------------

        Button(self, text="Refresh", width=20, font="arial 12 bold", bd=7, bg="lightgreen",
               command=lambda: self.refresh()).place(x=30, y=670)

        # ---------------------------------------------- BILL area ----------------------------------------
        self.show_bill_area()
        # ---------------------------------------------- Print Buttun ----------------------------------------

        F_print = LabelFrame(self)
        F_print.place(x=670, y=670, width=250, height=50)

        Button(F_print, text="Save&Print Bill", width=23, font="arial 12 bold", bd=7, bg="Blue", fg="white",
               command=lambda: self.save_print_bill()).place(x=0, y=0)

    # -------------------------------- View Functions
    def menu(self, parent, controller):
        F_Buttuns = LabelFrame(self,
                               bg=self.bg_color, fg="gold", bd=10, relief=GROOVE)
        # F_Buttuns.place(x=0, y=80, relwidth=1)
        F_Buttuns.pack(fill=X)


        Button(F_Buttuns, text="Return", width=20, font="arial 12 bold", bd=7, bg="green",
               command=lambda: controller.show_frame(Return.Return)).grid(row=0, column=0, pady=10, padx=15)

    def customer_details(self):
        F_customerDetails = LabelFrame(self, text="Customer Details", font=("times new roman", 15, "bold"),
                                       bg=self.bg_color, fg="gold", bd=10, relief=GROOVE)
        # F_customerDetails.place(x=0, y=170, relwidth=1)
        F_customerDetails.pack(fill=X)


        # Name Label
        customerDetails_cName_lable = Label(F_customerDetails, text="Customer Name",
                                            font=("times new roman", 12, "bold"), bg=self.bg_color, fg="white")
        customerDetails_cName_lable.grid(row=0, column=0, padx=20, pady=5, sticky=SW)

        # Name text
        customerDetails_cName_text = Entry(F_customerDetails, textvariable=self.name, width=20, font="arial 15", bd=1,
                                           relief=SUNKEN, justify='center')
        customerDetails_cName_text.grid(row=0, column=1, pady=5, sticky=SW)

        # phn Label
        customerDetails_cPhn_lable = Label(F_customerDetails, text="Customer Contact",
                                           font=("times new roman", 12, "bold"), bg=self.bg_color, fg="white")
        customerDetails_cPhn_lable.grid(row=0, column=2, padx=20, pady=5, sticky=SW)

        # phn text
        customerDetails_cPhn_text = Entry(F_customerDetails, textvariable=self.phn, width=15, font="arial 15", bd=1,
                                          relief=SUNKEN,justify='center')
        customerDetails_cPhn_text.grid(row=0, column=3, pady=5, sticky=SW)

        # issue DateField Label
        customerDetails_issuedate_lable = Label(F_customerDetails, text="Issue Date",
                                                font=("times new roman", 15, "bold"), bg=self.bg_color, fg="white")
        customerDetails_issuedate_lable.grid(row=0, column=4, padx=20, pady=5, sticky=SW)

        date = dt.datetime.now()

        # Format the date
        format_date = f"{date:%a, %b %d %Y}"

        # Display the date in a a label widget
        entry = Entry(F_customerDetails, textvariable=self.issue_date, width=15, font=("Calibri", 15))
        entry.insert(END, format_date)
        entry.grid(row=0, column=7, pady=5, sticky=SW)

        # rikshaw details
        rikshaw_number = OptionMenu(F_customerDetails, self.select_rikshaw, *self.riksaw_number)
        rikshaw_number.grid(row=1, column=0,padx=20, pady=5, sticky=SW)
        rikshaw_number.config(bg=self.bg_color, fg="WHITE", font=("times new roman", 15, "bold"), relief=GROOVE)
        rikshaw_number["menu"].config(bg=self.bg_color,fg="WHITE",font=("times new roman", 15, "bold"))

        rikshaw_rent = Entry(F_customerDetails, textvariable=self.rikshaw_rent, width=15, font="arial 15", bd=1,
                                          relief=SUNKEN, justify='center')
        rikshaw_rent.grid(row=1, column=1, pady=2, sticky=SW)


    def canvas_frame(self):
        # canvas use for scrollbar area
        self.canvas = Canvas(self.F_items, bg=self.bg_color)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.F_items, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = Frame(self.canvas, bg=self.bg_color)

        self.scrollbar.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind("<Enter>", self._bound_mousewheel)
        self.canvas.bind("<Leave>", self._unbound_mousewheel)

        # ------------ show items headings

    def show_items_frame(self):
        self.F_items = LabelFrame(self, text="Items", font=("times new roman", 25, "bold"), bg=self.bg_color, fg="gold",
                             bd=10, relief=GROOVE)
        self.F_items.place(x=0, y=290, width=580, height=380)

        self.canvas_frame()

        # items_heading frame

        Frame(self.F_items).place(x=5, y=5, width=530, height=30)

        Label(self.F_items, text="items", font="arial 15 bold", ).place(x=70, y=5)
        Label(self.F_items, text="require", font="arial 15 bold", ).place(x=230, y=5)
        Label(self.F_items, text="rate", font="arial 15 bold", ).place(x=350, y=5)
        Label(self.F_items, text="total", font="arial 15 bold", ).place(x=460, y=5)

        self.show_items()

    def show_items(self):
        self.row = 0
        # -----------items_details
        for item in self.items:
            a = item
            if self.row == 0:
                self.y = (40, 0)
            else:
                self.y = (10, 0)
            Label(self.scrollable_frame, text=self.items[item][0], font=("", 15, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=self.row, column=0, padx=(20, 0), pady=self.y, sticky=SW)
            a = Entry(self.scrollable_frame, textvariable=self.items[item][1], width=5, font="arial 12", bd=1, relief=SUNKEN,
                      justify='center')
            a.grid(row=self.row, column=1, padx=(60, 0), pady=self.y, sticky=SW)
            Label(self.scrollable_frame, text=get_rate(item), font=("", 15, "bold"), bg=self.bg_color, fg="lightgreen").grid(
                row=self.row, column=2, padx=(60, 0), pady=self.y, sticky=SW)
            Label(self.scrollable_frame, text=get_totalItems(item), font=("", 15, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=self.row, column=3, padx=(70, 0), pady=self.y, sticky=SW)

            a.bind('<KeyRelease>',
                   lambda e, item_name=item, total_number_of_item=get_totalItems(item): self.check_validate(e, item_name,
                                                                                                       total_number_of_item))

            self.row = self.row + 1

    def show_bill_area(self):
        F_bill = Frame(self, bd=10, relief=GROOVE)
        F_bill.place(x=600, y=290, width=480, height=380)

        Label(F_bill, text="Bill", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        # scroll bar in bill area
        scrol_y = Scrollbar(F_bill, orient=VERTICAL)
        self.textarea = Text(F_bill, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        self.write_bill_area()

    def write_bill_area(self):
        self.textarea.configure(state="normal")
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t    میاں بلڈنگ میٹیریئل سریا سٹور")
        self.textarea.insert(END, f"\n\n Customer Name: {self.name.get()}")
        self.textarea.insert(END, f"\n Contact Number: {self.phn.get()}")
        self.textarea.insert(END, f"\n Address: {self.addr.get()}")
        self.textarea.insert(END, f"\n issue date: {self.issue_date.get()}")

        self.textarea.insert(END, "\n=====================================================")
        self.textarea.insert(END, "\n\tمال\t\tنگ\tدر")
        self.textarea.insert(END, "\n=====================================================")

        for i in self.items.keys():
            if self.items[i][1].get() != 0:
                self.textarea.insert(END,f"\n{self.items[i][0]}\t\t\t {self.items[i][1].get()}\t {get_rate(i)}")
                # print(self.items[i][1].get(),' ',self.items[i][0])

        self.textarea.configure(state="disable")

    #     ----------------------------call able functions

    def check_validate(self,e, item_name, total_number_of_item):
        # e.char
        number_of_require_item = self.items[item_name][1].get()
        if not validate_number_of_items(number_of_require_item, total_number_of_item):
            messagebox.showerror('Invalid Values', 'Error: \n' + 'you have ' + str(
                total_number_of_item) + ' ' + item_name + '\n' + 'you enter ' + str(number_of_require_item))
            self.items[item_name][1] = IntVar()

            self.scrollable_frame.destroy()
            self.scrollable_frame = Frame(self.canvas, bg=self.bg_color)
            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            self.show_items()

            # importlib.reload(sys.modules.get(self.show_items()))

        return

    def check_values(self):
        bool = False
        for item in self.items:
            if self.items[item][1].get() > 0:
                bool = True

        if self.name.get() == '':
            messagebox.showerror('Invalid Name', 'Error: \n' + 'Please Enter Customer Name')
            return False
        elif self.phn.get() == '':
            messagebox.showerror('Invalid contact', 'Error: \n' + 'Please Enter Customer Contact')
            return False
        elif bool == False:
            messagebox.showerror('Empty Record', 'Error: \n' + 'You have Empty record')
            return False
        else:
            return True
            # self.bill_area()

    def call_bill_area(self):
        if (self.check_values()):
            self.write_bill_area()
        return

    def save_print_bill(self):
        receipt.prnt(self.textarea.get('1.0', 'end-1c'))  # printing function

        if (self.check_values()):
            order_save.Order(self.name.get(),self.phn.get(),self.issue_date.get(), self.items).save_data()
            self.items = {
                'electronic_vaibrator': ['وائیبریٹر بجلی والا', IntVar()],
                'grander': ['گرینڈر', IntVar()],
                'dril_machine': ['ڈرل مشین', IntVar()],
                'ghori_4ft': ['گھوڑی4فٹ', IntVar()],
                'ghori_5ft': ['گھوڑی5فٹ', IntVar()],
                'ghori_8ft': ['گھوڑی8فٹ', IntVar()],
                'ghori_10ft': ['گھوڑی10فٹ', IntVar()],
                'serhi_10ft': ['سیڑھی 10 تا 20 فٹ', IntVar()],
                'serhi_25ft': ['سیڑھی 25 اور 30 فٹ', IntVar()],
                'folding_serhi': ['فولڈنگ سیڑھی', IntVar()],
                'folding_seat': ['فولڈنگ سیٹ', IntVar()],
                'large_lohaPlate': ['لوہاپلیٹ بڑی', IntVar()],
                'small_lohaPlate': ['لوہاپلیٹ چھوٹی', IntVar()],
                'hand_rerhi': ['ہاتھ ریڑھی', IntVar()],
                'demp_farma': ['ڈیمپ والا فرما', IntVar()],
                'phata_7ft': ['پھٹا7فٹ', IntVar()],
                'baly': ['بالے', IntVar()],
                'bans': ['بانس', IntVar()],
                'drum': ['ڈرم', IntVar()],
                'damosa': ['دموسہ', IntVar()],
                'karahi': ['کڑاہی', IntVar()],
                'belcha': ['بیلچہ', IntVar()],
                'genti': ['گینتی', IntVar()],
                'kassi': ['کسسی', IntVar()],
                'panji': ['پنجی', IntVar()],
                'wadan': ['ودان', IntVar()],
                'cheni_hathora': ['چھینی ہتھوڑا', IntVar()],
            }
            self.refresh()

        return

# ------------------- mouse  fucntions
    def _bound_mousewheel(self,eve):
        self.canvas.bind_all("<MouseWheel>",self.__move)

    def _unbound_mousewheel(self,eve):
        self.canvas.unbind_all("<MouseWheel>")

    def __move(self,event):
        self.canvas.yview_scroll(int(-1*(event.delta/ 120)), "units")

    def refresh(self):
        self.scrollable_frame.destroy()
        self.scrollable_frame = Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.show_items()



