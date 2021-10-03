import re
from bs4 import BeautifulSoup as bs

import matplotlib.pyplot as plt

with open("data.txt", 'r') as data_text:
    new_data = data_text.read()
    occurence_a = re.findall(r"\ba",new_data)
    occurence_A = re.findall(r"\bA", new_data)
    beginning_a = len(occurence_A) + len(occurence_a)

    occurence_b = re.findall(r"\bb",new_data)
    occurence_B = re.findall(r"\bB", new_data)
    beginning_b = len(occurence_B) + len(occurence_B)

    occurence_c = re.findall(r"\bc",new_data)
    occurence_C = re.findall(r"\bC", new_data)
    beginning_c = len(occurence_C) + len(occurence_c)

    occurence_d = re.findall(r"\bd",new_data)
    occurence_D = re.findall(r"\bD", new_data)
    beginning_d = len(occurence_D) + len(occurence_d)

    occurence_e = re.findall(r"\be",new_data)
    occurence_E = re.findall(r"\bE", new_data)
    beginning_e = len(occurence_E) + len(occurence_e)

    occurence_f = re.findall(r"\bf",new_data)
    occurence_F = re.findall(r"\bF", new_data)
    beginning_f = len(occurence_F) + len(occurence_f)


    occurence_g = re.findall(r"\bg",new_data)
    occurence_G = re.findall(r"\bG", new_data)
    beginning_g = len(occurence_G) + len(occurence_g)

    occurence_h = re.findall(r"\bh",new_data)
    occurence_H = re.findall(r"\bH", new_data)
    beginning_h = len(occurence_H) + len(occurence_h)

    occurence_i = re.findall(r"\bi",new_data)
    occurence_I = re.findall(r"\bI", new_data)
    beginning_i = len(occurence_I) + len(occurence_i)

    occurence_j = re.findall(r"\bj",new_data)
    occurence_J = re.findall(r"\bJ", new_data)
    beginning_j = len(occurence_J) + len(occurence_j)

    occurence_k = re.findall(r"\bk",new_data)
    occurence_K = re.findall(r"\bK", new_data)
    beginning_k = len(occurence_K) + len(occurence_k)

    occurence_l = re.findall(r"\bl",new_data)
    occurence_L = re.findall(r"\bL", new_data)
    beginning_l = len(occurence_L) + len(occurence_l)

    occurence_m = re.findall(r"\bm",new_data)
    occurence_M = re.findall(r"\bM", new_data)
    beginning_m = len(occurence_M) + len(occurence_m)

    occurence_n = re.findall(r"\bn",new_data)
    occurence_N = re.findall(r"\bN", new_data)
    beginning_n = len(occurence_N) + len(occurence_n)

    occurence_o = re.findall(r"\bo",new_data)
    occurence_O = re.findall(r"\bO", new_data)
    beginning_o = len(occurence_O) + len(occurence_o)

    occurence_p = re.findall(r"\bp",new_data)
    occurence_P = re.findall(r"\bP", new_data)
    beginning_p = len(occurence_P) + len(occurence_p)

    occurence_q = re.findall(r"\bq",new_data)
    occurence_Q = re.findall(r"\bQ", new_data)
    beginning_q = len(occurence_Q) + len(occurence_q)

    occurence_r = re.findall(r"\br",new_data)
    occurence_R = re.findall(r"\bR", new_data)
    beginning_r = len(occurence_R) + len(occurence_r)

    occurence_s = re.findall(r"\bs",new_data)
    occurence_S = re.findall(r"\bS", new_data)
    beginning_s = len(occurence_S) + len(occurence_s)

    occurence_t = re.findall(r"\bt",new_data)
    occurence_T = re.findall(r"\bT", new_data)
    beginning_t = len(occurence_T) + len(occurence_t)

    occurence_u = re.findall(r"\bu",new_data)
    occurence_U = re.findall(r"\bU", new_data)
    beginning_u = len(occurence_U) + len(occurence_u)

    occurence_v = re.findall(r"\bv",new_data)
    occurence_V = re.findall(r"\bV", new_data)
    beginning_v = len(occurence_V) + len(occurence_v)

    occurence_w = re.findall(r"\bw",new_data)
    occurence_W = re.findall(r"\bW", new_data)
    beginning_w = len(occurence_W) + len(occurence_w)

    occurence_x = re.findall(r"\bx",new_data)
    occurence_X = re.findall(r"\bX", new_data)
    beginning_x = len(occurence_X) + len(occurence_x)

    occurence_y = re.findall(r"\by",new_data)
    occurence_Y = re.findall(r"\bY", new_data)
    beginning_y = len(occurence_Y) + len(occurence_y)

    occurence_z = re.findall(r"\bz",new_data)
    occurence_Z = re.findall(r"\bZ", new_data)
    beginning_z = len(occurence_Z) + len(occurence_z)

x = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
y = [beginning_a,beginning_b,beginning_c,beginning_d,beginning_e,beginning_f,beginning_g,beginning_h,beginning_i,beginning_j,
     beginning_k,beginning_l,beginning_m,beginning_n,beginning_o,beginning_p,beginning_q,beginning_r,beginning_s,beginning_t,
     beginning_u,beginning_v,beginning_w,beginning_x,beginning_y,beginning_z]
plt.plot(x,y)
plt.show()