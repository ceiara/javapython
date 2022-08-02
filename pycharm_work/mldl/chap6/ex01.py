import cv2
import numpy as np
import matplotlib.pyplot as plt


rp = cv2.imread('rp.jpg',cv2.IMREAD_GRAYSCALE)
print(rp.shape)
print(rp[0,:])
# pltrp = cv2.cvtColor(rp, cv2.COLOR_BGR2RGB)
# np.save('a.npy',pltrp)

# pltrp = np.load('a.npy')

plt.scatter([10,20,30], [10,20,30], s=100)
plt.text(100, 200, 'yeahyeah')
# plt.axes(off)
plt.imshow(rp, cmap='gray_r')
plt.show()
