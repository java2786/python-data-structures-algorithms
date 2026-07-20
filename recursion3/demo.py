def dice(sum, stop, path, list):
    if(sum == stop):
        list.append(path)
        return
    if(sum>stop):
        # print("Out:",path)
        return

    for i in range(1, 7):
        dice(sum+i, stop, path+str(i), list)


finalList = []
dice(0, 7, "", finalList)
print(finalList)
print(len(finalList))
