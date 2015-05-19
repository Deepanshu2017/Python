__author__ = 'deepanshu'


def solve(my_array, N, profit, share, position):

    """base case"""
    # if I reached at the position which is equal to size then return
    if position == N:
        return profit

    # suppose I buy that share then
    pro = profit - my_array[position]
    buy = solve(my_array, N, pro, share + 1, position + 1)

    # Suppose I don' buy that share not I sell anything
    do_nothing = solve(my_array, N, profit, share, position + 1)

    # Suppose I sell my shares
    sell = 0
    if share:
        sell = share * my_array[position]
        sell = solve(my_array, N, sell + profit, 0, position + 1)

    temp = max(buy, sell)
    return max(temp, do_nothing)

T = int(raw_input())
for _ in range(T):
    N = int(raw_input())
    test = raw_input()
    test = test.split()
    my_array = []
    for i in range(N):
        my_array.append(int(test[i]))
    profit = 0
    share = 0
    position = 0
    res = solve(my_array, N, profit, share, position)
    print res