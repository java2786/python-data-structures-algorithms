def dice(path, lenght):
    if(len(path)==lenght):
        print(path)
        return
    
    dice(path+"1", lenght)
    dice(path+"2", lenght)
    dice(path+"3", lenght)
    dice(path+"4", lenght)
    dice(path+"5", lenght)
    dice(path+"6", lenght)

dice("", 2)