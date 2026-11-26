# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: allanbreu <allanbreu@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/03 15:26:12 by allanbreu         #+#    #+#              #
#    Updated: 2026/08/04 12:00:38 by allanbreu        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input(" Enter length: "))
    width = int(input("Enter width: "))
    area = length * width 
    print("Plot area: ", area)