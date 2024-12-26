""" Hypothesis Testing หน้า 59
พยายามกระตุ้นให้ผู้คนหยุดขับรถไปที่มหาวิทยาลัย
มหาวิทยาลัยอ้างว่าโดยเฉลี่ยแล้วใช้เวลาอย่างน้อย 30 นาที
ในการหาที่จอดรถในมหาวิทยาลัย ฉันไม่คิดว่าจะใช้เวลานานในการหาที่นั่ง 
ในความเป็นจริงฉันมีตัวอย่างห้าครั้งสุดท้ายที่ฉันขับรถไปที่มหาวิทยาลัย 
และฉันคํานวณ x = 20 สมมติว่าเวลาที่ใช้ในการหาจุดจอดรถเป็นเรื่องปกติ 
และ σ = 6 นาที จากนั้นทําการทดสอบสมมติฐานด้วยระดับ α= 0.10 
เพื่อดูว่าคํากล่าวอ้างของฉันถูกต้องหรือไม่
"""
import scipy.stats as stats
import numpy as np

# ข้อมูลจากโจทย์
mu_0 = 30  # ค่าที่มหาวิทยาลัยอ้างว่าใช้เวลาเฉลี่ยหาที่จอดรถ (นาที)
x_bar = 20  # ค่าเฉลี่ยของตัวอย่างที่เก็บมา (นาที)
sigma = 6  # ส่วนเบี่ยงเบนมาตรฐาน (นาที)
n = 5  # ขนาดของตัวอย่าง
alpha = 0.10  # ระดับนัยสำคัญ

# ขั้นตอนการทดสอบสมมติฐาน
# 1. กำหนดสมมติฐาน
# H0: mu >= 30 (ใช้เวลาเฉลี่ยหาที่จอดรถมากกว่าหรือเท่ากับ 30 นาที)
# H1: mu < 30 (ใช้เวลาเฉลี่ยหาที่จอดรถน้อยกว่า 30 นาที)

# 2. คำนวณค่า z-test
z = (x_bar - mu_0) / (sigma / np.sqrt(n))

# 3. คำนวณค่า p-value
p_value = stats.norm.cdf(z)  # ใช้ cdf เพราะเป็นการทดสอบด้านเดียว

# 4. เปรียบเทียบค่า p-value กับระดับนัยสำคัญ
if p_value < alpha:
    result = "ปฏิเสธสมมติฐาน H0: ค่าเฉลี่ยเวลาที่ใช้ในการหาที่จอดรถน้อยกว่า 30 นาที"
else:
    result = "ไม่สามารถปฏิเสธสมมติฐาน H0 ได้"

# แสดงผลลัพธ์
print(f"ค่า z-test: {z:.2f}")
print(f"ค่า p-value: {p_value:.4f}")
print(f"ผลการทดสอบ: {result}")