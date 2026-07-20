def dice(sum, stop, path):
    if(sum == stop):
        print(path)
        return
    if(sum>stop):
        # print("Out:",path)
        return

    # for i in range(1, 7):
    #     dice(sum+i, stop, path+str(i))

    dice(sum+1, stop, path+"1")
    dice(sum+2, stop, path+"2")
    dice(sum+3, stop, path+"3")
    dice(sum+4, stop, path+"4")
    dice(sum+5, stop, path+"5")
    dice(sum+6, stop, path+"6")


dice(0, 5, "")