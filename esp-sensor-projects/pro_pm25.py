import ssd1306  
from machine import Pin, ADC, PWM, SoftI2C  
import time  
import utime  
  
# 设置引脚  
led_control = Pin(16, Pin.OUT)  # 黄色线（LED）连接到GPIO5  
adc_pin = ADC(Pin(00))  # 蓝色线（Vo）连接到GPIO36  
pwm = PWM(led_control)  # 用于控制LED的PWM  
pwm.freq(1000)  
  
# 初始化OLED  
i2c = SoftI2C(scl=Pin(23), sda=Pin(19))  
oled_width = 128  
oled_height = 64  
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)  
  
def read_pm25():  
    # 读取多次传感器值并计算平均值  
    samples = 10  # 样本数  
    total = 0  
    for i in range(samples):  
        total += adc_pin.read()  
        time.sleep(0.01)  # 稍微延迟，减小采样时间间隔  
    avg_value = total // samples  
    return avg_value  
  
def convert_to_ugm3(adc_value):  
    # 根据传感器的特性，找到正确的转换因子  
    conversion_factor = 100  # 假设一个转换因子（具体数值需要根据传感器规格确定）  
    voltage = (adc_value / 4095.0) * 3.3  # 将ADC值转换为电压  
    pm25_value = voltage * conversion_factor  # 将电压转换为PM2.5浓度  
    pm25_value -= 100  
    return pm25_value  
  
def get_air_quality_category(pm25_value):  
    # 根据PM2.5浓度判断空气质量类别  
    if pm25_value <= 35:  
        return "Good"  
    elif pm25_value <= 75:  
        return "Moderate"  
    elif pm25_value <= 115:  
        return "Unhealthy for Sensitive Groups"  
    elif pm25_value <= 150:  
        return "Unhealthy"  
    elif pm25_value <= 250:  
        return "Very Unhealthy"  
    else:  
        return "Hazardous"  
  
def write_to_file(data, category):  
    # 将数据写入文件  
    current_time = utime.localtime()  
    timestamp = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])  
    with open('/PM25_data.txt', 'a') as file:  
        file.write(f"{timestamp}, PM2.5: {data} μg/m³, Air Quality: {category}\n")  
  
def wrap_text(text, max_width, font_size):  
    """将文本拆分成适合显示屏宽度的多行"""  
    words = text.split(' ')  
    lines = []  
    current_line = ''  
    for word in words:  
        # 计算当前行宽度  
        line_width = len(current_line + word) * font_size  
        if line_width > max_width:  
            lines.append(current_line)  
            current_line = word  
        else:  
            current_line += ' ' + word  
    if current_line:  
        lines.append(current_line)  
    return lines  
  
while True:  
    pm25_value_adc = read_pm25()  
    pm25_value = convert_to_ugm3(pm25_value_adc)  
    air_quality_category = get_air_quality_category(pm25_value)  
      
    # 获取当前时间并格式化  
    current_time = utime.localtime()  
    year = "{}-{:02d}-{:02d}".format(current_time[0], current_time[1], current_time[2])  
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])  
      
    # 清除显示内容  
    oled.fill(0)  
      
    # 显示PM2.5浓度和空气质量  
    pm25_text = 'PM2.5:{:.1f} ug/m³'.format(pm25_value)  
    quality_text = 'Qual:' + air_quality_category  
    date_text = 'Date:' + year  
    time_text = 'Time:' + time_str  
  
    # 使用 wrap_text 函数处理文本换行  
    lines_pm25 = wrap_text(pm25_text, oled_width, 6)  # 字体宽度假设为6像素  
    lines_quality = wrap_text(quality_text, oled_width, 6)  
    lines_date = wrap_text(date_text, oled_width, 6)  
    lines_time = wrap_text(time_text, oled_width, 6)  
  
    # 将文本逐行显示在屏幕上  
    y = 0  
    for line in lines_pm25:  
        oled.text(line, 0, y)  
        y += 10  
    for line in lines_quality:  
        oled.text(line, 0, y)  
        y += 10  
    for line in lines_date:  
        oled.text(line, 0, y)  
        y += 10  
    for line in lines_time:  
        oled.text(line, 0, y)  
        y += 10  
      
    # 显示更新内容  
    oled.show()  
      
    # 打印带时间戳和空气质量类别的读数  
    print(f"{year}, {time_str}, PM2.5浓度: {pm25_value} μg/m³, 空气质量: {air_quality_category}")  
      
    # 将PM2.5数据和空气质量类别写入文件  
    write_to_file(pm25_value, air_quality_category)  
      
    # 根据传感器值调节LED亮度  
    pwm.duty(int(pm25_value // 4))  # 1024级PWM控制  
      
    time.sleep(0.5)  # 更短的读取间隔以观察变化
