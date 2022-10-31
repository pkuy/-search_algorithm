![image](https://user-images.githubusercontent.com/96604342/199021982-f9fbfbdf-00fa-4636-b26e-fa2f38adae93.png)
<p>• Ký hiệu ngôi sao đại diện cho vị trí xuất phát của tác nhân.
<p>• Ký hiệu x thể hiện các bức tường và tác nhân sẽ không thể di
chuyển lên các vị trí này.
<p>• Ký hiệu + thể hiện các ô điểm thưởng mà nếu tác nhân di chuyển
vào các ô này sẽ được giảm chi phí thực hiện đường đi.
<p>1 Cơ sở trí tuệ nhân tạo Thuật toán tìm kiếm
<p>• Ký hiệu exit đại diện cho vị trí đích mà tác nhân cần di chuyển
đến, là vị trí duy nhất mà tác nhân có thể thoát khỏi mê cung.
Mục tiêu của các bạn sinh viên là cài đặt các thuật toán tìm kiếm
đường đi từ vị trí xuất phát đến vị trí đích (vị trí thoát khỏi mê cung)
cho tác nhân. Trong đó tác nhân chỉ có thể di chuyển lên, xuống, trái,
phải với chi phí bằng nhau. Các bạn cần cài đặt các thuật toán sau:
<p>• Thuật toán tìm kiếm có thông tin:
<p>– Thuật toán tìm kiếm tham lam (Greedy Best First Search).
<p>– Thuật toán tìm kiếm A*.
<p>2
Cơ sở trí tuệ nhân tạo Thuật toán tìm kiếm
<p>Về bản đồ trò chơi, sẽ có hai loại: bản đồ không có điểm thưởng và
bản đồ có điểm thưởng. Nhiệm vụ của các bạn là cài đặt các thuật
toán tìm kiếm và tự thiết kế các bản đồ cho hai loại trên.
<p>• Với trường hợp bản đồ không có điểm thưởng (80%), các bạn sẽ
cài đặt 4 thuật toán trên để giải quyết. Các bạn sẽ tự thiết kế
và báo cáo khoảng 5 bản đồ tiêu biểu (các bạn nên chọn những
bản đồ mà các thuật toán có sự khác biệt với nhau nhiều) và so
sánh sự khác nhau giữa cách tìm đường đi trong các loại bản đồ
này với từng chiến lược khác nhau. Cụ thể với một bản đồ được
chọn để báo cáo, các bạn sẽ nhận xét:
<p>– Sự khác nhau giữa các chiến lược tìm kiếm đối với bản đồ
này được thể hiện như thế nào? Các bạn cần có hình vẽ
bản đồ output đường đi để minh họa và vận dụng lý thuyết
về tính đầy đủ và tối ưu của các thuật toán để giải thích.
<p>– Với các chiến lược tìm kiếm có thông tin, các bạn có thể
chọn nhiều hàm heuristic khác nhau và báo cáo sự khác
nhau giữa các chiến lược đối với từng hàm heuristic.
<p>• Với trường hợp bản đồ có điểm thưởng (20%), các bạn sẽ suy
nghĩ cách giải quyết và đề xuất chiến lược để tác nhân di chuyển
sao cho chi phí đường đi từ điểm bắt đầu đến điểm thoát khỏi
mê cung là nhỏ nhất có thể (lưu ý rằng tác nhân không nhất
thiết phải đi qua hết các điểm thưởng). Các bạn cần thiết kế
bản đồ với tối thiểu 3 trường hợp: có 2, 5, 10 điểm thưởng với
giá trị khác nhau trên bản đồ. Nếu các bạn không thể tìm được
lời giải tối ưu (bất kể trong trường hợp số lượng điểm thưởng
là nhiều hay ít), hãy đề xuất chiến lược heuristic để giải quyết,
chẳng hạn tham lam ăn tất cả điểm thưởng theo độ lớn giá trị
của chúng rồi mới tìm đường thoát khỏi mê cung.
<p>• Kích thước của các bản đồ được chọn để báo cáo phải đảm bảo
có ít nhất một bản đồ lớn (chiều dài và chiều rộng của bản đồ
phải có một số ít nhất bằng 15 và một số ít nhất bằng 35).
<p>3
Cơ sở trí tuệ nhân tạo Thuật toán tìm kiếm
<p>• Số lượng bản đồ tối thiểu cần báo cáo và phân tích: 5 bản đồ
đối với bản đồ không có điểm thưởng và 3 bản đồ đối với bản
đồ có điểm thưởng.
Các bạn tham khảo hàm vẽ bản đồ ở notebook sau: link
Thiết kế kịch bản kiểm thử và bản đồ
Mỗi kịch bản kiểm thử được thiết kế như sau:
<p>• Dòng đầu là số lượng điểm thưởng n (n = 0 với bản đồ không
có điểm thưởng).
<p>• n dòng tiếp theo, mỗi dòng sẽ bao gồm 3 số nguyên x,y, z với
x,y là tọa độ của điểm thưởng trong ma trận; z là giá trị của
điểm thưởng, sẽ là các số nguyên âm.
<p>• Các dòng tiếp theo mô tả bản đồ của trò chơi. Các bạn lưu ý
điểm kết thúc của hành trình sẽ là điểm thoát khỏi mê cung (ví
dụ trong hình 2 thì điểm kết thúc sẽ là điểm ở dòng 2 và cột 0);
điểm bắt đầu của tác nhân được ký hiệu bằng ký tự S; các ký
tự x sẽ là các bức tường; các ký tự + sẽ là các điểm thưởng.
