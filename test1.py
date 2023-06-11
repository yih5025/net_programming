import wiringpi

# MCP3008 SPI 채널 및 핀 번호
SPI_CHANNEL = 0
SPI_CE0_PIN = 8
# GPIO 핀 번호
buzzer_pin_1 = 1
buzzer_pin_2 = 24

# wPi 라이브러리 초기화
wiringpi.wiringPiSetup()

# PWM 모드 설정
'''import inspect
print(inspect.getfile(wiringpi))'''
wiringpi.pinMode(buzzer_pin_1, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(buzzer_pin_2, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(10) #소리 음량 조절
wiringpi.pwmSetRange(2000) 

wiringpi.pwmWrite(buzzer_pin_1,300)
wiringpi.pwmWrite(buzzer_pin_2, 300)
wiringpi.delay(2000)
# 부저 중지
wiringpi.pwmWrite(buzzer_pin_1, 0)
wiringpi.pwmWrite(buzzer_pin_2, 0)