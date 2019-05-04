def replace_tab(file_name):
    results = []
    with open(file_name) as f:
        for row in f:
            results.append(row.replace("\t"," "))
    return results


print(replace_tab('hightemp.txt'))
