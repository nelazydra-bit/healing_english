import subprocess
from flask import Flask, render_template_string, jsonify

# Khởi tạo một server Flask
app = Flask(__name__)

# Phần này chứa giao diện HTML sảnh game của bạn
HTML_LOBBY = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Sảnh Game Đơn Giản</title>
    <style>
        body { 
            background: #1e1e24; 
            color: white; 
            text-align: center; 
            font-family: 'Arial', sans-serif; 
            padding-top: 150px; 
        }
        h1 { color: #ff4757; font-size: 40px; }
        .play-btn { 
            background: #2ed573; 
            color: white; 
            padding: 15px 40px; 
            font-size: 22px; 
            border: none; 
            cursor: pointer; 
            border-radius: 8px; 
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(46, 213, 115, 0.4);
            transition: 0.2s;
        }
        .play-btn:hover { background: #26af5f; transform: scale(1.05); }
    </style>
</head>
<body>
    <h1>🎮 GAME LOBBY 🎮</h1>
    <p>Bấm nút bên dưới để khởi động game Pygame trên máy tính</p>
    <br><br>
    <button class="play-btn" onclick="startPygame()">BẮT ĐẦU CHƠI</button>

    <script>
        function startPygame() {
            // Khi bấm nút, trình duyệt sẽ gửi 1 lệnh ngầm đến server Python
            fetch('/run-game')
                .then(response => response.json())
                .then(data => {
                    console.log(data.status);
                });
        }
    </script>
</body>
</html>
"""

# Định nghĩa trang chủ khi bạn truy cập vào web
@app.route('/')
def home():
    return render_template_string(HTML_LOBBY)

# Định nghĩa đường dẫn xử lý việc mở game Pygame
@app.route('/run-game')
def run_game():
    try:
        # Lệnh này tương đương với việc bạn gõ "python main.py" trong CMD
        # LƯU Ý: Đổi 'main.py' thành tên file game Pygame của bạn nhé!
        subprocess.Popen(['python', 'main.py']) 
        return jsonify({"status": "Đang chạy game..."})
    except Exception as e:
        return jsonify({"status": f"Lỗi không mở được game: {str(e)}"})

if __name__ == '__main__':
    # Chạy server ở cổng (port) 5000
    app.run(port=5000, debug=False, use_reloader=False)
