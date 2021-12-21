import pandas as pd

df = pd.read_csv('shop_data.csv', dtype=str)

def get_rate(item_name):
    item_row = get_row_number(item_name)
    # print(df['rate'][item_row])
    return df['rate'][item_row]

def get_totalItems(item_name):
    data = pd.read_csv('shop_data.csv', dtype=str)
    item_row = get_row_number(item_name)
    return int(data['remain_piece'][item_row])

def update_items(items_data):
    for item in items_data:
        if item != 'Name' and item != 'contact' and item != 'address' and item != 'issue_date' and item != 'unique_id' and item != 'status':
            if int(items_data[item]) > 0:
                item_row = get_row_number(item)

                df.loc[item_row, 'used_piece'] = str(int(items_data[item]) + int(df['used_piece'][item_row]))

                df.loc[item_row, 'remain_piece'] = str(int(df['remain_piece'][item_row]) - int(items_data[item]))

                df.to_csv('shop_data.csv', index=False)
    return
def get_row_number(item_name):
    for i in range(len(df)):
        if df['Name'][i] == item_name:
            return i

# def auto_update():
#     bool = False
#     for i in range(len(df)):
#         if (int(df['remain_piece'][i]) + int(df['used_piece'][i])) > int(df['total_piece'][i]):
#             df.loc[i, 'remain_piece'] = str(int(df['total_piece'][i]) - int(df['used_piece'][i]))
#             df.to_csv('shop_data.csv', index=False)
#             bool = True
#     return bool
# auto_update()
# print(get_rate('grander'))
# print(get_totalItems('grander'))