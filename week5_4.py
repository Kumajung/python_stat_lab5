"""
โจทย์: การวิเคราะห์ประสิทธิภาพการผลิตของโรงงานผลิตสินค้า
โรงงานผลิตสินค้าแห่งหนึ่งอ้างว่าสามารถผลิตสินค้าได้เฉลี่ย 500 ชิ้นต่อวัน 
โดยมีค่าเบี่ยงเบนมาตรฐาน 50 ชิ้น 
คุณได้รับมอบหมายให้ทดสอบสมมติฐานเกี่ยวกับประสิทธิภาพการผลิตของโรงงาน 
โดยใช้ข้อมูลการผลิต 100 วันจากไฟล์ CSV "production_data.csv"
"""
import numpy as np
import pandas as pd
from scipy import stats

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv('production_data.csv')['production']

# คำนวณค่าเฉลี่ยของตัวอย่าง
sample_mean = np.mean(data)

# คำนวณขนาดตัวอย่าง
n = len(data)

# กำหนดค่าเบี่ยงเบนมาตรฐานของประชากร
population_std = 50

# กำหนดค่าเฉลี่ยที่คาดหวัง (สมมติฐานหลัก)
hypothesized_mean = 500

# คำนวณค่า Z
z_score = (sample_mean - hypothesized_mean) / (population_std / np.sqrt(n))

# คำนวณค่า p-value จาก Z-test
p_value = stats.norm.sf(abs(z_score)) * 2

# ระดับนัยสำคัญ
alpha = 0.05

# ตรวจสอบสมมติฐาน
if p_value < alpha:
    print(f"ค่า p-value คือ {p_value:.4f} ซึ่งน้อยกว่า {alpha} ดังนั้นเราปฏิเสธสมมติฐานหลัก")
else:
    print(f"ค่า p-value คือ {p_value:.4f} ซึ่งมากกว่า {alpha} ดังนั้นเราไม่สามารถปฏิเสธสมมติฐานหลัก")