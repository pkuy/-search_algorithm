import math
import matplotlib.pyplot as plt
 # Hàm mở file, file chứa ma trận
def read_file(A,S,E):          #A là ma trận dùng để lưu bản đồ sau khi đọc file, S để lưu vị trí bắt đầu
    file = open("graph1.txt",'r')   #E để lưu vị trí thoát ra của bản đồ
    rows=0
    colums=0
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
# Ước tính chi phí từ các điểm trên bản đồ để đến được điểm position theo như thuật toán
# Dùng pytago để ước tính chi phí, vì đường đi ngắn nhất là đường chéo
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
def find_end(A,B,Z,S,E): #B là ma trận phụ, có chung kích thước với A dùng để lưu những điểm đã được xét qua
    x=S[0]               #Z để lưu kích thước,S lưu điểm bắt đầu,E lưu điểm kết thúc
    y=S[1]
    B[x][y]='o'
    min=0
    k=0
    t=0              # t để lưu chi phí để đi từ điểm bắt đầu đến điểm được xét
    Arr=[]      # các phần tử trong mảng được lưu theo thứ tự: tọa độ x điểm 1, tọa độ y điểm 1, chi phí điểm 1 ; tương tự về sau
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
def find_start(A,B,Z,S,E,Way):
    x=E[0]
    y=E[1]
    B[x][y]='1'
    min=Z[0]*Z[1]
    Arr=[]
    k=0
    while(x!=S[0] or y!=S[1]):
        Way.append(y)
        Way.append(x)
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
        for i in range(len(Arr)):     # Chọn ra điểm có số thứ tự nhỏ nhất trong tập chờ
            if i%2==0:
                if A[Arr[i]][Arr[i+1]]<min:
                    x=Arr[i]
                    y=Arr[i+1]
                    min=A[x][y]
        B[x][y]='1'              # Đánh dấu đường đi tối giản
        k+=1                      # Trả về chi phí đường đi
    Way.reverse()
    return k
#Hàm xuất bản đồ kết quả
def write_file(A,B,Z,S,E,Way):
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
    plt.show()
A=[]
Way=[]
S=[0,0]
E=[0,0]
Z=read_file(A,S,E)      # trả về kích thước của ma trận sau khi đọc file
heuristic(A,Z,E)
B = []
for i in range(Z[0]):
    B.append([])
    for j in range(Z[1]):
        B[i].append('x')
if find_end(A,B,Z,S,E) == 1:
    print("Da tim duoc duong di!!!")
    k=find_start(A,B,Z,S,E,Way)
    print("Chi phi: ",k)              #in chi phí
    write_file(A,B,Z,S,E,Way)
else:
    print("Khong tim duoc duong di!!!")
