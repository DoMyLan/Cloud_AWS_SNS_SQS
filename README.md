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
1. Tạo một instance trên EC2
Đặt tên cho instances và chọn AMIs là Ubutu
<img width="941" alt="Screenshot 2022-12-23 151810" src="https://user-images.githubusercontent.com/115056835/209303883-c3ba51db-c640-46f4-8e43-fe6a12ba8c53.png">










