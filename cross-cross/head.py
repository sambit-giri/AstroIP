import numpy as np



def cross2d(array):
	if len(array.shape) != 2:
		print "The dimension of the array is incorrect"
		return 0
	if (array.shape[0] % 2) or (array.shape[1] % 2):
		print "Use array with 2^n length"
		return 0

	l = array.shape[0]
	m = array.shape[1]

	ar1 = np.zeros((l/2,m/2))
	ar2 = np.zeros((l/2,m/2))
	ar3 = np.zeros((l/2,m/2))
	ar4 = np.zeros((l/2,m/2))

	for i in range(0,l/2):
		ar1[i,:] = np.split(array[i,:],2)[0]
		ar2[i,:] = np.split(array[i,:],2)[1]
		ar3[i,:] = np.split(array[l/2+i,:],2)[0]
		ar4[i,:] = np.split(array[l/2+i,:],2)[1]

	return (ar1,ar2,ar3,ar4)

def relate2d(array):
	# A method similar to cross correlation is used.
	if (array.shape[0] == 1 or array.shape[1] == 1):
		#print "True"
		return True
		
	(ar1, ar2, ar3, ar4) = cross2d(array)
	b1 = ar1
	b2 = np.zeros((ar2.shape[0], ar2.shape[1]))
	b3 = np.zeros((ar3.shape[0], ar3.shape[1]))
	b4 = np.zeros((ar4.shape[0], ar4.shape[1]))

	for i in range(0, ar2.shape[1]):
		b2[:,i] = ar2[:,ar2.shape[1]-1-i]

	for j in range(0, ar3.shape[0]):
		b3[j,:] = ar3[ar3.shape[0]-1-j,:]

	for k1 in range(0, ar4.shape[0]):
		for k2 in range(0, ar4.shape[1]):
			b4[k1,k2] = ar4[ar3.shape[0]-1-k1, ar3.shape[1]-1-k2]

	#return (b1, b2, b3, b4)
	dt = []
	dt.append(sum(sum(np.dot(b1,b2))))
	dt.append(sum(sum(np.dot(b1,b3))))
	dt.append(sum(sum(np.dot(b1,b4))))
	dt.append(sum(sum(np.dot(b2,b3))))
	dt.append(sum(sum(np.dot(b2,b4))))
	dt.append(sum(sum(np.dot(b3,b4))))

	err = 100*np.std(dt)/np.mean(dt)

	if err < 0.01:
		#print "True"
		return True
	else:
		#print "False"
		return False

def separate2d(array):
	out = np.zeros((array.shape[0], array.shape[1]))
	mark = 1
	neig = 0
	for i in range(1, array.shape[0]-1):
		for j in range(1, array.shape[1]-1):
			if (array[i, j] == 1):
				if (out[i-1,j]!=0): neig = out[i-1,j]
				if (out[i,j-1]!=0): neig = out[i,j-1]
				if (out[i-1,j]==0 and out[i,j-1]==0):
					neig = mark
					mark = mark + 1
				out[i,j] = neig
	return out


def diff_image(img):
	m = img.shape[0]
	n = img.shape[1]
	gx = np.zeros((m, n))
	gy = np.zeros((m, n))
	gx[:(m-1), :] = img[1:, :] - img[:(m-1), :]
	gy[:, :(n-1)] = img[:, 1:] - img[:, :(n-1)]
	dimg = np.fabs(gx)+np.fabs(gy)
	return (dimg, gx, gy)




