def binSearch(lst, value):
        # High and low set in class initialisation.
        high = len(lst) -1 
        low = 0
        while (low <= high):
            midpoint = (high + low) /2 
            # print(midpoint)
            if (lst[midpoint]) > value: # If value is lower than the midpoint then truncate.
                high = midpoint - 1
            elif (lst[midpoint] < value):
                low = midpoint + 1
            else:
                print(midpoint)
                return midpoint
        print("Not Found")
