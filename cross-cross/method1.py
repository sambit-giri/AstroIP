import numpy as np
from head import cross2d, relate2d, separate2d, diff_image
from draw_shapes import circle
from random import randint
import matplotlib.pyplot as plt
import c2raytools as c2t


def crop_array(array, (xs, ys), (xl, yl)):
	return array[xs:xl, ys:yl]

def append_points(st_list, en_list, st, en):
	mid_x = (st[0]+en[0])/2
	mid_y = (st[1]+en[1])/2
	st_list.append(st)
	en_list.append((mid_x, mid_y))
	st_list.append((st[0],mid_y))
	en_list.append((mid_x,en[1]))
	st_list.append((mid_x,st[1]))
	en_list.append((en[0],mid_y))
	st_list.append((mid_x,mid_y))
	en_list.append(en)

def test_region(patch):
        #m1 = data.mean()
        m2 = patch.mean()
	m3 = patch[patch.shape[0]/2, patch.shape[1]/2]
	#print m2, m3
        if (m2 > 0.8):
                return True
        else:
                return  False

def put_mark(out, bub, count, (xs, ys), (xl, yl), reg):
	out[xs:xl, ys:yl] = count
        if(reg):
                bub[xs:xl, ys:yl] = 1
		

def make_input(xs,ys):
	arr=np.zeros((xs,ys))
	ns=30
	for i in range(0,ns):
		xx=randint(0,arr.shape[0])
		yy=randint(0,arr.shape[1])
		rr=randint(0,(arr.shape[0]+arr.shape[1])/20)
		arr=circle(arr, rr, xx, yy)
	return arr



def main():
	#data = make_input(256, 256)
	"""
	c2t.set_sim_constants(500)		#This function takes as its only parameter the box side in cMpc/h
	c2t.set_verbose(True)			#Get feedback

	xfile = c2t.XfracFile('/disk/dawn-1/sgiri/500Mpc_f2_0_300/xfrac3d_6.686.bin')
	xfrac=xfile.xi
	
	data = crop_array(xfrac[150,:,:], (0,0), (256,256))
	#data = data.T
	"""

	data = np.load('../sample-input/data.2D.npy')
	data = crop_array(data, (0,0), (256,256))

	out = np.ones((256, 256))
        bub_mat = np.zeros((256, 256))
	count = 0

	st = (0, 0)
	en = (data.shape[0], data.shape[1])

	st_list = []
	en_list = []
	append_points(st_list, en_list, st, en)

	control = True
	mar = 0
	#print control

	while(control):
		#print st, en
		st = st_list[0]
		en = en_list[0]
		st_list.pop(0)
		en_list.pop(0)

		check_ar = crop_array(data, st, en)
		rel = relate2d(check_ar)
		
		if(rel):
                           reg = test_region(check_ar)
			   #if (reg): mar=mar+1
			   print reg
                           put_mark(out, bub_mat, count, st, en, reg)
                           count = count+1
		else:
                           append_points(st_list, en_list, st, en)	

		if(len(st_list) == 0):
                           control = False

	#print data.mean()
	#bub_out = separate2d(bub_mat)
        plt.figure(0)
	plt.imshow(data)
	plt.colorbar()
	plt.figure(1)
	plt.imshow(out)
	plt.colorbar()
        plt.figure(2)
        plt.imshow(bub_mat)
        plt.colorbar()
	plt.figure(3)
	plt.imshow(diff_image(data)[0])
	plt.colorbar()
	plt.show()

	
main()





