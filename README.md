
# ขั้นตอนการใช้งาน
## 1.สำหรับแปลงข้อความจากวีดีโออย่างเดียว
โดยไฟล์จะอยู่ใน Path:
```
sub-single.py
```


## 2.สำหรับแปลงข้อความจากวีดีโอ ในรูปแบบของ subtitle

โดยไฟล์จะอยู่ใน Path:
```
sub-multiple.py
```

เอาไปแล้วตั้งค่า video_path

```
video_path = "{You-Video-Path}"
```

## 3.สำหรับไฟล์วีดีโอที่มีความยาวมากๆ

### 3.1 อัพโหลดวีดีโอไปเก็บบน Google Cloud Storage

### 3.2 ตั้งค่า Google Cloud service-key

ในไฟล์:
```
google-text-to-speech-v2-with-long-audio.py
```

ตั้งค่า
```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{..path/key.json}"
```

### 3.3 ตั้งค่า gcs_uris

ตั้งค่า
```
gs_out = 'gs://...'
gs_in_list = [
    'gs://file1.wav',
    'gs://file2.wav',
    # '...',
]
gs_project_id = '{your-project-id}'
```

โดยไฟล์เสียงที่ได้จะอยู่ใน gs_out

สามารถดูตัวอย่างได้ใน
```
out-txt-long-audio/out-tts-v1_yt-THE--STANDARD_transcript_65e8854d-0000-278e-b1f0-883d24f27174.json
```

---

# SOME IDEAS

## Search ข้อความจากวิดีโอ ลดเวลาการหา

## ถอดเสียงงานสัมมนา

### fretures
- แปลข้อความ
- Smart Search (หลายๆ เวที)


## รายงานผลสลากกินแบ่ง

### fretures
- อัพเดทเข้าฐานข้อมูลแบบ Real Time
