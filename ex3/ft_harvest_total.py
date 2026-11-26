# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: allanbreu <allanbreu@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/03 16:15:50 by allanbreu         #+#    #+#              #
#    Updated: 2026/08/04 12:00:40 by allanbreu        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print("Total harvest:",total)