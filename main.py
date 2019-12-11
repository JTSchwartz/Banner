#!/usr/bin/env python

import argparse
import letters
import string

default_art = "#"

parser = argparse.ArgumentParser(description="Create banner comments")

parser.add_argument("banner", metavar="banner", type=str, help="String to be converted to a banner comment")

parser.add_argument("-a", "--art", metavar="str", type=str, default=default_art,
						help=f"Banner character [default: \"{default_art}\"]")

parser.add_argument("-c", "--comment", metavar="str", type=str, default="//",
						help="Comment character [default: \"//\"]")

parser.add_argument("-s", "--spacing", metavar="int", type=int, default=2,
						help="Spacing between letters [default: 2]")

# TODO: Allow for change in character sizing
# TODO: Allow for lowercase
# TODO: Build up from string.uppercase to string.printable

args = parser.parse_args()
art = "".join(args.art)
banner = args.banner.upper()
change_banner_char = args.art != "#"
comment = "".join(args.comment) + " "
height = 7
spacing = args.spacing

upper_dict = dict(zip(list(string.ascii_uppercase), [letters.a_u, letters.b_u, letters.c_u, letters.d_u, letters.e_u, letters.f_u, letters.g_u, letters.h_u, letters.i_u, letters.j_u, letters.k_u, letters.l_u, letters.m_u, letters.n_u, letters.o_u, letters.p_u, letters.q_u, letters.r_u, letters.s_u, letters.t_u, letters.u_u, letters.v_u, letters.w_u, letters.x_u, letters.y_u, letters.z_u]))
upper_dict[" "] = " " * height

for line in range(height):
	row = (" " * spacing).join([upper_dict[char][line] for char in banner])
	
	if change_banner_char:
		row = row.replace("#", art)
	
	if len(art) > 1:
		row.replace(" ", "@")
	
	print(comment, row)