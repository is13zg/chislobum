from itertools import product, combinations_with_replacement
from pprint import pprint
from random import shuffle
from itertools import product, permutations, combinations
from collections import Counter


def less_than(numbers_tuple, comparison_number):
    return all(number < comparison_number for number in numbers_tuple)


def more_than(numbers_tuple, comparison_number):
    return any(number > comparison_number for number in numbers_tuple)


def lamda2(x):
    tt = list(x)
    shuffle(tt)
    return tuple(tt)


def count_numbers(nested_list):
    # Функция для "выпрямления" вложенных списков
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    # Выпрямляем список и подсчитываем вхождения каждого числа
    flat_list = list(flatten(nested_list))
    number_counts = Counter(flat_list)

    return number_counts


def check(dict, t_num):
    tx = [n for n in dict.items() if n[0][1] == t_num]
    # print(tx)
    ttmp = [n[1] for n in tx]
    # print(ttmp)
    txmax = max(ttmp)
    txmin = min(ttmp) if len(ttmp) == 6 else 0
    return txmax - txmin <= 2


def all_check_and_viiw(dict):
    for t_num in range(10):
        print(t_num)
        tx = [n for n in dict.items() if n[0][1] == t_num]
        print(tx)
        ttmp = [n[1] for n in tx]
        print(ttmp)
        txmax = max(ttmp)
        txmin = min(ttmp) if len(ttmp) == 6 else 0
        print(txmin, txmax)
        print("delat", txmax - txmin)
        max_ls = []
        for kk in tx:
            if kk[1] == txmax:
                max_ls.append(kk[0][0])
        print("maxes", " ".join(max_ls))
        if txmin == 0:
            t_set = {"red", "yellow", "green", "blue", "violet", "orange"}
            for kk in tx:
                t_set.remove(kk[0][0])
            print("mines", " ".join(list(t_set)))
        else:
            min_ls = []
            for kk in tx:
                if kk[1] == txmin:
                    min_ls.append(kk[0][0])
            print("mines", " ".join(min_ls))
        print()


def calculate_expressions0(a, b, c, d, Natural=True, less64=True):
    # Define the operators
    operators = ['+', '-']

    # Generate all possible permutations of the four numbers and all possible combinations of three operators
    num_permutations = list(permutations([a, b, c, d]))
    operator_combinations = list(product(operators, repeat=3))

    results = set()

    for nums in num_permutations:
        for ops in operator_combinations:
            expression = f"({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})"
            print(expression)
            try:
                # Evaluate the expression and add to results if it's a non-negative integer
                result = eval(expression)
                if less64:
                    if result >= 65:
                        continue
                if result == int(result) and result >= 1:
                    results.add((int(result), expression))
            except ZeroDivisionError:
                # Ignore division by zero errors
                continue

    return results


def calculate_expressions(a, b, c, d, Natural=True, less64=True):
    # Define the operators
    operators = ['+', '-']

    # Generate all possible permutations of the four numbers and all possible combinations of three operators
    num_permutations = list(permutations([a, b, c, d]))
    operator_combinations = list(product(operators, repeat=3))

    results = set()

    for nums in num_permutations:
        for ops in operator_combinations:
            expression = f"({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})"
            try:
                # Evaluate the expression and add to results if it's a non-negative integer
                result = eval(expression)
                if less64:
                    if result >= 65:
                        continue
                if result == int(result) and result >= 1:
                    results.add(int(result))
            except ZeroDivisionError:
                # Ignore division by zero errors
                continue

    return results


def calculate_expressions2(a, b, c, d, Natural=True, less64=True):
    # Define the operators
    operators = ['+', '-', '*', '/']

    # Generate all possible permutations of the four numbers and all possible combinations of three operators
    num_permutations = list(permutations([a, b, c, d]))
    operator_combinations = list(product(operators, repeat=3))

    results = set()

    for nums in num_permutations:
        for ops in operator_combinations:
            expression = f"({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})"
            try:
                # Evaluate the expression and add to results if it's a non-negative integer
                result = eval(expression)
                if less64:
                    if result >= 65:
                        continue
                if result == int(result) and result >= 1:
                    results.add(int(result))
            except ZeroDivisionError:
                # Ignore division by zero errors
                continue

    return results


def smal_test():
    # Test the function with an example
    main_ls = list([(3, 4, 6, 9), ])
    main_ans = []
    # Пример использования функции
    for x in main_ls:
        if len(set(x)) <= 2:
            continue
        t_ans = []
        t_ans.append(x)
        t_ans.append(calculate_expressions0(*x))
        main_ans.append(t_ans)
        pprint(main_ans)


def main_view():
    # Test the function with an example
    main_ls = list(combinations_with_replacement((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), 4))
    main_ans = []
    # Пример использования функции
    for x in main_ls:
        if len(set(x)) <= 2:
            continue
        t_ans = []
        t_ans.append(x)
        t_ans.append(calculate_expressions(*x))
        t_ans.append(calculate_expressions2(*x))
        main_ans.append(t_ans)
    main_ans = sorted(main_ans, key=lambda x: (len(set(x[0])), len(x[1]), len(x[2])), reverse=True)
    for x in main_ans:
        if len(set(x[1])) <= 3:
            continue
        if len(set(x[2])) <= 6:
            continue
        print(
            f"{sorted(x[0])}	{sorted(x[1])}	{len(x[1]) > 6}	{sorted(x[2])}	{less_than(x[0], 5)}	{less_than(x[0], 6)}	{less_than(x[0], 7)}	{more_than(x[0], 7)}")


def shuffle_lists_in_unison(list1, list2):
    # Check if lists are the same length
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length.")

    # Create a list of indices
    indices = list(range(len(list1)))

    # Shuffle the indices
    shuffle(indices)

    # Arrange the elements of both lists according to the shuffled indices
    shuffled_list1 = [list1[i] for i in indices]
    shuffled_list2 = [list2[i] for i in indices]

    return shuffled_list1, shuffled_list2

def shuffle_didgits_on_cards():
    nmt = [('yellow', 'red', 'violet', 'blue'),
           ('orange', 'blue', 'violet', 'yellow'),
           ('red', 'blue', 'green', 'orange'),
           ('yellow', 'blue', 'violet', 'red'),
           ('violet', 'yellow', 'orange', 'red'),
           ('yellow', 'red', 'green', 'violet'),
           ('yellow', 'green', 'red', 'orange'),
           ('yellow', 'violet', 'red', 'orange'),
           ('red', 'violet', 'blue', 'green'),
           ('yellow', 'violet', 'green', 'orange'),
           ('red', 'violet', 'green', 'yellow'),
           ('violet', 'orange', 'blue', 'green'),
           ('blue', 'orange', 'yellow', 'red'),
           ('orange', 'blue', 'red', 'yellow'),
           ('yellow', 'orange', 'violet', 'blue'),
           ('orange', 'red', 'blue', 'violet'),
           ('orange', 'violet', 'green', 'yellow'),
           ('yellow', 'blue', 'violet', 'green'),
           ('red', 'green', 'yellow', 'orange'),
           ('blue', 'yellow', 'green', 'red'),
           ('green', 'red', 'orange', 'blue'),
           ('yellow', 'red', 'blue', 'green'),
           ('orange', 'blue', 'red', 'violet'),
           ('blue', 'red', 'violet', 'green'),
           ('blue', 'green', 'violet', 'red'),
           ('green', 'red', 'orange', 'yellow'),
           ('green', 'violet', 'yellow', 'orange'),
           ('yellow', 'green', 'violet', 'red'),
           ('green', 'blue', 'orange', 'yellow'),
           ('blue', 'green', 'orange', 'yellow'),
           ('orange', 'blue', 'green', 'red'),
           ('red', 'orange', 'violet', 'blue'),
           ('violet', 'blue', 'green', 'orange'),
           ('red', 'green', 'yellow', 'orange'),
           ('orange', 'violet', 'red', 'green'),
           ('violet', 'yellow', 'blue', 'red'),
           ('orange', 'blue', 'yellow', 'violet'),
           ('orange', 'yellow', 'red', 'violet'),
           ('blue', 'green', 'yellow', 'orange'),
           ('green', 'violet', 'red', 'orange'),
           ('green', 'red', 'blue', 'yellow'),
           ('violet', 'green', 'blue', 'yellow'),
           ('red', 'green', 'yellow', 'blue'),
           ('orange', 'green', 'blue', 'violet'),
           ('red', 'blue', 'orange', 'yellow'),
           ('yellow', 'violet', 'green', 'red'),
           ('green', 'blue', 'yellow', 'violet'),
           ('violet', 'green', 'orange', 'red')]

    nums = [[2, 4, 7, 8],
            [4, 5, 6, 8],
            [1, 4, 6, 8],
            [2, 5, 8, 9],
            [3, 6, 7, 8],
            [5, 6, 7, 9],
            [3, 5, 6, 7],
            [1, 2, 4, 9],
            [1, 4, 7, 9],
            [4, 7, 8, 9],
            [3, 4, 6, 9],
            [3, 5, 6, 9],
            [3, 6, 8, 9],
            [2, 3, 6, 7],
            [2, 4, 5, 9],
            [3, 4, 8, 9],
            [2, 3, 7, 9],
            [1, 3, 5, 6],
            [3, 4, 5, 6],
            [1, 2, 4, 6],
            [1, 2, 5, 6],
            [1, 2, 4, 5],
            [1, 2, 3, 6],
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4],
            [0, 2, 3, 7],
            [0, 2, 5, 6],
            [0, 2, 4, 7],
            [0, 1, 5, 7],
            [0, 1, 2, 7],
            [0, 2, 3, 4],
            [1, 2, 6, 6],
            [1, 2, 5, 5],
            [1, 3, 5, 5],
            [2, 5, 5, 6],
            [2, 4, 5, 5],
            [3, 4, 5, 5],
            [3, 3, 4, 5],
            [1, 2, 4, 4],
            [1, 3, 4, 4],
            [2, 4, 6, 6],
            [2, 3, 5, 5],
            [1, 3, 3, 4],
            [2, 2, 4, 5],
            [2, 2, 3, 5],
            [1, 2, 3, 3]]
    nums2 = []
    colors2 = []

    for x in range(len(nums)):
        t1, t2 = shuffle_lists_in_unison(nums[x], nmt[x])
        nums2.append(t1)
        colors2.append(t2)
    print(nums2)
    print(colors2)




def final_check():
    nmt = [('yellow', 'red', 'violet', 'blue'),
 ('orange', 'blue', 'violet', 'yellow'),
 ('red', 'blue', 'green', 'orange'),
 ('yellow', 'blue', 'violet', 'red'),
 ('violet', 'yellow', 'orange', 'red'),
 ('yellow', 'red', 'green', 'violet'),
 ('yellow', 'green', 'red', 'orange'),
 ('yellow', 'violet', 'red', 'orange'),
 ('red', 'violet', 'blue', 'green'),
 ('yellow', 'violet', 'green', 'orange'),
 ('red', 'violet', 'green', 'yellow'),
 ('violet', 'orange', 'blue', 'green'),
 ('blue', 'orange', 'yellow', 'red'),
 ('orange', 'blue', 'red', 'yellow'),
 ('yellow', 'orange', 'violet', 'blue'),
 ('orange', 'red', 'blue', 'violet'),
 ('orange', 'violet', 'green', 'yellow'),
 ('yellow', 'blue', 'violet', 'green'),
 ('red', 'green', 'yellow', 'orange'),
 ('blue', 'yellow', 'green', 'red'),
 ('green', 'red', 'orange', 'blue'),
 ('yellow', 'red', 'blue', 'green'),
 ('orange', 'blue', 'red', 'violet'),
 ('blue', 'red', 'violet', 'green'),
 ('blue', 'green', 'violet', 'red'),
 ('green', 'red', 'orange', 'yellow'),
 ('green', 'violet', 'yellow', 'orange'),
 ('yellow', 'green', 'violet', 'red'),
 ('green', 'blue', 'orange', 'yellow'),
 ('blue', 'green', 'orange', 'yellow'),
 ('orange', 'blue', 'green', 'red'),
 ('red', 'orange', 'violet', 'blue'),
 ('violet', 'blue', 'green', 'orange'),
 ('red', 'green', 'yellow', 'orange'),
 ('orange', 'violet', 'red', 'green'),
 ('violet', 'yellow', 'blue', 'red'),
 ('orange', 'blue', 'yellow', 'violet'),
 ('orange', 'yellow', 'red', 'violet'),
 ('blue', 'green', 'yellow', 'orange'),
 ('green', 'violet', 'red', 'orange'),
 ('green', 'red', 'blue', 'yellow'),
 ('violet', 'green', 'blue', 'yellow'),
 ('red', 'green', 'yellow', 'blue'),
 ('orange', 'green', 'blue', 'violet'),
 ('red', 'blue', 'orange', 'yellow'),
 ('yellow', 'violet', 'green', 'red'),
 ('green', 'blue', 'yellow', 'violet'),
 ('violet', 'green', 'orange', 'red')]



    nums = [[2, 4, 7, 8],
            [4, 5, 6, 8],
            [1, 4, 6, 8],
            [2, 5, 8, 9],
            [3, 6, 7, 8],
            [5, 6, 7, 9],
            [3, 5, 6, 7],
            [1, 2, 4, 9],
            [1, 4, 7, 9],
            [4, 7, 8, 9],
            [3, 4, 6, 9],
            [3, 5, 6, 9],
            [3, 6, 8, 9],
            [2, 3, 6, 7],
            [2, 4, 5, 9],
            [3, 4, 8, 9],
            [2, 3, 7, 9],
            [1, 3, 5, 6],
            [3, 4, 5, 6],
            [1, 2, 4, 6],
            [1, 2, 5, 6],
            [1, 2, 4, 5],
            [1, 2, 3, 6],
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4],
            [0, 2, 3, 7],
            [0, 2, 5, 6],
            [0, 2, 4, 7],
            [0, 1, 5, 7],
            [0, 1, 2, 7],
            [0, 2, 3, 4],
            [1, 2, 6, 6],
            [1, 2, 5, 5],
            [1, 3, 5, 5],
            [2, 5, 5, 6],
            [2, 4, 5, 5],
            [3, 4, 5, 5],
            [3, 3, 4, 5],
            [1, 2, 4, 4],
            [1, 3, 4, 4],
            [2, 4, 6, 6],
            [2, 3, 5, 5],
            [1, 3, 3, 4],
            [2, 2, 4, 5],
            [2, 2, 3, 5],
            [1, 2, 3, 3]]

    res = []
    res2 = []
    for x in range(48):
        tx = list(zip(nmt[x], nums[x]))
        res2.append(tx)
        for y in range(4):
            res.append(tx[y])
    pprint(nmt)
    pprint(res2)
    tt2 = Counter(res)
    all_check_and_viiw(tt2)



def determ_color_brutforce():
    tt = combinations(("red", "yellow", "green", "blue", "violet", "orange"), 4)
    tt = list(tt)
    mt = tt[:] * 3 + tt[:3]
    nums = [[2, 4, 7, 8],
            [4, 5, 6, 8],
            [1, 4, 6, 8],
            [2, 5, 8, 9],
            [3, 6, 7, 8],
            [5, 6, 7, 9],
            [3, 5, 6, 7],
            [1, 2, 4, 9],
            [1, 4, 7, 9],
            [4, 7, 8, 9],
            [3, 4, 6, 9],
            [3, 5, 6, 9],
            [3, 6, 8, 9],
            [2, 3, 6, 7],
            [2, 4, 5, 9],
            [3, 4, 8, 9],
            [2, 3, 7, 9],
            [1, 3, 5, 6],
            [3, 4, 5, 6],
            [1, 2, 4, 6],
            [1, 2, 5, 6],
            [1, 2, 4, 5],
            [1, 2, 3, 6],
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4],
            [0, 2, 3, 7],
            [0, 2, 5, 6],
            [0, 2, 4, 7],
            [0, 1, 5, 7],
            [0, 1, 2, 7],
            [0, 2, 3, 4],
            [1, 2, 6, 6],
            [1, 2, 5, 5],
            [1, 3, 5, 5],
            [2, 5, 5, 6],
            [2, 4, 5, 5],
            [3, 4, 5, 5],
            [3, 3, 4, 5],
            [1, 2, 4, 4],
            [1, 3, 4, 4],
            [2, 4, 6, 6],
            [2, 3, 5, 5],
            [1, 3, 3, 4],
            [2, 2, 4, 5],
            [2, 2, 3, 5],
            [1, 2, 3, 3]]

    cc = 0
    while cc < 100000000:
        nmt = list(map(lamda2, mt))
        cc += 1
        shuffle(nmt)

        res = []
        for x in range(48):
            tx = list(zip(nmt[x], nums[x]))
            for y in range(4):
                res.append(tx[y])

        tt2 = Counter(res)

        if not check(tt2, 0):
            # print("No 0")
            continue
        if not check(tt2, 1):
            # print("No 1")
            continue
        if not check(tt2, 2):
            # print("No 2")
            continue
        if not check(tt2, 3):
            # print("No 3")
            continue
        if not check(tt2, 4):
            # print("No 4")
            continue
        if not check(tt2, 5):
            print("No 5")
            continue
        if not check(tt2, 6):
            print(nmt)
            print(nums)
            print(tt2)
            print("No 6")
            continue
        if not check(tt2, 7):
            print(nmt)
            print(nums)
            print(tt2)
            print("No 7")
            continue
        if not check(tt2, 8):
            print(nmt)
            print(nums)
            print(tt2)
            print("No 8")
            continue
        if not check(tt2, 9):
            print(nmt)
            print(nums)
            print(tt2)
            print("No 9")
            continue

        print(nmt)
        print(nums)
        print(tt2)
        break;

    print("Nothing")


def form_cards_list(nums):
    tec_ls = nums[:]

    print(len(list(map(tuple, tec_ls))))
    print(len(set(map(tuple, tec_ls))))

    all_sets_sums = set()
    all_sets_results = set()
    for x in tec_ls:
        all_sets_sums = all_sets_sums.union(calculate_expressions(*x))
        all_sets_results = all_sets_results.union(calculate_expressions2(*x))
    print("all_sets_sums", len(all_sets_sums), all_sets_sums)
    print("all_sets_results", len(all_sets_results), all_sets_results)

    dict = count_numbers(tec_ls)
    print(sorted(dict.items()))

    all_sets_sums = []
    all_sets_results = []
    for x in tec_ls:
        all_sets_sums = all_sets_sums + list(calculate_expressions(*x))
        all_sets_results = all_sets_results + list(calculate_expressions2(*x))
    print("all_sets_sums", len(all_sets_sums), all_sets_sums)
    print("all_sets_results", len(all_sets_results), all_sets_results)
    dict = count_numbers(all_sets_sums)
    print(sorted(dict.items()))

    dict = count_numbers(all_sets_results)
    print(sorted(dict.items()))


old_num = [[1, 2, 3, 4], [2, 2, 3, 4], [0, 2, 3, 4], [2, 3, 3, 4], [1, 3, 3, 4], [1, 2, 4, 5], [1, 3, 4, 5],
          [1, 2, 3, 5], [2, 3, 4, 5], [3, 3, 4, 5], [2, 2, 4, 5], [2, 2, 3, 5], [3, 4, 4, 5], [1, 2, 5, 5],
          [3, 4, 5, 5], [1, 3, 3, 5], [2, 3, 5, 5], [2, 3, 4, 6], [1, 2, 4, 6], [1, 2, 5, 6], [3, 3, 4, 6],
          [1, 2, 3, 6], [3, 3, 5, 6], [2, 2, 3, 6], [3, 4, 4, 6], [2, 4, 6, 9], [2, 3, 4, 8], [3, 4, 6, 8],
          [2, 3, 7, 9], [4, 5, 6, 8], [3, 4, 7, 9], [2, 3, 6, 9], [1, 2, 4, 8], [4, 4, 6, 8], [3, 3, 5, 9],
          [2, 3, 5, 7], [2, 3, 6, 7], [0, 2, 5, 6], [0, 3, 6, 8], [0, 2, 7, 8], [0, 3, 7, 8], [3, 4, 5, 7],
          [5, 6, 7, 9], [1, 3, 6, 9], [0, 4, 5, 7], [0, 5, 6, 9], [0, 2, 8, 9], [2, 3, 5, 9]]
new_nums = [[2, 4, 7, 8],
            [4, 5, 6, 8],
            [1, 4, 6, 8],
            [2, 5, 8, 9],
            [3, 6, 7, 8],
            [5, 6, 7, 9],
            [3, 5, 6, 7],
            [1, 2, 4, 9],
            [1, 4, 7, 9],
            [4, 7, 8, 9],
            [3, 4, 6, 9],
            [3, 5, 6, 9],
            [3, 6, 8, 9],
            [2, 3, 6, 7],
            [2, 4, 5, 9],
            [3, 4, 8, 9],
            [2, 3, 7, 9],
            [1, 3, 5, 6],
            [3, 4, 5, 6],
            [1, 2, 4, 6],
            [1, 2, 5, 6],
            [1, 2, 4, 5],
            [1, 2, 3, 6],
            [2, 3, 4, 5],
            [1, 3, 4, 5],
            [1, 2, 3, 5],
            [1, 2, 3, 4],
            [0, 2, 3, 7],
            [0, 2, 5, 6],
            [0, 2, 4, 7],
            [0, 1, 5, 7],
            [0, 1, 2, 7],
            [0, 2, 3, 4],
            [1, 2, 6, 6],
            [1, 2, 5, 5],
            [1, 3, 5, 5],
            [2, 5, 5, 6],
            [2, 4, 5, 5],
            [3, 4, 5, 5],
            [3, 3, 4, 5],
            [1, 2, 4, 4],
            [1, 3, 4, 4],
            [2, 4, 6, 6],
            [2, 3, 5, 5],
            [1, 3, 3, 4],
            [2, 2, 4, 5],
            [2, 2, 3, 5],
            [1, 2, 3, 3]]

shuffle_didgits_on_cards()
#final_check()
#determ_color_brutforce()
#form_cards_list(old_num)
#print()
#form_cards_list(new_nums)

#main_view()
# smal_test()
