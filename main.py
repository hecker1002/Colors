import cv2
import pandas as pd 


path = r"C:\Users\HP\OneDrive\Desktop\Github\example1.jpg"
img = cv2.imread(path) 


click = False 
r= g = b = x_m = y_m = 0

index = ["color"  , "color_name" , "hex" , "R" , "G" , "B"]
colors = pd.read_csv('my_colors.csv' , names = index , header = None)

def get_color_names ( R, G , B , colors) :
    
    minm = 10000 
    for j in range(len(colors)):
        d = abs(R - int(colors.loc[j , "R"])) + abs(G - int(colors.loc[ j, "G"])) + abs(B- int(colors.loc[j , "B"]))
        if d<=minm :
            minm = d
            cname  = colors.loc[j , "color_name"]
            
                
    return cname
  
                
            
def draw_it (event , x , y , flags , param ) :
     if event == cv2.EVENT_LBUTTONDBLCLK:
            
            global b , g , r , click  , x_m , y_m
            click = True 
            x_m = x
            y_m = y
            b , g, r = img[y ,x]
            b = int(b)
            g = int(g)
            r =int(r)
            
               
                
cv2.namedWindow('image')
cv2.setMouseCallback('image' , draw_it) 
            
           



while True:


    cv2.imshow("image" , img)

    if click :
        
        
        cv2.rectangle (img , (20 , 20) , (740 , 60) , ( b, g, r) , -1) 
                
            
        text = get_color_names(r , g , b , colors)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            
        if(r + g+ b >= 600):
            cv2.putText(img , text , (50 , 50) , 2 , 0.8 , (0 , 0 , 0) , 2 , cv2.LINE_AA)
            
        click  = False 
            
                    
           
            
    if cv2.waitKey(20) & 0xFF == 27 :
        break
        

cv2.destroyAllWindows()
            

       
                