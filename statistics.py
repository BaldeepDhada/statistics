import math

def mean(alist):
    
    return sum(alist)/len(alist)

def median(alist):
    
    if len(alist) == 1:
        median = alist[0]
        return median
    elif len(alist)%2 == 0:
        new_list = sorted(alist)
        value_one = new_list[round(len(alist)/2) - 1]
        value_two = new_list[round(len(alist)/2)]
        median = (value_one + value_two)/2
        return median             
    else:
        new_list = sorted(alist)
        median = new_list[round((len(alist) + 1)/2) - 1]
        return median

def mode(alist):
    data_dict = {}
    count, item = 0, ""
    for item in alist:
        data_dict[item] = data_dict.get(item, 0) + 1
        if data_dict[item] >= count:
            count, item = data_dict[item], item
    key_list = list(data_dict.keys())
    value_list = list(data_dict.values())
    
    index_list = []
    for i in range(len(value_list)):
        if value_list[i] == count:
            index_list.append(i)
    
    mode_list = []
    for i in range(len(index_list)):
        mode_list.append(key_list[index_list[i]])
    
    mode = ", ".join(map(str, mode_list))
    if count > 1:
        if len(index_list) > 1:
            return f'{mode} are the mode and they are repeated {count} times each\n'
        else:
            return f'{mode} is the mode and it is repeated {count} times\n'
    else:
        return f'This data set has no repeating values\n'

def standard_deviation(alist, average):
    
    square = []
    for i in alist:
        square.append((i - average)**2)
    
    s_deviation = math.sqrt(sum(square)/len(square))
    return f'The standard_deviation of this data set is {s_deviation}'
    
def main():        
    
    data_points = input("Type your data points in a single line seperated by a space: ")
    print()
    data = data_points.split()
    data_list = []
    non_data_list = []
    for i in range(len(data)):
        if data[i].isdecimal():
            data_list.append(int(data[i]))
        elif data[i].find("-") == 0 and data[i].replace("-", "").isdecimal():
            data_list.append(int(data[i]))
        elif data[i].count(".") == 1 and data[i].replace(".", "").isdecimal():
            data_list.append(float(data[i]))
        elif data[i].find("-") == 0 and data[i].count(".") == 1 and data[i].replace(".", "").replace("-", "").isdecimal(): 
            data_list.append(float(data[i]))
        else:
            non_data_list.append(data[i])

    non_data_list_formatted = ", ".join(map(str, non_data_list))
    if len(non_data_list) > 0:
        print(f'Here are things you may have inputed by accident or made a mistake: {non_data_list_formatted}\n')
    
    data_list_formatted = ", ".join(map(str, data_list))
    print(f'Here is the list of your data: {data_list_formatted}\n')
    average = mean(data_list)
    print(f'The mean value of this data set is {average}\n')
    med = median(data_list)
    print(f'The median value of this data set is {med}\n')
    print(mode(data_list))
    print(standard_deviation(data_list, average))

main()