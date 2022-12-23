# TÊN ĐỀ TÀI "TÌM HIỂU VỀ DỊCH VỤ SNS & SQS CỦA AMAZON WEB SERVICE"
## Project Name: Cloud_AWS_SNS_SQS

## Project use DynamoDB + EC2 + Lambda + VPC + SQS + SNS

## 🔗 Thành viên
- Đỗ Thị Mỹ Lan - 20110666
- Bùi Quốc Tĩnh - 20110737
- Nguyễn Hữu Đạt - 20110630

## 🔗 Các chức năng chính
- Đăng ký tài khoản trên website
- Đăng nhập vào hệ thống
- Thay đổi số dư trong tài khoản
- Gửi tin nhắn đến khách hàng qua email về sự thay đổi số dư này.

## Công nghệ sử dụng
1. Ngôn ngữ: Python 
2. Thư viện: boto3, Flask framework.
3. Database: DynamoDB

## Thực thi trên localhost
Clone project "Cloud_AWS_SNS_SQS" with github

```bash
  git clone https://github.com/DoMyLan/Cloud_AWS_SNS_SQS.git
```
Truy cập thư mục chứa project DYNAMODB_FLASK
```bash
  cd WEB_CLOUD_DEMO
```
Chạy file run.py
```bash
  python run.py
```
Lưu ý: Nên sử dụng thư viện ảo app đã có sẵn khi clone về.

## Deploy Web lên AWS
### Tạo 1 instance trên EC2
1. Chọn AMIs là ubuntu
<img width="411" alt="image" src="https://user-images.githubusercontent.com/115056835/209304713-228f0032-c73a-46c2-be18-c5d1d307b94f.png">
2. Tạo sẵn 1 VPC "Public_Access"
<img width="442" alt="image" src="https://user-images.githubusercontent.com/115056835/209305199-530fd3b8-bdee-43ce-a653-b724b685f4ab.png">











