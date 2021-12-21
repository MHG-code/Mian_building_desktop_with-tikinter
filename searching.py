import pandas as pd

import my_functions

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
    def search_by_name(self):
        print("searching...")

    def all_orders(self):
        for i in range(len(self.df)): # loop for total data rows
            self.bool = False
            for j in range(len(self.headers[0]) - 2): # ignore name and issue date
                j = j + 1
                if self.df[self.headers[0][j]][i] != '0':
                    self.bool = True
            if self.bool == True:
                self.data.append(self.df.iloc[i])
        return self.data
    def save_all_names(self):
        # self.names = df['Name'].values #save all names
        for i in range(len(self.df)):
            if self.df['Name'][i] not in self.names:
                self.names.append(self.df['Name'][i])
        pass
    def save_all_headers(self):
        self.headers = [self.df.columns.values]  # save all headers
        pass
    def show_items(self,name,data):
        for i in range(len(self.headers[0])):
            if data[self.headers[0][i]] != '0':
                self.data_rec[self.headers[0][i]] = data[self.headers[0][i]]
        # for i in self.data_rec.keys():
        #     if i not in 'Name':
        #         print(i , ' ',self.data_rec[i])
        return self.data_rec


# --------- get all the data against all names
# df.set_index("Name", inplace=True)
# data = df.loc[names]
# print(data)
