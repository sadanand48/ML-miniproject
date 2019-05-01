import numpy as np
from fractions import Fraction
# import networkx as nx
# import matplotlib.pyplot as plt
#
# G=nx.barabasi_albert_graph(10,4)
# nx.draw(G, with_labels=True)
# plt.show()

def float_format(vector, decimal):
    return np.round((vector).astype(np.float), decimals=decimal)


in_pr = Fraction(1, 5)


adj_mat = np.matrix([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])

x = np.zeros((5, 5))
x[:] = in_pr


damping = 0.85


formula = damping * adj_mat + ((1 - damping) * x)


pr = np.matrix([in_pr, in_pr, in_pr, in_pr, in_pr])
pr = np.transpose(pr)

prev_rank = pr
for it in range(1,100):
    pr = formula * pr
    print (float_format(pr, 3))
    #checking for convergence
    if (prev_rank == pr).all():
        break
    prev_rank = pr

print ("Final:\n", float_format(pr, 3))
print ("sum", np.sum(pr))


