sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def get_last_element(x):
    return x[1]

sorted_list=sorted(sample,key= lambda x:get_last_element(x))
print(sorted_list)