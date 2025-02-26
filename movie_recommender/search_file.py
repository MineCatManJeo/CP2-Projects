# This should search through the items in a list (file)
def search(rows,searches):
    found_items_1st = []
    found_items_2nd = []
    for row in rows:
        posible_fi = 0
        for search in searches:
            if isinstance(search,list):
                if int(row[4]) >= search[0] and int(row[4]) <= search[1]:
                    posible_fi += 1
            elif search in str(row):
                posible_fi += 1
        # possible fi just adds on the more user gets correct
        if posible_fi == len(searches):
            found_items_1st.append(row)
        elif posible_fi == len(searches)-1 and len(searches) >= 3:
            found_items_2nd.append(row)
    return found_items_1st, found_items_2nd
