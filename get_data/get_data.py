import tushare as ts

sz_list_file = open('sz_stock_list.dat')
sz_list = sz_list_file.readlines()
for stock_id in sz_list:
    stock_id = stock_id.strip()
    try:
        data = ts.get_h_data(stock_id, start='2015-04-01', end='2017-04-16')
        data.to_csv('data/'+stock_id)
    except:
        print stock_id+ " download error"

