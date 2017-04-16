#encoding:utf8
'''
    label data, 0 : buy  1 : sale   2: do nothoing
    buy : 从该天开始，N天之内的最低点，并且最高点和最低点相差10%以上
    sale : 从该天开始，N天之内的最高点，并且最高点和最低点相差10%以上
'''
import os

def get_file_list(path):
    result = []
    path_dir = os.listdir(path)
    for item in path_dir:
        result.append(item)
    return result

def parse_data(line):
    vals = line.split(',')
    date = vals[0]
    open_val = float(vals[1])
    high_val = float(vals[2])
    close_val = float(vals[3])
    low_val = float(vals[4])
    volume_val = float(vals[5])
    amount_val = float(vals[6])
    return (date, open_val, close_val, low_val, volume_val, amount_val)

def label_data(prices):
    label = []
    N = 20
    size = len(prices)
    for i in range(0, size):
        label.append(2)
    start = 0
    end = size-N
    if end <= start:
        return label
    for idx in range(start, end):
        '''
            check buy, sale
        '''
        min_val = prices[idx]
        max_val = prices[idx]
        min_flag = True
        max_flag = True
        for i in range(idx+1, idx+N):
            if prices[i] < min_val:
                min_val = prices[i]
                min_flag = False
            if prices[i] > max_val:
                max_val = prices[i]
                max_flag = False
        '''
            buy
        '''
        if min_flag == True:
            diff = max_val - prices[idx]
            percent = diff/prices[idx]
            if percent > 0.1:
                label[idx] = 0
        '''
            sale
        '''
        if max_flag == True:
            diff = prices[idx] - min_val
            percent = diff/prices[idx]
            if percent > 0.1:
                label[idx] = 1
    return label

for item in get_file_list('./data'):
    f = open('./data/'+item)
    first = True
    close_vals = []
    lines = f.readlines()
    for l in lines:
        if first :
            first = False
            continue
        l = l.strip()
        vals = parse_data(l)
        close_vals.append(vals[2])
    f.close()
    close_vals.reverse()
    labels = label_data(close_vals)
    f = open('./label_data/'+item, 'w')
    size = len(lines)
    for idx in range(1, size):
        l = lines[idx].strip()
        buf = '%s,%d\n'%(l, labels[size -1 - idx])
        f.write(buf)
    f.close()




