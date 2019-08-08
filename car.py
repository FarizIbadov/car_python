while True:
    category = input("Kateqoriyanizi daxil edin:")
    bashlangic = int(input("begining distanse:"))
    son = int(input("ending distanse:"))

    borc = 0
    if son >= bashlangic:
        ferq = (son - bashlangic) 
    else:
        ferq = (999999999 - bashlangic + son)

    if category == "b":
        borc += 40    
        borc += ferq * 0.25
    elif category == "d":
        borc += 60
        if ferq > 100:
            borc += (ferq - 4000000) * 0.25
    elif category == 'w':
        borc += 190
        if ferq > 900 and ferq <= 1500:
            borc += 190
        elif ferq > 1500:
            borc += 390
            borc += (ferq - 1500) * 0.25

    print("Sizin shotuvuz:", borc)
    cavab = input("Davam etmek isteyirsinizmi? [y|n]")
    if cavab == 'y':
        continue
    else:
        print("Bye!")
        break