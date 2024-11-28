# Activity Selection

def selection(activities):
    sorted_act = sorted(activities.items(), key= lambda x: x[1][1])
    current_time = sorted_act[0][1][0]
    selection_list = []
    ans = ""

    for i in range(len(sorted_act)):
        if sorted_act[i][1][0] >= current_time:
            selection_list.append(sorted_act[i][0])
            current_time = sorted_act[i][1][1]

    for i in range(len(selection_list)):
        if i != len(selection_list)-1:
            ans += selection_list[i] + ' -> '
        else:
            ans += selection_list[i]

    return ans


activities = {
    'A1': [1,3],
    'A2': [3,4],
    'A3': [2,5],
    'A4': [4,7],
    'A5': [8,9],
    'A6': [7,10]
}

print("Order of Selection of Activities : ", selection(activities))