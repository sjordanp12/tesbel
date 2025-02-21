from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Zona waktu Jakarta
timezone = pytz.timezone('Asia/Jakarta')

# Simpan jadwal bel untuk setiap hari (Senin sampai Sabtu)
weekly_schedule = {
    "Senin": [
        {"time": "07:15:00", "label": "Upacara Bendera", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat 1", "sound": "Istirahat_Pertama.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Istirahat 2", "sound": "Istirahat_Kedua.wav"},
        {"time": "11:45:00", "label": "Pelajaran 7", "sound": "bel7.wav"},
        {"time": "12:15:00", "label": "Pelajaran 8", "sound": "bel8.wav"},
        {"time": "12:45:00", "label": "Pelajaran 9", "sound": "bel9.wav"},
        {"time": "13:15:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya...
    ],
    "Selasa": [
      {"time": "07:15:00", "label": "Upacara", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat 1", "sound": "Istirahat_Pertama.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Istirahat 2", "sound": "Istirahat_Kedua.wav"},
        {"time": "11:45:00", "label": "Pelajaran 7", "sound": "bel7.wav"},
        {"time": "12:15:00", "label": "Pelajaran 8", "sound": "bel8.wav"},
        {"time": "12:45:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya..9
    ],
    # Tambahkan untuk hari Rabu sampai Sabtu
       "Rabu": [
         {"time": "07:15:00", "label": "Upacara", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat 1", "sound": "Istirahat_Pertama.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Istirahat 2", "sound": "Istirahat_Kedua.wav"},
        {"time": "11:45:00", "label": "Pelajaran 7", "sound": "bel7.wav"},
        {"time": "12:15:00", "label": "Pelajaran 8", "sound": "bel8.wav"},
        {"time": "12:45:00", "label": "Pelajaran 9", "sound": "bel9.wav"},
        {"time": "13:15:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya...
    ],
       "Kamis": [
       {"time": "07:15:00", "label": "Apel Pagi", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat 1", "sound": "Istirahat_Pertama.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Istirahat 2", "sound": "Istirahat_Kedua.wav"},
        {"time": "11:45:00", "label": "Pelajaran 7", "sound": "bel7.wav"},
        {"time": "12:15:00", "label": "Pelajaran 8", "sound": "bel8.wav"},
        {"time": "12:45:00", "label": "Pelajaran 9", "sound": "bel9.wav"},
        {"time": "13:15:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya...
    ],
       "Jumat": [
        {"time": "07:15:00", "label": "Apel Pagi", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat", "sound": "Istirahat.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya...
    ],
       "Sabtu": [
        {"time": "07:15:00", "label": "Senam", "sound": "bel1.wav"},
        {"time": "07:30:00", "label": "Pelajaran 1", "sound": "bel1.wav"},
        {"time": "08:15:00", "label": "Pelajaran 2", "sound": "bel2.wav"},
        {"time": "08:55:00", "label": "Pelajaran 3", "sound": "bel3.wav"},
        {"time": "09:30:00", "label": "Istirahat 1", "sound": "Istirahat_Pertama.wav"},
        {"time": "10:00:00", "label": "Pelajaran 4", "sound": "bel4.wav"},
        {"time": "10:30:00", "label": "Pelajaran 5", "sound": "bel5.wav"},
        {"time": "11:00:00", "label": "Pelajaran 6", "sound": "bel6.wav"},
        {"time": "11:30:00", "label": "Istirahat 2", "sound": "Istirahat_Kedua.wav"},
        {"time": "11:45:00", "label": "Pelajaran 7", "sound": "bel7.wav"},
        {"time": "12:15:00", "label": "Pelajaran 8", "sound": "bel8.wav"},
        {"time": "12:45:00", "label": "Pelajaran 9", "sound": "bel9.wav"},
        {"time": "13:15:00", "label": "Pulang", "sound": "belpulang.mp3"},
        # Tambahkan jadwal lainnya...
    ],
}

# Routing untuk menampilkan jadwal bel
@app.route('/')
def index():
    return render_template('index.html')

# API untuk mengirim jadwal bel berdasarkan hari
@app.route('/get_schedule/<day>')
def get_schedule(day):
    return jsonify(weekly_schedule.get(day, []))

# API untuk mendapatkan waktu Jakarta sekarang
@app.route('/get_time')
def get_time():
    current_time = datetime.now(timezone).strftime('%H:%M:%S')
    return jsonify({"time": current_time})

if __name__ == '__main__':
    app.run(debug=True)
