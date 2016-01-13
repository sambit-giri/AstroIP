def circle(array, rad, xx, yy):
	array1=array
	m = array.shape[0]
	n = array.shape[1]
	for i in range(-rad,rad+1):
		for j in range(-rad,rad+1):
			x=xx+i
			y=yy+j
			rr2=i*i+j*j
 	  		if x < 0: x=x+m
			if x >= m: x=x-m
 			if y < 0: y=y+n
			if y >= n: y=y-n
			#print x,y
			if rr2<=rad*rad:
				array1[x,y]=1
	return array1

def rectangle(array, l, b, xx, yy):
	array1=array
	m = array.shape[0]
	n = array.shape[1]
	for i in range(-l/2,l/2+1):
		for j in range(-b/2,b/2+1):
			x=xx+i
			y=yy+j
 	  		if x < 0: x=x+m
			if x >= m: x=x-m
 			if y < 0: y=y+n
			if y >= n: y=y-n
			array1[x,y]=1
	return array1

def sphere(array, rad, xx, yy, zz):
	array1=array
	l = array.shape[0]
	m = array.shape[1]
	n = array.shape[2]
	for i in range(-rad,rad+1):
		for j in range(-rad,rad+1):
			for k in range(-rad,rad+1):
				x=xx+i
				y=yy+j
				z=zz+k
				rr2=i*i+j*j+k*k
 	  			if x < 0: x=x+l
				if x >= l: x=x-l
 				if y < 0: y=y+m
				if y >= m: y=y-m
 				if z < 0: y=y+n
				if z >= n: y=y-n
				if rr2<=rad*rad:
					array1[x,y,z]=1
	return array1
