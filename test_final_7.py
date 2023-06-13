import paramiko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SSH 접속 정보
ssh_host = 'ssh.example.com'
ssh_port = 22
ssh_username = 'your-username'
ssh_password = 'your-password'

# SFTP 설정
sftp_remote_path = '/remote/path/20191539.zip'
sftp_local_path = '20191539.zip'

# 이메일 설정
email_subject = '20191539.zip'
email_attachment_name = '20191539.zip'
email_sender = 'your-email@example.com'
email_receiver = 'daeheekim@sch.ac.kr'
email_password = 'your-email-password'

# SSH 접속 및 작업 수행
with paramiko.Transport((ssh_host, ssh_port)) as transport:
    transport.connect(username=ssh_username, password=ssh_password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 폴더 생성
    sftp.mkdir('20191539')

    # 파일 생성
    with sftp.open('20191539/iot.txt', 'w') as file:
        file.write('iot')

    # 폴더 압축
    sftp.get_channel().exec_command('zip -r 20191539.zip 20191539')

    # 파일 가져오기
    sftp.get('20191539.zip', sftp_local_path)

# 이메일 전송
msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = email_subject

part = MIMEBase('application', 'octet-stream')
part.set_payload(open(email_attachment_name, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename="{email_attachment_name}"')
msg.attach(part)

smtp = smtplib.SMTP('smtp.example.com', 587)
smtp.starttls()
smtp.login(email_sender, email_password)
smtp.sendmail(email_sender, email_receiver, msg.as_string())
smtp.quit()
