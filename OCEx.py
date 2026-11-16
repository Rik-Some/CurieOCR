import cv2
import easyocr
import matplotlib.pyplot as plt
C=[]#capacitance
O=[]#Dielectric
T=[]#Temperature
#path
path=r'F:\Temp.png'
#extract img
img=cv2.imread(path)
#intiating reader
R=easyocr.Reader(['en'],gpu=True)
#extract txt
txt=R.readtext(img)

#Temperature extractor
for t in txt:
    coo,t,score=t
    #conversion of coordinates to int tuple
    pt1=list(map(int,coo[0]))
    pt2=list(map(int,coo[2]))
    #Temp extraction
    T1=list(t[0:])
    Tx="".join(T1)
    T.append(Tx)
    print(T)
    cv2.rectangle(img,pt1,pt2,(0,225,0),5)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

#path
path2=r'F:\Capa.png'
#extract img
img2=cv2.imread(path2)
#intiating reader
R2=easyocr.Reader(['en'],gpu=True)
#extract txt
txt2=R2.readtext(img2)

#dielectric calculator
for c in txt2 :
 coo,c,score=c
    #conversion of coordinates to int tuple
 pt1=list(map(int,coo[0]))
 pt2=list(map(int,coo[2]))
    #Temp extraction
 C1=list(c[0:])
 Cx="".join(C1)
 C.append(Cx)
    #BOX
 cv2.rectangle(img,pt1,pt2,(0,225,0),5)
def cal(C,O):
 for j in C:
  for i in j:
     o=(int(i)*1000)//(544.58)
     O.append(o)  
     return O       
cal(C,O)
#table
for y in range(len(C)):
   print("(",y+1,")","[",T[y],"|",C[y],"|",O[y],"] \n ___________________")
plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
plt.show()

#Graph plotter
plt.title("Curie Temp")
plt.xlabel("Temp")
plt.ylabel("Dielectric")
plt.scatter(T,O,color="Black")
plt.grid(color="Red")
plt.plot(T,O)
plt.show()