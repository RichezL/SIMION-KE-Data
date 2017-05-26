import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#Importing SIMION data
data1 = np.genfromtxt('Initial_KEs.txt', delimiter = ',')
data2 = np.genfromtxt('Pre_Quad_KE.txt', delimiter = ',')
data3 = np.genfromtxt('Final_KE.txt', delimiter = ',')

#Importing KE values from second column
initialKE = data1[:,][:,1]
prequadKE = data2[:,][:,1]
finalKE = data3[:,][:,1]

#Calculating Absolute and Percentage number of Ions Lost
numLost = float(len(initialKE))-float(len(finalKE))
percLost = numLost / 10

print "The number of ions lost was: %d or %.1f percent" % (numLost, percLost)

#Calculating mean and standard deviation of KEs
mu1 = np.mean(initialKE)
sigma1 = np.std(initialKE)

mu2 = np.mean(prequadKE)
sigma2 = np.std(prequadKE)

mu3 = np.mean(finalKE)
sigma3 = np.std(finalKE)

#Setting weight of bins s.t. frequency sums to one
weights1 = np.ones_like(initialKE)/float(len(initialKE))
weights2 = np.ones_like(prequadKE)/float(len(prequadKE))
weights3 = np.ones_like(finalKE)/float(len(finalKE))

#Histogram for Initial KE
plt.hist(initialKE, bins = 20, weights = weights1)
plt.title("Initial KE: $\mu = %.3f,\ \sigma = %.3f$" %(mu1, sigma1))
plt.xlabel("Kinetic Energy (eV)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#Histogram for Pre-Quad KE
plt.hist(prequadKE, bins = 20, weights = weights2)
plt.title("Pre-Quadrupole KE: $\mu = %.3f,\ \sigma = %.3f$" %(mu2, sigma2))
plt.xlabel("Kinetic Energy (eV)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#Histogram for Final KE
plt.hist(finalKE, bins = 20, weights = weights3)
plt.title("Final KE: $\mu = %.3f,\ \sigma = %.3f$" %(mu3,sigma3))
plt.xlabel("Kinetic Energy (eV)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
