def count_nested_tuple(tuple_in):
    iterator = 0
    for i in tuple_in:
        if type(i) is tuple:
            iterator += count_nested_tuple(i)
        else:
            iterator +=1
    return iterator



if __name__ == '__main__':
    print(count_nested_tuple((1,)))
    print(count_nested_tuple((1, 2)))
    print(count_nested_tuple((1, (2, 3))))
    print(count_nested_tuple((1, (2, 3), 4)))
    print(count_nested_tuple((1, (2, 3, (4, 5)))))
    print(count_nested_tuple((1, (2, 3, (4, 5), 6))))