def ft_count_harvest_recursive(d_u_h=int(input("Days until harvest:"))):
    def count_rec(count: int, start: int):
        if count+1 == start:
            return
        print("Day", start)
        count_rec(count, start + 1)
    count_rec(d_u_h, 1)
    print("Harvest time!")
ft_count_harvest_recursive()