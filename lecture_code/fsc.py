import numpy as np
import h5py
import spimage
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy import ndimage
from scipy.optimize import leastsq
from scipy import optimize


def FSC(F1, F2):
    fsc = []
    
    F1 = np.fft.fftshift(np.fft.fftn(F1))
    F2 = np.fft.fftshift(np.fft.fftn(F2))
    
    r = np.sqrt((F1.shape[0]/2)**2 + (F1.shape[1]/2)**2 + (F1.shape[2]/2)**2)
    r = r.astype(np.int)
    
    if (F1.shape != F2.shape):
        return "shape mismatch"
    
    else:
        for i in np.arange(0,r,1):
            a, b, c = F1.shape[0]/2, F1.shape[1]/2, F1.shape[2]/2                                                                                                          
            x, y, z = np.ogrid[-a:F1.shape[0]-a, -b:F1.shape[1]-b, -c:F1.shape[2]-c]
            mask1 = x**2 + y**2 + z**2 >= i**2
            mask2 = x**2 + y**2 + z**2 < (i+1)**2
            mask3 = mask1 * mask2
            fsc_value = (F1[mask3] * np.conjugate(F2[mask3])).sum() / np.sqrt( (np.abs(F1[mask3])**2).sum() * (np.abs(F2[mask3])**2).sum())
            
            fsc.append(fsc_value)
            
    fsc = np.array(fsc)
            
    return fsc

def radial_average(data):
    average = []
    
    if len(data.shape) == 2:
        y, x = np.indices((data.shape))
        r = np.sqrt((x/2)**2 + (y/2)**2)
        r = r.astype(np.int)
        r = np.ravel(r)
        print(r)
    
        for i in np.arange(0,r[-1]):
            a, b = data.shape[0]/2, data.shape[1]/2                                                                                                         
            x, y = np.ogrid[-a:data.shape[0]-a, -b:data.shape[1]-b]
            mask = x**2 + y**2 == i**2
            average.append(np.average(np.ravel(data[mask])))
            
    if len(data.shape) == 3:
        z, y, x = np.indices((data.shape))
        r = np.sqrt((x)**2 + (y)**2 + (z)**2)
        r = r.astype(np.int)
        r = np.ravel(r)
        print(r)
    
        for i in np.arange(0,r[-1]):
            a, b, c = data.shape[0]/2, data.shape[1]/2, data.shape[2]/2                                                                                                          
            x, y, z = np.ogrid[-a:data.shape[0]-a, -b:data.shape[1]-b, -c:data.shape[2]-c]
            mask = x**2 + y**2 + z**2 == i**2
            average.append(np.average(np.ravel(data[mask])))
        
    return average

def fun2(z, f1, f2):
    x1, x2, x3 = z
    f2 = ndimage.interpolation.shift(f2, shift=(x1, x2, x3), mode='wrap')
    return np.sum(np.abs(f1 - f2) ** 2)

def vector_align(cm11, cm12, cm21, cm22):
    v1 = cm12 - cm11
    v2 = cm22 - cm21
    #print "vector 1: " + v1
    #print "vector 2: " + v2
    
    # unit vectors
    z = np.array((0,0,1))
    y = np.array((0,1,0))
    x = np.array((1,0,0))
    
    # angle to the z axis
    theta1 = np.arccos(np.inner(z,v1) / (np.linalg.norm(z) * np.linalg.norm(v1)))
    theta2 = np.arccos(np.inner(z,v2) / (np.linalg.norm(z) * np.linalg.norm(v2)))
    theta1 = theta1 * 180/np.pi
    theta2 = theta2 * 180/np.pi
    print("theta 1: %.2f" %(theta1))
    print("theta 2: %.2f" %(theta2))
    
    # angle to the yz - plane
    n = np.cross(y,z)
    #print "normal vector to the y-z-plane" + n
    
    if v1[0] < 0:
        phi1 = -(180 - ((np.arccos(np.inner(n,v1) / (np.linalg.norm(n) * np.linalg.norm(v1)))) * 180/np.pi))
    else:
        phi1 = -(90 - ((np.arccos(np.inner(n,v1) / (np.linalg.norm(n) * np.linalg.norm(v1)))) * 180/np.pi))
        
    if v2[0] < 0:
        phi2 = -(180 - ((np.arccos(np.inner(n,v2) / (np.linalg.norm(n) * np.linalg.norm(v2)))) * 180/np.pi))
    else:
        phi2 = -(90 - ((np.arccos(np.inner(n,v2) / (np.linalg.norm(n) * np.linalg.norm(v2)))) * 180/np.pi))
    
    print("phi 1: %.2f" %(phi1))
    print("phi 2: %.2f" %(phi2))
        
    if v1[2] < 0:
        theta1 = theta1 - 90
    else:
        theta1 = -(90 - theta1)
        
    if v2[2] < 0:
        theta2 = theta2 - 90
    else:
        theta2 = -(90 - theta2)
        
    print("these are the angles to rotate:")
    print("theta 1: %.2f" %(theta1))
    print("theta 2: %.2f" %(theta2))
    print("phi 1: %.2f" %(phi1))
    print("phi 2: %.2f" %(phi2))
    
    return theta1, theta2, phi1, phi2


with h5py.File('/scratch/fhgfs/doctor/moded_Icosahedron/AMO/250_pattern/stick_rot.h5', "r") as f:
    f2 = f['real'][:,:,:].astype(np.float64)

with h5py.File('/scratch/fhgfs/doctor/moded_Icosahedron/AMO/250_pattern/stick.h5', "r") as f:
    f1 = f['real'][:,:,:].astype(np.float64)     

fsc = FSC(f1,f2)

fig = plt.figure()
ax = fig.add_subplot(121)
ax.imshow(np.abs(f1.sum(axis=2)), cmap='plasma')
ax.plot(14.5,14.5,'wo')
ax.plot(24,14.5,'wo')
ax1 = fig.add_subplot(122)
ax1.imshow(np.abs(f2.sum(axis=2)), cmap='plasma')
ax1.plot(14.5,14.5,'wo')
ax1.plot(17,10,'wo')
plt.show()

#center of mass f1

cm11 = np.array(ndimage.measurements.center_of_mass(f1))
print(cm11)

cm12 = ndimage.measurements.center_of_mass(f1[:,24:,:])
print(cm12)
cm12 = np.array((14.5, 24, 14.5))
print(cm12)

#center of mass f1

cm21 = np.array(ndimage.measurements.center_of_mass(f2))
print(cm21)

cm22 = ndimage.measurements.center_of_mass(f2[:12,15:,:])
cm22 = np.array((10.299, 16.954, 21.223))
#cm22 = np.array((11.299, 15.954, 22.223))
print(cm22)

angles = vector_align(cm11,cm12,cm21,cm22)
print(angles[0])

f2 = ndimage.interpolation.rotate(f2, angles[3], axes=(0,1), reshape=False, mode='wrap') 
f2 = ndimage.interpolation.rotate(f2, angles[1], axes=(1,2), reshape=False, mode='wrap')

fig = plt.figure()
ax = fig.add_subplot(121)
ax.imshow(np.abs(f1.sum(axis=2)), cmap='plasma')
ax1 = fig.add_subplot(122)
ax1.imshow(np.abs(f2.sum(axis=2)), cmap='plasma')
plt.show()

#fsc = FSC(f1, f2)
#print len(fsc)

fsc_2 = FSC(f1,f2)
# index/pixel in resolution
res = []
for i in range(1,26):
    res.append(1.24E-9/(2*((i*75E-6)/np.sqrt(((i*75E-6)**2+0.4**2)))))
    
print(res)

res_round = [ '%.1e' % elem for elem in res ]

fig = plt.figure(figsize=((15,5)))
ax = fig.add_subplot(121)
ax.plot(np.arange(len(res)),np.abs(fsc), color='b')
#ax.set_xticklabels(res_round)
ax.set_xlabel('pixels')
ax.axhline(1/np.exp(1), color='r', label='1/e')
ax.axvline(15, color='k', linestyle='-.', label='detector edge')
ax.axvline(21.21, color='k', linestyle='--', label='corner 2D detector')
ax.axvline(25, color='k', label='corner 3D image')
ax.legend(loc='upper right')
ax.set_title('before alignment')

ax1 = fig.add_subplot(122)
ax1.plot(np.arange(len(res)),np.abs(fsc_2), color='b')
ax1.set_xticklabels(res_round)
ax1.set_xlabel('resolution')
ax1.axhline(1/np.exp(1), color='r', label='1/e')
ax1.axvline(15, color='k', linestyle='-.', label='detector edge')
ax1.axvline(21.21, color='k', linestyle='--', label='corner 2D detector')
ax1.axvline(25, color='k', label='corner 3D image')
ax1.legend(loc='left')
ax1.set_title('after alignment')
plt.show()
