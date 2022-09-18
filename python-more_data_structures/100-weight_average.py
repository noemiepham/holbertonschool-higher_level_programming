#!/usr/bin/python3
def weight_average(my_list=[]):
    sumValues = 0
    sumWeights = 0
    for i in range(len(my_list)):
        sumValues += sum(list(my_list[i]))
    # values = sum(map(sum, my_list)) (cach khac de cong tuple in list)
        sumWeights += sum(list(my_list[1]))
    return (sumValues / sumWeights)
