###### ห้ามสอน
""" Hypothesis Testing หน้า 61
สํานักงานหนังสือเดินทางอ้างว่าคําขอหนังสือเดินทางได้รับการดําเนินการภายใน 30 วัน
นับจากวันที่ส่งแบบฟอร์มใบสมัครและเอกสารที่จําเป็นทั้งหมด 
ตารางด้านล่างแสดงเวลาดําเนินการของผู้ยื่นขอหนังสือเดินทาง 40 คน 
ค่าเบี่ยงเบนมาตรฐานของประชากรของเวลาดําเนินการคือ 12.5 วัน 
ทําการทดสอบสมมติฐานที่ระดับนัยสําคัญ a = 0.05 
เพื่อตรวจสอบการอ้างสิทธิ์ของสํานักงานหนังสือเดินทาง
"""
import numpy as np
from scipy import stats

# ข้อมูลการประมวลผลคำขอหนังสือเดินทาง
data = [16, 16, 30, 37, 25, 22, 19, 35, 27, 32, 
        34, 28, 24, 35, 24, 21, 32, 29, 24, 35,
        28, 29, 18, 31, 28, 33, 32, 24, 25, 22,
        21, 27, 41, 23, 23, 16, 24, 38, 26, 28]
# ค่าเฉลี่ยของตัวอย่าง
sample_mean = np.mean(data)

# ขนาดตัวอย่าง
n = len(data)

# ค่าเบี่ยงเบนมาตรฐานของประชากร
population_std = 12.5

# ค่าเฉลี่ยที่คาดหวัง (สมมติฐานหลัก)
hypothesized_mean = 30

# คำนวณค่า Z
z_score = (sample_mean - hypothesized_mean) / (population_std / np.sqrt(n))

# ค่า p-value จาก Z-test
p_value = stats.norm.sf(abs(z_score)) * 2  # คูณด้วย 2 เพื่อให้เป็น two-tailed test

# ระดับนัยสำคัญ
alpha = 0.05

# ตรวจสอบสมมติฐาน
if p_value < alpha:
    print(f"ค่า p-value คือ {p_value:.4f} ซึ่งน้อยกว่า {alpha} ดังนั้นเราปฏิเสธสมมติฐานหลัก")
else:
    print(f"ค่า p-value คือ {p_value:.4f} ซึ่งมากกว่า {alpha} ดังนั้นเราไม่สามารถปฏิเสธสมมติฐานหลัก")