import numpy as np


def GetOp(icost, dcost, scost):
    if min(icost, dcost, scost) == icost:
        return 'insertion'
    elif min(icost, dcost, scost) == dcost:
        return 'deletion'
    else:
        return 'substitution'


def Levenshtein(x, y):
    c = len(x)
    r = len(y)

    D = np.zeros([r + 1, c + 1])
    action = np.full([r + 1, c + 1], None)
    for i in range(c + 1):  # 0th row initialization
        D[0][i] = i
    for j in range(r + 1):  # 0th column initialization
        D[j][0] = j

    for j in range(1, r + 1):
        for i in range(1, c + 1):
            icost = D[j - 1][i] + 1                     # insertion cost
            dcost = D[j][i - 1] + 1                     # deletion cost
            pre_scost = 0 if x[i - 1] == y[j - 1] else 1
            scost = D[j - 1][i - 1] + pre_scost         # substitution cost

            D[j][i] = min(icost, dcost, scost)
            act = GetOp(icost, dcost, scost)

            if act == 'substitution' and pre_scost == 0:
                act = 'changeless'

            action[j][i] = act

    edit_list = list()
    d = D[r][c]
    j = r
    i = c
    while j != 0 and i != 0:
        if action[j][i] == 'insertion':
            edit_list.append('insertion')
            j -= 1
        elif action[j][i] == 'deletion':
            edit_list.append('deletion')
            i -= 1
        elif action[j][i] == 'substitution':
            edit_list.append('substitution')
            j -= 1
            i -= 1
        elif action[j][i] == 'changeless':
            edit_list.append('changeless')
            j -= 1
            i -= 1

    edit_list.reverse()
    print(D)
    return d, edit_list


if __name__ == '__main__':
    # x = input('Test String:')
    # y = input('Reference String:')
    x = 'revgniaton'
    y = 'recognition'

    x = '1107666554117701'
    y = '100766555541707700'

    x = '0765530766544'
    y = '100766555541707700'

    d, result = Levenshtein(x, y)
    print(d)
    print(result)

    pass