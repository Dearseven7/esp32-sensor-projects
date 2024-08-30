import ssd1306
from machine import Pin, ADC, PWM,SoftI2C
from time import sleep
import utime
from num import *
from utime import localtime


# 初始化光敏传感器、触摸传感器和LED
light_sensor = ADC(Pin(35))  # 假设光敏传感器连接到GPIO 34
light_sensor.atten(ADC.ATTN_11DB)  # 设置衰减为11dB，使得输入电压范围为0到3.6V
light_sensor.width(ADC.WIDTH_10BIT)  # 设置位宽为10位，分辨率为1024

touch_sensor = Pin(34, Pin.IN)  # 假设触摸传感器连接到GPIO 18
led = PWM(Pin(32), freq=1000)   # 假设LED连接到GPIO 32

# 用于跟踪LED的开关状态
led_state = False

# 使用I2C协议，初始化OLED
i2c = SoftI2C(scl=Pin(23), sda=Pin(19))

# 定义OLED显示屏像素
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# 初始状态下确保LED关闭
led.duty(0)

# 定义指数平滑的alpha值（控制平滑度，范围在0到1之间）
alpha = 0.8
smoothed_value = None

def handle_interrupt(pin):
    global led_state
    # 切换LED状态
    led_state = not led_state
    if not led_state:
        print("Turn off")
        led.duty(0)  # 关闭LED

# 设置中断触发器，触发方式为上升沿（触摸）
touch_sensor.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

def write_to_file(data):
    # 将数据写入文件
    with open('/light_data.txt', 'a') as file:
        file.write(f"{data}\n")

while True:
    if led_state:
        # 多次读取光敏传感器的值以获得平均值
        readings = []
        for _ in range(10):
            readings.append(light_sensor.read())
            sleep(0.05)  # 稍微延迟减小噪声影响
        avg_value = sum(readings) // len(readings)
        
        # 应用指数平滑
        if smoothed_value is None:
            smoothed_value = avg_value
        else:
            smoothed_value = alpha * avg_value + (1 - alpha) * smoothed_value
        
        # 反转光敏传感器的值，使光照越强LED越暗
        duty = 1023 - int((smoothed_value / 1023) * 1023)
        
        # 确保duty在0到1023范围内
        duty = max(0, min(1023, duty))
        
        led.duty(duty)
        
        # 获取当前时间并格式化
        current_time = utime.localtime()
        timestamp = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])
        
        
#         根据光照强度输出对应的光照等级
        rate = int(smoothed_value)

        if rate >= 0 and rate <=100:
            display_0()
            light_num = 0
        if rate > 100 and rate <=200:
            display_1()
            light_num = 1
        if rate > 200 and rate <=300:
            display_2()
            light_num = 2
        if rate > 300 and rate <=400:
            display_3()
            light_num = 3
        if rate > 400 and rate <=500:
            display_4()
            light_num = 4
        if rate > 500 and rate <=600:
            display_5()
            light_num = 5
        if rate > 600 and rate <=700:
            display_6()
            light_num = 6
        if rate > 700 and rate <=800:
            display_7()
            light_num = 7
        if rate > 800 and rate <=900:
            display_8()
            light_num = 8
        if rate > 900:
            display_9()
            light_num = 9
        # 打印和写入带时间戳的读数
        output = f"{timestamp}, 光照强度: {int(smoothed_value)}, LED亮度: {duty}, 光照强度等级: {light_num}"
        print(output)
                
                     
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
        oled.text('LightIntens:' + str(smoothed_value) + 'C', 0, 0)
        oled.text('Led: ' + str(duty) , 0, 10)
        oled.text('Light Rate:'+ str(light_num), 0, 20)
        oled.text(current_date, 0, 30)
        oled.text('Time:', 0, 40)
        oled.text(current_time, 0, 50)
        # 显示更新内容
        oled.show()
        write_to_file(output)
    
    # 每0.5秒读取一次
    sleep(1)


