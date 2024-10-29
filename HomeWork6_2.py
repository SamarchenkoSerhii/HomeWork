StringSeconds = int(input("Inpup number of seconds :"))
deytop = "днів,"
if 0 <= StringSeconds < 8640000:
    if 5 <= StringSeconds // 86400 <= 20 : deytop = "днів,"
    else:
        if StringSeconds // 86400-StringSeconds // 864000*10 == 1 :      deytop = "день,"
        elif 2<= StringSeconds // 86400-StringSeconds // 864000*10 <= 4 :  deytop = "дні,"

    second = (str(StringSeconds % 60).zfill(2))
    minute = (str(StringSeconds % 3600 // 60)).zfill(2)
    hour   = (str(StringSeconds % 86400 // 3600)).zfill(2)
    day    = str(StringSeconds // 86400)
    print(day,deytop,hour,":",minute,":",second)
else:
    print("the number is incorrect")