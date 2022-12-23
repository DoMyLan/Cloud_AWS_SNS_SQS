# TÊN ĐỀ TÀI:  "TÌM HIỂU VỀ DỊCH VỤ SNS & SQS CỦA AWS"
## Project Name: Cloud_AWS_SNS_SQS

## Project use: DynamoDB + EC2 + Lambda + VPC + SQS + SNS

## Thành viên
- Đỗ Thị Mỹ Lan - 20110666
- Bùi Quốc Tĩnh - 20110737
- Nguyễn Hữu Đạt - 20110630

## Các chức năng chính
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
Truy cập thư mục chứa project
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
<img width="439" alt="image" src="https://user-images.githubusercontent.com/115056835/209306026-a6b8bacc-6d5c-492c-94cf-5d295748878d.png">
2. Chọn instaces types và keypair
<img width="438" alt="image" src="https://user-images.githubusercontent.com/115056835/209306112-bb91d035-3339-4ac4-9b9d-38035c382f15.png">
3. Tạo sẵn 1 VPC "Public_Access"
<img width="439" alt="image" src="https://user-images.githubusercontent.com/115056835/209306320-7af705cc-d651-43e6-a826-7c391f538e46.png">
---->Hoàn tất khởi tạo 1 instance

### Kết nối instance vừa tạo với máy ảo ubuntu
<img width="451" alt="image" src="https://user-images.githubusercontent.com/115056835/209307181-bbbada5d-1d82-4340-93da-e46ba03e78be.png">

### Khi được chuyển đến giao diện như hình là ta đã kết nối thành công
<img width="956" alt="image" src="https://user-images.githubusercontent.com/115056835/209307604-c3a776dc-7b3f-4557-a0dc-3def2c9e9c89.png">

Cài đặt và update máy ảo ubuntu
```bash
  sudo apt update
```
Install gói phần mềm "software-properties-common"
```bash
  sudo apt install software-properties-common
```
Cài đặt thêm một số công cụ hỗ trợ sử dụng python 
```bash
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt install python3.8
  sudo apt install git
  sudo apt-get install python3-pip
```
Kiểm tra version của python
```bash
  python3.8 --version
```

Clone project "Cloud_AWS_SNS_SQS" with github
```bash
  git clone https://github.com/DoMyLan/Cloud_AWS_SNS_SQS.git
```

Sử dụng port 5555
```bash
  sudo ufw allow 5000
```

Đi đến thư mục Cloud_AWS_SNS_SQS
```bash
  cd Cloud_AWS_SNS_SQS
```

Cài đặt thư viện
```bash
  pip3 install -r requirements.txt
```

Cấu hình lại file run.py
```bash
  from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
```

Chạy project trên máy ảo ubuntu 
```bash
  python3 run.py
```

DONE !!! TA THỰC THI CÁC THAO TÁC VỚI PROJECT NHƯ CHẠY TRÊN LOCALHOST





