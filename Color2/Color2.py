import cv2 
import numpy as np


def figColor(imageHSV):
	yellowBajo = np.array([15,100,20],np.uint8)
	yellowAlot = np.array([45,255,255],np.uint8)
	blueBajo = np.array([100,100,20],np.uint8)
	blueAlto= np.array([125,255,20],np.uint8)
	greenAlto= np.array([125,255,20],np.uint8)
	greenBajo= np.array([125,255,20],np.uint8)
	redBajo= np.array([0,100,20],np.uint8)
	redAlto= np.array([8,255,255],np.uint8)
	redBajo1= np.array([0,100,20],np.uint8)
	redAlto1= np.array([8,255,255],np.uint8)
	maskYellow = cv2.inRange(imageHSV,yellowBajo,yellowAlot)
	maskBlue = cv2.inRange(imageHSV,blueBajo,blueAlto)
	maskgreen = cv2.inRange(imageHSV,greenAlto,greenBajo)
	maskgreen = cv2.inRange(imageHSV,greenAlto,greenBajo)
	maskRed = cv2.inRange(imageHSV,redAlto,redBajo)
	maskRed1 = cv2.inRange(imageHSV,redAlto1,redBajo1)
	maskRedcomp = cv2.inRange(imageHSV,maskRed,maskRed1)

	cntsRed = cv2.findCountours(maskRedcomp,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsYellow = cv2.findCountours(maskYellow,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsBlue = cv2.findCountours(maskBlue,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsgreen = cv2.findCountours(maskgreen,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	color ='x'
	if len(cntsRed)>0: color = 'rojo'
	elif len(cntsYellow)>0:color = 'Amarillo'
	elif len(cntsBlue)>0:color ='Azul'
	elif len(cntsgreen)>0:color = 'verde'
	return color

def figName(contorno,width, higth):
	namefig='x'
	epsilon =0.01 * cv2.arcLength(contorno,True)
	approx = cv2.approxPolyDP(contorno,epsilon,True)
	if(approx)==3 : 
		namefig = 'triangulo'
	if (approx)==4:
		res = float(width)/higth
		if res>=1:
			namefig ='Cuadrado'
		else:
			namefig = 'Rectangulo'

	if(approx)== 5:
		namefig ='Pentagono'
	if(approx)==6:
		namefig = 'Hexagono'
	if(approx)>10:
		namefig= 'Circulo'  
	
	return namefig

imge = cv2.imread('f.jpg')
gray = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,10,150)
canny = cv2.dilate(canny,None,iterations=1)
canny = cv2.erode(canny, None, iterations =1)

contorno, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

imageHSV = cv2.cvtColor(imge,cv2.COLOR_BGR2HSV)

for c in contorno:
	x,y,w,h = cv2.boundingRect(c)

	imgAux = np.zeros(imge.shape[:2],dtype='uint8')
	imgAux = cv2.drawContours(imgAux,[c],-1,255,-1)
	maskHSV = cv2.bitwise_and(imageHSV,imageHSV,mask=imgAux)
	figAll=figName(c,w,h)+' '+ figColor(maskHSV)
	cv2.putText(image,figAll(x,y,-5),1,1,(0,255,0),1)

cv2.imshow('imagen',image)
cv2.waitKey(0)
cv2.destroyAllWindows()