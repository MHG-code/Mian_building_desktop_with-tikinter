import tkinter as tk
from tkinter import*
from tkinter import messagebox

import datetime as dt
from datetime import datetime
import New_order
from orders import Orders

import receipt


from validation import validate_number_of_items
from shop_data import get_rate


class Return(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.bg_color = "#074463"
        self.y = ()

        self.name = StringVar()

        self.orders = []

        self.current_date = dt.datetime.now()
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

        Label(self, text="میاں بلڈنگ میٹیریئل سریا سٹور", font=("times new roman", 30, "bold"),
                      bg=self.bg_color, fg="white", bd=12, relief=GROOVE, pady=2).pack(fill=X)

        # ---------------------------------------------- Menu ----------------------------------------
        self.menu(parent, controller)

        # ---------------------------------------------- Customer searching Details ----------------------------------------
        self.customer_searching_details()

        # ---------------------------------------------- all customers ----------------------------------------
        self.all_customers_frame()

        # ---------------------------------------------- customer Record ----------------------------------------

        self.customer_details_frame()

        # self.show_bill_area()

        # ---------------------------------------------- refresh function ----------------------------------------

        self.refresh_page()
# ---------------------------------------------- View Functions ----------------------------------------

    def menu(self, parent, controller):
        F_Buttuns = LabelFrame(self,
                               bg=self.bg_color, fg="gold", bd=10, relief=GROOVE)
        F_Buttuns.place(x=0, y=80, relwidth=1)

        Button(F_Buttuns, text="New Order", width=20, font="arial 12 bold", bd=7,
               command=lambda: controller.show_frame(New_order.New_order)).grid(row=0, column=0, pady=10)

    def customer_searching_details(self):
        F_customerDetails = LabelFrame(self, text="Customer Details", font=("times new roman", 15, "bold"),
                                       bg=self.bg_color, fg="gold", bd=10, relief=GROOVE)
        F_customerDetails.place(x=0, y=170, relwidth=1)

        # Name Label

        customerDetails_cName_lable = Label(F_customerDetails, text="Customer Name",
                                            font=("times new roman", 15, "bold"), bg=self.bg_color, fg="white")
        customerDetails_cName_lable.grid(row=0, column=0, padx=20, pady=5)
        # Name text
        customerDetails_cName_text = Entry(F_customerDetails, textvariable=self.name, width=20, font="arial 15", bd=1,
                                           relief=SUNKEN, justify='center')
        customerDetails_cName_text.grid(row=0, column=1, pady=5)

        customerDetails_cName_text.bind('<KeyRelease>', self.searching_customer)

    def all_customers_frame(self):

        self.F_Orders = LabelFrame(self, text="All Returners", font=("times new roman", 25, "bold"), bg=self.bg_color,
                                   fg="gold", bd=10,
                                   relief=GROOVE)
        self.F_Orders.place(x=0, y=250, width=580, height=380)

        self.customer_canvas_frame()
        # heading frame

        Frame(self.F_Orders).place(x=5, y=5, width=530, height=30)

        Label(self.F_Orders, text="Name", font="arial 15 bold", ).place(x=30, y=5)
        Label(self.F_Orders, text="Contact", font="arial 15 bold", ).place(x=180, y=5)
        Label(self.F_Orders, text="issue_date", font="arial 15 bold", ).place(x=300, y=5)

        self.show_all_customers()
        pass

    def show_all_customers(self):
        row = 0

        self.orders = Orders().all_orders()

        self.orders_scrollable_frame = Frame(self.Orders_canvas, bg=self.bg_color)
        self.Orders_canvas.create_window((0, 0), window=self.orders_scrollable_frame, anchor="nw")

        # creat empty item details for set layout
        Label(self.orders_scrollable_frame, text='                               ', font=("", 13, "bold"),
              bg=self.bg_color,
              fg="lightgreen").grid(row=0, column=0, padx=(0, 0), pady=(60, 0), sticky=SW)

        #     items_details
        for i in range(len(self.orders)):
            row = row + 1
            self.y = (10, 0)

            Label(self.orders_scrollable_frame, text=self.orders[i]['Name'], font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=0, padx=(0, 0), pady=self.y, sticky=SW)
            Label(self.orders_scrollable_frame, text="03004901080", font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=1, padx=(10, 0), pady=self.y, sticky=SW)
            Label(self.orders_scrollable_frame, text="7/10/2021", font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=2, padx=(30, 0), pady=self.y, sticky=SW)
            Button(self.orders_scrollable_frame, text='View', width=5, font="arial 12 bold",
                   command=lambda data=self.orders[i]: self.show_customer_details(data)).grid(row=i, column=3,
                                                                                              padx=(70, 0), pady=self.y,
                                                                                              sticky=SW)
        pass

    def searching_customer(self,e):
        row = 0
        if self.orders_scrollable_frame:
            self.orders_scrollable_frame.destroy()
        # heading frame
        self.orders = Orders().search_by_name(self.name.get())
        self.orders_scrollable_frame = Frame(self.Orders_canvas, bg=self.bg_color)
        self.Orders_canvas.create_window((0, 0), window=self.orders_scrollable_frame, anchor="nw")

        # creat empty item details for set layout
        Label(self.orders_scrollable_frame, text='                               ', font=("", 13, "bold"),
              bg=self.bg_color,
              fg="lightgreen").grid(row=0, column=0, padx=(0, 0), pady=(60, 0), sticky=SW)

        #     items_details
        for i in range(len(self.orders)):
            row = row + 1
            self.y = (10, 0)

            Label(self.orders_scrollable_frame, text=self.orders[i]['Name'], font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=0, padx=(0, 0), pady=self.y, sticky=SW)
            Label(self.orders_scrollable_frame, text="03004901080", font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=1, padx=(10, 0), pady=self.y, sticky=SW)
            Label(self.orders_scrollable_frame, text="7/10/2021", font=("", 13, "bold"), bg=self.bg_color,
                  fg="lightgreen").grid(row=i, column=2, padx=(30, 0), pady=self.y, sticky=SW)
            Button(self.orders_scrollable_frame, text='View', width=5, font="arial 12 bold",
                   command=lambda data=self.orders[i]: self.show_customer_details(data)).grid(row=i, column=3,
                                                                                              padx=(70, 0), pady=self.y,
                                                                                              sticky=SW)
        pass

    def customer_details_frame(self):
        self.F_details = LabelFrame(self, text="customer_record", font=("times new roman", 25, "bold"), bg=self.bg_color,
                               fg="gold", bd=10, relief=GROOVE)
        self.F_details.place(x=590, y=250, width=550, height=380)

        self.details_canvas_frame()
        # items_heading frame
        Frame(self.F_details).place(x=100, y=5, width=300, height=30)
        self.details_customerName = Label(self.F_details, text="", font="arial 15 bold", )
        self.details_customerName.place(x=100, y=5)

        self.issue_date = Label(self.F_details, text="issue date", font="arial 15 bold", )
        self.issue_date.place(x=10, y=50)

        self.total_days = Label(self.F_details, text="total days", font="arial 15 bold", )
        self.total_days.place(x=300, y=50)

        Frame(self.F_details).place(x=5, y=90, width=500, height=30)

        Label(self.F_details, text="items", font="arial 15 bold", ).place(x=70, y=90)
        Label(self.F_details, text="reserve", font="arial 15 bold", ).place(x=230, y=90)
        Label(self.F_details, text="return", font="arial 15 bold", ).place(x=330, y=90)
        Label(self.F_details, text="rent", font="arial 15 bold", ).place(x=420, y=90)

    def show_customer_details(self,data):
        if self.details_scrollable_frame:
            self.details_scrollable_frame.destroy()
        if self.details_customerName:
            self.details_customerName.destroy()
        if self.issue_date:
            self.issue_date.destroy()
        if self.total_days:
            self.total_days.destroy()
        row = 0

        data = Orders().show_items(data)  # collect all items

        self.details_customerName = Label(self.F_details, text=data['Name'], font="arial 15 bold", )
        self.details_customerName.place(x=230, y=5)

        self.issue_date = Label(self.F_details, text=data['issue_date'], font="arial 15 bold", )
        self.issue_date.place(x=10, y=50)

        self.total_days = Label(self.F_details, text=self.get_total_days(data['issue_date']), font="arial 15 bold", )
        self.total_days.place(x=300, y=50)

        self.details_scrollable_frame = Frame(self.details_canvas, bg=self.bg_color)
        self.details_canvas.create_window((0, 0), window=self.details_scrollable_frame, anchor="nw")

        Label(self.details_scrollable_frame, text='                         ', font=("", 15, "bold"), bg=self.bg_color,
              fg="lightgreen").grid(row=row, column=0, padx=(20, 0), pady=(90, 0), sticky=SW)

        # ---------------------------------------------- Items ----------------------------------------
        for item in data.keys():
            if item != 'Name' and item != 'contact' and item != 'address' and item != 'issue_date' and item != 'unique_id' and item != 'status':
                a = item
                row = row + 1
                self.y = (8, 0)

                Label(self.details_scrollable_frame, text=self.items[item][0], font=("", 15, "bold"), bg=self.bg_color,
                      fg="lightgreen").grid(row=row, column=0, padx=(20, 0), pady=self.y, sticky=SW)

                Label(self.details_scrollable_frame, text=data[item], font=("", 12, "bold"), bg=self.bg_color,
                      fg="lightgreen").grid(row=row, column=1, padx=(70, 0), pady=self.y, sticky=SW)

                a = Entry(self.details_scrollable_frame, textvariable=self.items[item][1], width=5, font="arial 12", bd=1,
                      relief=SUNKEN,
                      justify='center')
                a.grid(row=row, column=2, padx=(65, 0), pady=self.y, sticky=SW)

                Label(self.details_scrollable_frame, text=self.calculation_rent(item,data[item],self.get_total_days(data['issue_date'])), font=("", 12, "bold"), bg=self.bg_color,
                      fg="lightgreen").grid(row=row, column=3, padx=(60, 0), pady=self.y, sticky=SW)

                a.bind('<KeyRelease>',
                       lambda e, item_name=item, total_number_of_item=data[item]: self.check_validate(e,
                                                                                                                item_name,
                                                                                                                total_number_of_item))

                row = row + 1
        # ---------------------------------------------- Update buttun ----------------------------------------


        Button(self, text="create bill", width=25, font="arial 15 bold", bd=7, bg='red',
               command = lambda : self.show_bill_area(data)).place(x=720, y=630)

    def show_bill_area(self,data=None):
        bill = Tk()
        bill.title("bill")

        F_bill = Frame(bill, bd=10, relief=GROOVE)
        # F_bill.place(x=1150, y=250, width=440, height=380)
        F_bill.pack()

        Label(F_bill, text="Bill", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        # scroll bar in bill area
        scrol_y = Scrollbar(F_bill, orient=VERTICAL)
        self.textarea = Text(F_bill, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        name = StringVar()
        contact = IntVar()
        address = StringVar()
        issue_date = StringVar()
        self.total = 0
        if data:
            name = data['Name']
            contact = data['contact']
            # address = data['address']
            issue_date = data['issue_date']

            for item_name in self.items.keys():
                if self.items[item_name][1].get() != 0:
                    self.total = (int(self.get_total_days(data['issue_date']) + 1) * int(
                        self.items[item_name][1].get()) * int(get_rate(item_name))) + self.total

        # self.textarea.configure(state="normal")
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\t    میاں بلڈنگ میٹیریئل سریا سٹور")
        self.textarea.insert(END, f"\n\n Customer Name: {name}")
        self.textarea.insert(END, f"\n Contact Number:{contact} ")
        # self.textarea.insert(END, f"\n Address: {address}")
        self.textarea.insert(END, f"\n issue date: {issue_date}")
        self.textarea.insert(END, f"\n Total: {self.total}")

        self.textarea.insert(END, "\n=================================================")
        self.textarea.insert(END, "\n\tمال\t\tروپے     در     نگ    یوم")
        self.textarea.insert(END, "\n=================================================")

        for item_name in self.items.keys():
            if self.items[item_name][1].get() != 0:
                self.textarea.insert(END,
                                     f"\n{self.items[item_name][0]}\t\t\t {self.get_total_days(data['issue_date'])}\t {self.items[item_name][1].get()}   {get_rate(item_name)}    {self.calculation_rent(item_name, self.items[item_name][1].get(), self.get_total_days(data['issue_date']))}")
                # print(self.items[i][1].get(),' ',self.items[i][0])

        self.textarea.configure(state="disable")

        Button(bill, text="Print & Update Record", width=25, font="arial 15 bold", bd=7, bg='red',
               command=lambda: self.update_customer(data,self.total)).pack()
        mainloop()

# ---------------commented write bill area function
    # def write_bill_area(self,data=None):
    #     name = StringVar()
    #     contact = IntVar()
    #     address = StringVar()
    #     issue_date= StringVar()
    #     self.total = 0
    #     if data:
    #         name = data['Name']
    #         contact = data['contact']
    #         address = data['address']
    #         issue_date = data['issue_date']
    #
    #         for item_name in self.items.keys():
    #             if self.items[item_name][1].get() != 0:
    #                 self.total = (int(self.get_total_days(data['issue_date']) + 1) * int(
    #                     self.items[item_name][1].get()) * int(get_rate(item_name))) + self.total
    #
    #     self.textarea.configure(state="normal")
    #     self.textarea.delete('1.0',END)
    #     self.textarea.insert(END, "\t    میاں بلڈنگ میٹیریئل سریا سٹور")
    #     self.textarea.insert(END, f"\n\n Customer Name: {name}")
    #     self.textarea.insert(END, f"\n Contact Number:{contact} ")
    #     self.textarea.insert(END, f"\n Address: {address}")
    #     self.textarea.insert(END, f"\n issue date: {issue_date}")
    #     self.textarea.insert(END, f"\n Total: {self.total}")
    #
    #
    #     self.textarea.insert(END, "\n=================================================")
    #     self.textarea.insert(END, "\n\tمال\t\tروپے     در     نگ    یوم")
    #     self.textarea.insert(END, "\n=================================================")
    #
    #
    #     for item_name in self.items.keys():
    #         if self.items[item_name][1].get() != 0:
    #             self.textarea.insert(END,f"\n{self.items[item_name][0]}\t\t\t {self.get_total_days(data['issue_date'])}\t {self.items[item_name][1].get()}   {get_rate(item_name)}    {self.calculation_rent(item_name,self.items[item_name][1].get(),self.get_total_days(data['issue_date']))}")
    #             # print(self.items[i][1].get(),' ',self.items[i][0])
    #
    #
    #     self.textarea.configure(state="disable")

# ----------------------------------------------callable Functions ----------------------------------------



    def check_validate(self,e, item_name, total_number_of_item):
        number_of_require_item = self.items[item_name][1].get()

        if not validate_number_of_items(number_of_require_item, total_number_of_item):
            messagebox.showerror('Invalid Values', 'Error: \n' + 'you have ' + str(
                total_number_of_item) + ' ' + item_name + '\n' + 'you enter ' + str(number_of_require_item))
            self.items[item_name][1] = IntVar()

    def update_customer(self,data,total_rent):
        current_date = f"{self.current_date:%a, %b %d %Y}"
        total_days = self.get_total_days(data['issue_date'])
        data = Orders().order_update(self.items, data,current_date,total_days,total_rent)
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
        self.show_customer_details(data)

        self.orders_scrollable_frame.destroy()
        self.show_all_customers()
        print(self.textarea.get('1.0', 'end-1c'))
        receipt.prnt(self.textarea.get('1.0', 'end-1c'))  # printing function


# ----------------------------------------------canvas Functions ----------------------------------------
    def details_canvas_frame(self):
        # canvas use for scrollbar area
        self.details_canvas = Canvas(self.F_details, bg=self.bg_color)
        self.details_canvas.pack(side="left", fill="both", expand=True)

        self.details_scrollbar = Scrollbar(self.F_details, orient="vertical", command=self.details_canvas.yview)
        self.details_scrollbar.pack(side="right", fill="y")

        self.details_scrollable_frame = Frame(self.details_canvas, bg=self.bg_color)

        self.details_scrollbar.bind(
            "<Configure>",
            lambda e: self.details_canvas.configure(
                scrollregion=self.details_canvas.bbox("all")
            )
        )

        self.details_canvas.create_window((0, 0), window=self.details_scrollable_frame, anchor="nw")
        self.details_canvas.configure(yscrollcommand=self.details_scrollbar.set)

        self.details_canvas.bind("<Enter>", self.details_bound_mousewheel)
        self.details_canvas.bind("<Leave>", self.details_unbound_mousewheel)
        pass

    def customer_canvas_frame(self):
        # canvas use for scrollbar area
        self.Orders_canvas = Canvas(self.F_Orders, bg=self.bg_color)
        self.Orders_canvas.pack(side="left", fill="both", expand=True)

        Orders_Scrollbar = Scrollbar(self.F_Orders, orient="vertical", command=self.Orders_canvas.yview)
        Orders_Scrollbar.pack(side="right", fill="y")

        self.orders_scrollable_frame = Frame(self.Orders_canvas, bg=self.bg_color)

        Orders_Scrollbar.bind(
            "<Configure>",
            lambda e: self.Orders_canvas.configure(
                scrollregion=self.Orders_canvas.bbox("all")
            )
        )

        self.Orders_canvas.create_window((0, 0), window=self.orders_scrollable_frame, anchor="nw")
        self.Orders_canvas.configure(yscrollcommand=Orders_Scrollbar.set)

        self.Orders_canvas.bind("<Enter>", self.orders_bound_mousewheel)
        self.Orders_canvas.bind("<Leave>", self.orders_unbound_mousewheel)

# ----------------------------------------------Mouse Functions ----------------------------------------

    def orders_bound_mousewheel(self, eve):
        self.Orders_canvas.bind_all("<MouseWheel>", self.orders__move)

    def orders_unbound_mousewheel(self, eve):
        self.Orders_canvas.unbind_all("<MouseWheel>")

    def orders__move(self, event):
        self.Orders_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def details_bound_mousewheel(self, eve):
        self.details_canvas.bind_all("<MouseWheel>", self.details__move)

    def details_unbound_mousewheel(self, eve):
        self.details_canvas.unbind_all("<MouseWheel>")

    def details__move(self, event):
        self.details_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# ----------------------------------------------auto refresh ----------------------------------------
    def refresh_page(self):
        data = Orders().all_orders()
        if len(data) != len(self.orders):
            self.orders_scrollable_frame.destroy()
            self.show_all_customers()

        self.after(1000, self.refresh_page) # run itself again after 1000 ms
        pass
    def get_total_days(self, issue_date):
        current_date = f"{self.current_date:%a, %b %d %Y}"
        date_format = "%a, %b %d %Y"
        a = datetime.strptime(current_date, date_format)
        b = datetime.strptime(issue_date, date_format)
        delta = a-b
        return delta.days

    def calculation_rent(self, item_name, total_items, total_days):
        total_days = total_days+1
        item_rate = get_rate(item_name)

        return (int(item_rate) * int(total_items)) * int(total_days)


