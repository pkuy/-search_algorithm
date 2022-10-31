import math
import matplotlib.pyplot as plt
 # Hàm mở file, file chứa ma trận
def read_file(A,S,E,point):         #A là ma trận dùng để lưu bản đồ sau khi đọc file, S để lưu vị trí bắt đầu
    file = open("bonus1.txt",'r')        #E để lưu vị trí thoát ra của bản đồ
    rows=0                          #point là list dùng để lưu các điểm thưởng có trong bản đồ
    colums=0
    k=int(file.readline())
    for i in range(k):
        data=file.readline()
        data=data.split(',')
        point.append([])
        for j in range(3):
            point[i].append(int(data[j]))
    while(True):
        data=file.readline()
        if data=='':
            break
        colums=len(data)
        A.append([])
        for i in range(colums):
            A[rows].append(0)
            if data[i]=='x':
                A[rows][i]=0
            elif data[i] == 'e':
                A[rows][i] = 2
                E[0] = rows
                E[1] = i
            elif data[i] == 's':
                A[rows][i] = 2
                S[0] = rows
                S[1] = i
            else:
                A[rows][i] = 1
        rows+=1
    file.close()
    return rows,colums
#Hàm để tính chi phí theo list thứ tự đường đi
def count(Way,point):      #Way là lish đường đi, point là list chứa các điểm thưởng
    k=0
    for i in range(len(Way)):
        if i%2==0:
            k+=1
            for j in range(len(point)):
                if Way[i]==point[j][0] and Way[i+1]==point[j][1]:
                    k=k+point[j][2]
    return k
#Hàm để tính chi phí từ position đi đến các điểm khác trên bản đồ theo đường đi ngắn nhất là đường chéo
def heuristic(A,Z,position): # A là ma trận lưu bản đồ, Z chứa kích thước ma trận A 
    t1=0
    t2=0
    for i in range(Z[0]):
        for j in range(Z[1]):
            if A[i][j]!=0:
                t1 = abs(i-position[0])+1
                t2 = abs(j-position[1])+1
                A[i][j] = math.sqrt(t1*t1+t2*t2)
                A[i][j]=round(A[i][j],1)
# Hàm để tìm điểm kết thúc(E) từ điểm bắt đầu (S)
def find_end(A,B,Z,S,E):  #B là ma trận phụ, có chung kích thước với A dùng để lưu những điểm đã được xét qua
    x=S[0]                #Z để lưu kích thước,S lưu điểm bắt đầu,E lưu điểm kết thúc
    y=S[1]
    min=0
    k=0
    t=0              # t để lưu chi phí để đi từ điểm bắt đầu đến điểm được xét
    Arr=[]
    for i in range(Z[0]):
        for j in range(Z[1]):
            B[i][j]='x'
    B[x][y]='o'
    while(x!=E[0] or y!=E[1]):
        k+=1
        A[x][y]=k
        B[x][y]='o'                             # Đánh số tăng dần cho những điểm đã xét
        if A[x-1][y] != 0 and B[x-1][y]!= 'o' and B[x-1][y]!= 't': # nếu những vị trí ở A khác 0 (không phải tường)
            Arr.append(x-1)                                        # và ở B khác o (chưa được xét) sẽ được đưa vào để xét
            Arr.append(y)                                          # và ở B khác t (đã ở trong hàng chờ)
            Arr.append(t+1)
            B[x-1][y]='t'
        if A[x][y-1] != 0 and B[x][y-1]!= 'o' and B[x][y-1]!= 't':
            Arr.append(x)
            Arr.append(y-1)
            Arr.append(t+1)
            B[x][y-1]='t'
        if A[x+1][y] != 0 and B[x+1][y]!= 'o'and B[x+1][y]!= 't':
            Arr.append(x+1)
            Arr.append(y)
            Arr.append(t+1)
            B[x+1][y]='t'
        if A[x][y+1] != 0 and B[x][y+1]!= 'o'and B[x][y+1]!= 't':
            Arr.append(x)
            Arr.append(y+1)
            Arr.append(t+1)
            B[x][y+1]='t'
        min = Z[0]*Z[1]
        if len(Arr)==0:
            return 0
        for i in range(len(Arr)):            # Chọn ra điểm có ước lượng chi phí nhỏ nhất trong trong tập chờ
            if i%3==0:
                if A[Arr[i]][Arr[i+1]] + Arr[i+2]<min:
                    x=Arr[i]
                    y=Arr[i+1]
                    t=Arr[i+2]
                    min=A[x][y] + t
        for i in range(len(Arr)):            # Xóa điểm được chọn ra khỏi tập chờ
            if i%3==0:
                if Arr[i]==x and Arr[i+1]==y and Arr[i+2]==t:
                    Arr.pop(i+2)
                    Arr.pop(i+1)
                    Arr.pop(i)
                    break
    return 1
# Hàm để tìm lại đường đi tối giản, bằng cách cho chạy ngược lại từ E đến S
# Trong tập những điểm đã được xét qua
def find_start(A,B,Z,S,E,Way):  #Way là một list chứa đường đi
    x=E[0]
    y=E[1]
    B[x][y]='1'
    min=Z[0]*Z[1]
    Arr=[]
    Temp=[]                # tạo list để lưu đường đi tối giản
    k=0
    while(x!=S[0] or y!=S[1]):
        Temp.append(y)
        Temp.append(x)
        if x!=0:    
            if B[x-1][y] == 'o':      #Những điểm có giá trị trong B là o sẽ được thêm vào tập chờ
                Arr.append(x-1)
                Arr.append(y)
        if y!=0:
            if B[x][y-1]== 'o':
                Arr.append(x)
                Arr.append(y-1)
        if x!= Z[0]-1:
            if B[x+1][y]== 'o':
                Arr.append(x+1)
                Arr.append(y)
        if y!= Z[1]-1:
            if B[x][y+1]== 'o':
                Arr.append(x)
                Arr.append(y+1)
        for i in range(len(Arr)):          # Chọn ra điểm có số thứ tự nhỏ nhất trong tập chờ
            if i%2==0:
                if A[Arr[i]][Arr[i+1]]<min:
                    x=Arr[i]
                    y=Arr[i+1]
                    min=A[x][y]
        B[x][y]='1'              # Đánh dấu đường đi tối giản
        k+=1
    Temp.reverse()              # đảo list temp lại để được xếp theo thứ tự từ S đến E
    Way+=Temp                   # lưu thêm temp vào Way

#Hàm để tìm những đường đi từ một list đường đi ban đầu truyền vào đến một điểm thưởng rồi đến đích
#Mà chi phí có thể nhỏ hơn chi phí của đường đi tốt nhất hiện tại và lưu vào Way_list
def Point(A,B,Z,E,point,Min,point_list,Way_list,way,x): #Min là chi phí nhỏ nhất hiện tại
# point_list là list để lưu các list điểm thưởng mà đường đi                                 
# # có đi qua được lưu trong Way_list
# Way_list là list để lưu các list đường đi 
# Way là list đường đi được đem ra xét tiếp
# x lưu vị trí của list được xét trong point_list và Way_list
    temp_point=[]                          # tạo ra list phụ để lưu point 
    temp_point+=point                           
    k=len(point_list[x])                          
    for i in range(k):                     # điểm thưởng trong list phụ trùng với điểm thưởng đã có trong point_list[x] 
        if i%2==0:                         # thì sẽ bị xóa
            for j in range(len(temp_point)):
                if temp_point[j][0]==point_list[x][i] and temp_point[j][1]==point_list[x][i+1]:
                    temp_point.pop(j)
                    break
    P=[]                        # tạo P để lưu điểm thưởng cuối cùng xong point_list[x] được xét
    P.append(point_list[x][k-2])
    P.append(point_list[x][k-1])
    for i in range(len(temp_point)):
        list_w=[]                    # tạo list_w để lưu đường đi
        list_w+=way                  # lưu way vào list_w
        # Tìm đường đi từ P đến 1 điểm thưởng trong temp_point
        heuristic(A,Z,temp_point[i])
        find_end(A,B,Z,P,temp_point[i])
        find_start(A,B,Z,P,temp_point[i],list_w)
        # Tìm đường đi từ điểm thưởng được chọn đến E
        heuristic(A,Z,E)
        find_end(A,B,Z,temp_point[i],E)
        find_start(A,B,Z,temp_point[i],E,list_w)

        temp=Min                                 # tạo temp để lưu Min
        for j in range(len(temp_point)):
            if temp_point[j]!=temp_point[i]:
                temp-=temp_point[j][2]

        if count(list_w,point)<temp:            # Nếu như chi phí của đường đi vừa tìm đươc nhỏ hơn temp 
            Way_list.append([])                 # Thì lưu điểm thưởng được chọn vào point_list[x]
            Way_list[len(Way_list)-1]+=list_w   # Lưu đường đi vừa mới tìm và Way_list
            point_list.append([])
            point_list[len(point_list)-1]+=point_list[x]
            point_list[len(point_list)-1].append(temp_point[i][0])
            point_list[len(point_list)-1].append(temp_point[i][1])
# Dùng để tìm những đường đi qua điểm thưởng có chi phí nhỏ hơn đường đi ban đầu nếu có
def Point_map(A,B,Z,S,E,point,Min,Best_Way): #Best_Way là đường đi tốt nhất,Min là chi phí nhỏ nhất
    Way_list=[]                              # tạo Way_list để lưu các đường đi 
    Way_list.append([])        
    Way_list[0]+=Best_Way                    # thêm Best_way vào Way_list
    point_list=[]                         # tạo point_list để lưu danh sách các điểm thưởng mà đường đi tương ứng trong way_list đi qua
    point_list.append([])
    point_list[0].append(S[0])
    point_list[0].append(S[1])
    way=[]
    while len(point_list)>0:
        i=0
        k=len(point_list)
        while i<k:
            way.clear()
            way+=Way_list[i] # lưu đường đi đang được xét vào Way
            # Xóa đường đi từ điểm thưởng xa nhât đến E( điểm kết thúc)
            while way[len(way)-2] != point_list[i][len(point_list[i])-2] or way[len(way)-1] != point_list[i][len(point_list[i])-1]:
                way.pop()
                way.pop()
                if len(way)==0:
                    break
            Point(A,B,Z,E,point,Min,point_list,Way_list,way,i)
            temp =count(Way_list[i],point)        #tạo temp để lưu chi phí đường đi đang được xét
            if temp<Min:                          # tìm đường đi có chi phí nhỏ nhất
                Min=temp
                Best_Way.clear()
                Best_Way+=Way_list[i]
            point_list.pop(i)                    #xóa đường đi sau khi đã xét xong
            Way_list.pop(i)
            k-=1
# đây là hàm viết lại đường đi ngắn nhất vào ma trân B để chuẩn bị viết file
def write_way(B,Z,Best_Way,point):
    for i in range(Z[0]):
        for j in range(Z[1]):
            B[i][j]='x'
    for i in range(len(Best_Way)):
        if i%2==0:
            if B[Best_Way[i]][Best_Way[i+1]]=='1':
                B[Best_Way[i]][Best_Way[i+1]]='2'
            else:
                B[Best_Way[i]][Best_Way[i+1]]='1'
    for i in range(len(point)):
        B[point[i][0]][point[i][1]]='3'
#Hàm xuất bản đồ kết quả
def write_file(A,B,Z,S,E,point,Way):
    ax=plt.figure(figsize=(15,7))
    for i in range(len(Way)-2):
        if i%2==0:
            if Way[i]<Way[i+2]:
                B[Way[i]][Way[i+1]]='v'
            elif Way[i]>Way[i+2]:
                B[Way[i]][Way[i+1]]='^'
            elif Way[i+1]<Way[i+3]:
                B[Way[i]][Way[i+1]]='>'
            elif Way[i+1]>Way[i+3]:
                B[Way[i]][Way[i+1]]='<' 
    for i in range(len(Way)-2):
        if i%2==0:
            plt.scatter(Way[i+1],Z[0]-Way[i],marker=B[Way[i]][Way[i+1]],s=100,color='silver')
    for i in range(Z[0]):
        for j in range(Z[1]):
            if A[i][j]==0:
                plt.scatter(j,Z[0]-i,marker='X',s=100,color='black')
            elif i==S[0] and j==S[1]:
                plt.scatter(j,Z[0]-i,marker='*',s=100,color='gold')
            elif i==E[0] and j==E[1]:
                plt.text(j,Z[0]-i,'EXIT',color='red',horizontalalignment='center',verticalalignment='center')
    for i in range(len(point)):
        plt.scatter(point[i][1],Z[0]-point[i][0],marker='+',s=100,color='green')
    plt.show()
A=[]
point=[]    # để lưu các điểm thưởng trên bản đồ
Best_Way=[] # để lưu đường đi tốt nhất
Min=[]
S=[0,0]
E=[0,0]
Z=read_file(A,S,E,point)   # lưu kích thước ma trận sau khi đọc file
heuristic(A,Z,E)           
B = []
for i in range(Z[0]):
    B.append([])
    for j in range(Z[1]):
        B[i].append('x')
if find_end(A,B,Z,S,E)==1:
    print("Da tim duoc duong di !!!")
    # Tìm đường đi mà không cần xét điểm thưởng
    find_start(A,B,Z,S,E,Best_Way)
    Min=count(Best_Way,point)
    # Tim đường đi có xét các điểm thưởng
    Point_map(A,B,Z,S,E,point,Min,Best_Way)
    # In chi phí
    Min=count(Best_Way,point)
    print("Chi phí: ",Min)           
    write_file(A,B,Z,S,E,point,Best_Way)
else:
    print("Khong tim duoc duong di !!!")