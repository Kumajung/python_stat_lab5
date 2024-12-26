import numpy as np
import scipy.stats as stats

# ข้อมูลตัวอย่าง
sample_scores = [72, 74, 75, 78, 76, 73, 74, 77, 79, 75]  # คะแนนนักเรียน
population_mean = 70  # ค่าเฉลี่ยประชากรที่กำหนดไว้
alpha = 0.05  # ระดับนัยสำคัญ

# คำนวณค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของกลุ่มตัวอย่าง
sample_mean = np.mean(sample_scores)
sample_std = np.std(sample_scores, ddof=1)  # ddof=1 สำหรับ Sample Standard Deviation
n = len(sample_scores)

# คำนวณ t-statistic
t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(n))

# คำนวณค่า p-value
p_value = 2 * stats.t.sf(np.abs(t_statistic), df=n-1)

# แสดงผลลัพธ์
print(f"ค่าเฉลี่ยกลุ่มตัวอย่าง: {sample_mean:.2f}")
print(f"t-statistic: {t_statistic:.2f}")
print(f"p-value: {p_value:.4f}")

# สรุปผลการทดสอบสมมติฐาน
if p_value < alpha:
    print("ปฏิเสธสมมติฐาน H0: คะแนนเฉลี่ยแตกต่างจาก 70")
else:
    print("ยอมรับสมมติฐาน H0: ไม่มีหลักฐานว่าคะแนนเฉลี่ยแตกต่างจาก 70")
