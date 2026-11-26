def ft_count_harvest_iterative():
    days_until_harvest = int(input("Days until harvest: "))
    for count in range(1, days_until_harvest + 1):
        print("Day", count)
    print("Harvest time!")
