from matplotlib import pyplot as plt     # Pyplot for nice graphs
from matplotlib import patches as mpatches
from mpl_toolkits.mplot3d import Axes3D  # Used for 3D plots
from matplotlib.widgets import Slider, Button
import matplotlib
import numpy as np                      # NumPy
# import seaborn
from numpy import linalg as LA
# from collections import Counter
from Functions import xyzimport, Hkay, Onsite, Hop, RecursionRoutine
import sys
np.set_printoptions(threshold=sys.maxsize)

# Set hopping potential
Vppi = -1

# Define lattice vectors
# shiftx = 32.7862152500
# shifty = 8.6934634800
#
# # Retrieve unit cell
# xyz = xyzimport('TestCell.fdf')
# # Calculate onsite nearest neighbours
# Ham = Onsite(xyz, Vppi)
#
# # Shift unit cell
# xyz1 = xyz + np.array([shiftx, 0, 0])
# # Calculate offsite nearest neighbours
# V1 = Hop(xyz, xyz1, Vppi)
#
# # Shift unit cell
# xyz2 = xyz + np.array([0, shifty, 0])
# # Calculate offsite nearest neighbours
# V2 = Hop(xyz, xyz2, Vppi)
#
# # Shift unit cell
# xyz3 = xyz + np.array([shiftx, shifty, 0])
# # Calculate offsite nearest neighbours
# V3 = Hop(xyz, xyz3, Vppi)

h = np.array([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]])
V = np.array([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]])

# h = np.array([[0]])
# V = np.array([[1]])

h = h * Vppi
V = V * Vppi

# print(np.sum(h))

Show = 0
if Show == 1:
    plt.imshow(h)
    plt.colorbar()
    plt.show()
    plt.imshow(V)
    plt.colorbar()
    plt.show()

En = np.linspace(-3, 3, 100)
# En = np.linspace(-1, 1, 3)
eta = 1e-6j
G00 = np.zeros((En.shape[0]), dtype=complex)  # Empty data matrix for Green's functions
for i in range(En.shape[0]):  # Loop iterating over energies
    G, SelfER, SelfEL = RecursionRoutine(En[i], h, V, eta)  # Invoking the RecursionRoutine
    G = np.diag(G)  # The Green's functions for each site is in the diagonal of the G matrix
    G00[i] = G[4]  # Chosen Green's function (here the 4th site)
# print(G00)
Y = G00
X = En
Y1 = Y.real
Y2 = Y.imag
# Y1 = np.sort(Y1)
# Y2 = np.sort(Y2)
# print(Y1, Y2)
real, = plt.plot(X, Y1, label='real')
# imag, = plt.plot(X, Y2, label='imag')
imag, = plt.fill(X, Y2, c='orange', alpha=0.8, label='imag')
plt.ylim((-2, 4))
# plt.axis('equal')
plt.grid(which='major', axis='both')
plt.legend(handles=[imag, real])
plt.title('Greens function of a simple four-atom unit cell')
plt.xlabel('Energy E arb. unit')
plt.ylabel('Re[G00(E)]/Im[G00(E)]')
plt.savefig('imrealplot.eps', bbox_inches='tight')
plt.show()

for i in range(h[:, 0].shape[0]):
    s = i
    xy = (h[i, 0], h[i, 1])
    plt.annotate(s, xy)
plt.grid(b=True, which='both', axis='both')
plt.show()
