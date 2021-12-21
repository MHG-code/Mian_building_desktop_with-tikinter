# Writing to an excel
# sheet using Python

import pathlib
import pandas as pd

from uuid import uuid4
from shop_data import update_items
class Order():
    def __init__(self, name,contact,issue_date,items,address=None):
        # self.data = items
        self.data = {
            'Name': name,
            'contact': contact,
            'address': address,
            'electronic_vaibrator' : items['electronic_vaibrator'][1].get(),
            'grander': items['grander'][1].get(),
            'dril_machine': items['dril_machine'][1].get(),
            'ghori_4ft': items['ghori_4ft'][1].get(),
            'ghori_5ft': items['ghori_5ft'][1].get(),
            'ghori_8ft': items['ghori_8ft'][1].get(),
            'ghori_10ft': items['ghori_10ft'][1].get(),
            'serhi_10ft': items['serhi_10ft'][1].get(),
            'serhi_25ft': items['serhi_25ft'][1].get(),
            'folding_serhi': items['folding_serhi'][1].get(),
            'folding_seat': items['folding_seat'][1].get(),
            'large_lohaPlate': items['large_lohaPlate'][1].get(),
            'small_lohaPlate': items['small_lohaPlate'][1].get(),
            'hand_rerhi': items['hand_rerhi'][1].get(),
            'demp_farma': items['demp_farma'][1].get(),
            'phata_7ft': items['phata_7ft'][1].get(),
            'baly'  : items['baly'][1].get(),
            'bans'  : items['bans'][1].get(),
            'drum'  : items['drum'][1].get(),
            'damosa': items['damosa'][1].get(),
            'karahi': items['karahi'][1].get(),
            'belcha': items['belcha'][1].get(),
            'genti' : items['genti'][1].get(),
            'kassi' : items['kassi'][1].get(),
            'panji' : items['panji'][1].get(),
            'wadan' : items['wadan'][1].get(),
            'cheni_hathora': items['cheni_hathora'][1].get(),
            'issue_date': issue_date,
            'unique_id': issue_date + str(uuid4()),
             'status' : 'unpaid'
        }
        #path file
        # path = "C:\\Users\\root\\Desktop\\MianApp\\bills.csv"
        # self.file = pathlib.Path(path)

    # self Functions
    def save_data(self):

        if all(x == 0 or x == self.data['Name'] or x == self.data['issue_date'] for x in self.data.values()):
            print('all vlues are empty')
        else:
            self.data_save_asCSV()

    def data_save_asCSV(self):
       df = pd.DataFrame(data=[self.data])
       try:
            df.to_csv('bills.csv',header=False, mode='a', index=False, encoding='utf-8', na_rep='0')
            update_items(self.data)
       except:
           print("data not save... may be file is bussy")

       return
    # def save_data(self):
    #
    #     if all(x == 0 or x == self.data['Name'] or x == self.data['issue_date'] for x in self.data.values()):
    #         print('all vlues are empty')
    #     else:
    #         if self.file.exists():
    #             self.data_save_asCSV()
    #         else:
    #            columns = ['Name','contact','address','electronic_vaibrator', 'grander', 'dril_machine', 'ghori_4ft', 'ghori_5ft', 'ghori_8ft', 'ghori_10ft', 'serhi_10ft', 'serhi_25ft', 'folding_serhi', 'folding_seat', 'large_lohaPlate', 'small_lohaPlate', 'hand_rerhi', 'demp_farma', 'phata_7ft', 'baly', 'bans', 'drum', 'damosa', 'karahi', 'belcha', 'genti', 'kassi', 'panji', 'wadan', 'cheni_hathora', 'issue_date', 'unique_id','status']
    #            self.data_save_asCSV(columns)
    #         return
    #
    # def data_save_asCSV(self,columns=None):
    #     if columns==None:
    #         self.header = False
    #         df = pd.DataFrame(data=[self.data])
    #     else:
    #         self.header = True
    #         df = pd.DataFrame(data=[self.data], columns=columns)
    #     try:
    #         df.to_csv('bills.csv',header=self.header, mode='a', index=False, encoding='utf-8', na_rep='0')
    #
    #                 #---------------- update Shop data
    #         update_items(self.data)
    #
    #     except:
    #         print("data not save... may be file is bussy")
    #     return

    def save_records(self,unique_id,current_date,total_days,total_rent):
        self.data['return_date'] = current_date
        self.data['unique_id'] = unique_id
        self.data['status'] = 'paid'
        self.data['total_days'] = total_days
        self.data['total_payment'] = total_rent


        df = pd.DataFrame(data=[self.data])
        df.to_csv('record.csv', header=False, mode='a', index=False, encoding='utf-8', na_rep='0')
        print(self.data)

        pass
# testing
# data = {
#             'Name': 'name',
#             'contact': 'contact',
#             'addr': 'address',
#             'electronic_vaibrator' : 'items['"electronic_vaibrator"'][1].get()',
#             'grander': 'items['"grander"'][1].get()',
#             'dril_machine': 'items['"dril_machine"'][1].get()',
#             'ghori_4ft': 'items['"ghori_4ft"'][1].get()',
#             'ghori_5ft': 'items['"ghori_5ft"'][1].get()',
#             'ghori_8ft': 'items['"ghori_8ft"'][1].get()',
#             'ghori_10ft': 'items['"ghori_10ft"'][1].get()',
#             'serhi_10ft': 'items['"serhi_10ft"'][1].get()',
#             'serhi_25ft': 'items['"serhi_25ft"'][1].get()',
#             'folding_serhi': 'items['"folding_serhi"'][1].get()',
#             'folding_seat': 'items['"folding_seat"'][1].get()',
#             'large_lohaPlate': 'items['"large_lohaPlate"'][1].get()',
#             'small_lohaPlate': 'items['"small_lohaPlate"'][1].get()',
#             'hand_rerhi': 'items['"hand_rerhi"'][1].get()',
#             'demp_farma': 'items['"demp_farma"'][1].get()',
#             'phata_7ft': 'items['"phata_7ft"'][1].get()',
#             'baly'  : 'items['"baly"'][1].get()',
#             'bans'  : 'items['"bans"'][1].get()',
#             'drum'  : 'items['"drum"'][1].get()',
#             'damosa': 'items['"damosa"'][1].get()',
#             'karahi': 'items['"karahi"'][1].get()',
#             'belcha': 'items['"belcha"'][1].get()',
#             'genti' : 'items['"genti"'][1].get()',
#             'kassi' : 'items['"kassi"'][1].get()',
#             'panji' :' items['"panji"'][1].get()',
#             'wadan' : 'items['"wadan"'][1].get()',
#             'cheni_hathora': 'items['"cheni_hathora"'][1].get()',
#             'issue_date': 'issue_date'
#         }
# Order('Hamza','03224901080','a1','12/45',data).save_data()