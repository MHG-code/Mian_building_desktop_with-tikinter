import pandas as pd
from shop_data import get_row_number
import order_save

# ------ data formates
# print(df['Name'][0])
# print(df[header[0][0]])
# print(df['Name'])
# print(header[0][1])
# print(len(header[0]))

class Orders:
    def __init__(self):
        # variables
        self.bool = False
        self.headers = []  #all values in header[0]
        self.names = []
        self.data = []
        self.data_rec = {}

        # read csv file
        self.df = pd.read_csv('bills.csv', dtype=str)

        # Functions
        self.save_all_headers()
        self.save_all_names()
        pass
    def search_by_name(self,name='Ha'):
        for i in range(len(self.df)):  # loop for total data rows
            self.bool = False
            if name in self.df['Name'][i] and self.df['status'][i] != 'paid':

                for j in range(len(self.headers[0]) - 6):  # ignore name and issue date etc
                    j = j + 3
                    if self.df[self.headers[0][j]][i] != '0' and self.df['status'][i] != 'paid':
                        self.bool = True
                if self.bool == True:
                    self.data.append(self.df.iloc[i])
        return self.data

    def all_orders(self):
        for i in range(len(self.df)): # loop for total data rows
            self.bool = False
            for j in range(len(self.headers[0]) - 6): # ignore name and issue date etc
                j = j + 3
                if self.df[self.headers[0][j]][i] != '0' and self.df['status'][i] != 'paid':
                    self.bool = True
            if self.bool == True:
                self.data.append(self.df.iloc[i])
        return self.data

    def show_items(self,data):
        for i in range(len(self.headers[0])):
            if data[self.headers[0][i]] != '0':
                self.data_rec[self.headers[0][i]] = data[self.headers[0][i]] # dictionary (keys: values)
        # for i in self.data_rec.keys():
        #     if i not in 'Name':
        #         print(i , ' ',self.data_rec[i])
        return self.data_rec
    def search_orderby_uniqueId(self,uniqueId):
        for i in range(len(self.df)):
            if self.df['unique_id'][i] == uniqueId:
                for j in range(len(self.headers[0])):
                    if self.df[self.headers[0][j]][i] != '0':
                        self.data = self.df.iloc[i]
        # self.show_items(self.data)
    def order_update(self,items,data,current_date,total_days,total_rent): # order will update in bills file
        itr = int()
        for i in range(len(self.df)): # find data by name which will be update
            if data['unique_id'] == self.df['unique_id'][i]:
                itr = i                 # take row number which will be changed

        for item in data:
            if item != 'Name' and item != 'contact' and item != 'address' and item != 'issue_date' and item != 'unique_id' and item != 'status':
                # print(i ,' ', data[i]) # total taken item
                # print(i ,' ', items[i][1].get()) # number of given items

                self.df.loc[itr, item] = str(int(data[item]) - int(items[item][1].get()))
                self.df.to_csv('bills.csv', index = False)

                # update items from shop_data
                self.update_items(item,items[item][1].get())

                # Enter data into records
                order_save.Order(data['Name'],data['contact'],data['issue_date'],items).save_records(data['unique_id'],current_date,total_days,total_rent)
                # update user_status
                self.update_user_status(data['unique_id'],itr)

                # for store  updated customer in self.data variable
                self.search_orderby_uniqueId(data['unique_id'])
        # print(self.data_rec)
        return self.data

    def save_records(self,items,data):
        print(data)

        pass
    def update_user_status(self,unique_id,row_number):
        self.bool = False

        self.data = self.df.loc[self.df['unique_id']== unique_id]

        for item in self.data:
            if item != 'Name' and item != 'contact' and item != 'address' and item != 'issue_date' and item != 'unique_id' and item != 'status':
                if int(self.data[item]) > 0:
                    self.bool = True
        if self.bool == False:
            self.df.loc[row_number, 'status'] = 'paid'
            self.df.to_csv('bills.csv', index=False)

        pass


    def save_all_names(self):
        # self.names = df['Name'].values #save all names
        for i in range(len(self.df)):
            if self.df['Name'][i] not in self.names:
                self.names.append(self.df['Name'][i])
        pass
    def save_all_headers(self):
        self.headers = [self.df.columns.values]  # save all headers
        pass

    def update_items(self,item, item_value): # update items from shopdata file we can't use this function which is shop data because data formate
        df = pd.read_csv('shop_data.csv', dtype=str)

        item_row = get_row_number(item)

        df.loc[item_row, 'remain_piece'] = str(int(df['remain_piece'][item_row]) + int(item_value))
        df.loc[item_row, 'used_piece'] = str(int(df['used_piece'][item_row]) - int(item_value))
        df.to_csv('shop_data.csv', index=False)
        return

# --------- get all the data against all names
# df.set_index("Name", inplace=True)
# data = df.loc[names]
# print(data)
# Orders().update_user_status('Sun, Dec 05 202107de782b-cb10-4508-aaa9-6f6082df6835',0)
# Orders().search_orderby_uniqueId('Wed, Dec 08 2021380a1c40-95a5-4795-8cec-aead8e57e2af')
# print(Orders().search_by_name())