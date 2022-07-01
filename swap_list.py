

def swap_numbers(swap_list):
    l = len(swap_list)
    temp = swap_list[0]
    swap_list[0] = swap_list[l -1]
    swap_list[l - 1] = temp
    return swap_list

def swap_list_fun(swap_list):
    start, *middle, end = swap_list
    swap_list = [end, *middle, start]
    return swap_list

def largest_num(list):
    max=list[0]
    for n in list:
        if n > max:
            max = n
    return max

def second_largest_num(list):
    num = largest_num(list)
    list.remove(num)
    return largest_num(list)

def count_of_alpha(sample_str):
    alpha_count = {}
    for i in sample_str:
        if i in alpha_count:
            alpha_count[i] += 1
        else:
            alpha_count[i] = 1
        print(alpha_count)
    return alpha_count

my_list_1 = [23, 34, 56, 32, 53, 78, 24]
print(sorted(my_list_1)[-1])
print(sorted(my_list_1)[-2])

my_book="wings of fire"
print(count_of_alpha(my_book))
print(len(my_book.split()))
my_book="wings;of;fire"
print(len(my_book.split(";")))




