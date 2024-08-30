import ssd1306
from time import sleep
from machine import Pin, SoftI2C, PWM
from dht import DHT11
from utime import localtime

# 初始化PWM
S1 = PWM(Pin(4), freq=50, duty=0)

# 温湿度传感器定义
dht_pin = Pin(21, Pin.IN)
sensor = DHT11(dht_pin)

# 使用I2C协议，初始化OLED
i2c = SoftI2C(scl=Pin(23), sda=Pin(19))

# 定义OLED显示屏像素
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
S1.duty(77)
s
# 文件名定义
filename = 'sensor_data.txt'

while True:
    sleep(1)
    # 读取传感器数据
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    # 获取当前时间并手动格式化
    current_time_tuple = localtime()
    current_date = "{:04d}-{:02d}-{:02d}".format(
        current_time_tuple[0],  # 年
        current_time_tuple[1],  # 月
        current_time_tuple[2]   # 日
    )

    current_time = "{:02d}:{:02d}:{:02d}".format(
        current_time_tuple[3],  # 时
        current_time_tuple[4],  # 分
        current_time_tuple[5]   # 秒
    )
    
    # 清除显示内容
    oled.fill(0)
    
    # 显示温湿度和当前时间
    oled.text('Temperature: ' + str(temp) + 'C', 0, 0)
    oled.text('Humidity: ' + str(hum) + '%', 0, 10)
    oled.text('Date:', 0, 20)
    oled.text(current_date, 0, 30)
    oled.text('Time:', 0, 40)
    oled.text(current_time, 0, 50)
    # 显示更新内容
    oled.show()
    
    # 打印到控制台
    print('Temperature: ' + str(temp) + 'C')
    print('Humidity: ' + str(hum) + '%')
    print('Date: ' + current_date)
    print('Time: ' + current_time)
    
    # 将数据写入文件
    with open(filename, 'a') as file:
        file.write(f"{current_date} {current_time}, Temp: {temp}C, Humidity: {hum}%\n")
    
    # 根据温度控制PWM
    if int(temp) >= 25:
        S1.duty(65)
    else:
        S1.duty(77)
    
    # 等待1秒后再次读取并更新显示
    sleep(1)