# Conformer

- โมเดล Transformer และ Convolution Neural Network (CNN) แสดงให้เห็นถึงประสิทธิภาพที่ดีในการรู้จำเสียงพูดอัตโนมัติ (ASR) เมื่อเทียบกับ Recurrent Neural Network (RNN) แบบเดิม
- Transformer เก่งในการจับความสัมพันธ์เชิงเนื้อหาโดยรวม ในขณะที่ CNN สามารถใช้ประโยชน์จากข้อมูลเฉพาะจุดได้อย่างมีประสิทธิภาพ
- งานวิจัยนี้ประยุกต์ข้อดีของทั้ง CNN และ Transformer เพื่อจำลองการความสัมพันธ์ทั้งระดับท้องถิ่นและระดับโลกของลำดับเสียงอย่างมีประสิทธิภาพ
- ด้วยเหตุนี้จึงได้มีการนำเสนอ Conformer ซึ่งเป็น convolution-augmented transformer สำหรับการรู้จำเสียงพูด
- Conformer มีประสิทธิภาพเหนือกว่าโมเดล Transformer และ CNN รุ่นก่อนหน้าอย่างมาก โดยได้ผลลัพธ์ที่ล้ำสมัย
- จากชุดข้อมูลมาตรฐาน LibriSpeech โมเดลนี้ให้ค่าความคลาดเคลื่อนของคำ (WER) เพียง 2.1%/4.3% โดยไม่ใช้โมเดลภาษา และ 1.9%/3.9% เมื่อใช้โมเดลภาษาภายนอกในการทดสอบ
- นอกจากนี้ Conformer ยังมีประสิทธิภาพที่ดีแม้จะเป็นโมเดลขนาดเล็กที่มีพารามิเตอร์เพียง 10 ล้านตัว โดยให้ค่า WER 2.7%/6.3%