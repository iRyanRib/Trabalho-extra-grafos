# importing the module
import cv2
import math
list_coordinatesx = []
list_coordinatesy = []
list_dist= []
matadj = []
rota_maiscurta = []
distTotal_pixel = 0
distTotal_km = 0
#função para pegar as coordenadas do clique
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # displaying the coordinates
        # on the Shell
        list_coordinatesx.append(x)
        list_coordinatesy.append(y)
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
# driver function
if __name__=="__main__":
    
    # reading the image
    img = cv2.imread('base.png', 1)
 
    # displaying the image
    cv2.imshow('image', img)
    
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    print(list_coordinatesx)
    print(list_coordinatesy)
    for x in range(len(list_coordinatesx)):
        for i in range(len(list_coordinatesx)):
            a = list_coordinatesx[i] - list_coordinatesx[x]
            b = list_coordinatesy[i] - list_coordinatesy[x]
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            list_dist.append(c)
        matadj.append(list_dist)
        list_dist = []
    print(matadj)
#------------------------------------------------------------------------------------------
    #algoritimo de prim
    INF = 9999999
    #numero de vértices do grafo
    V = len(list_coordinatesx)
    #matriz de adjascencia
    G = matadj
    # create a array to track selected vertex
    # selected will become true otherwise false
    selected = []
    for i in range(len(list_coordinatesx)):
        selected.append(0)
    # set number of edge to 0
    no_edge = 0
    # the number of egde in minimum spanning tree will be
    # always less than(V - 1), where V is number of vertices in
    # graph
    # choose 0th vertex and make it true
    selected[0] = True
    # print for edge and weight
    print("Edge : Weight\n")
    while (no_edge < V - 1):
        # For every vertex in the set S, find the all adjacent vertices
        #, calculate the distance from the vertex selected at step 1.
        # if the vertex is already in the set S, discard it otherwise
        # choose another vertex nearest to selected vertex  at step 1.
        minimum = INF
        h = 0
        m = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                        # not in selected and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            h = i
                            m = j
        print(str(h) + "-" + str(m))
        distTotal_pixel+= G[h][m]
        rota_maiscurta.append((h,m))      
        selected[m] = True
        no_edge += 1
        # close the window
        cv2.destroyAllWindows()
    #1 Pixel [px] = 0,026 458 333 333 333 Centímetro [cm] 
    distTotal_km = ((distTotal_pixel*0.026)*100)
    print("Distancia total em km:",distTotal_km)
