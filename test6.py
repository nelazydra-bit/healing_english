import subprocess
from flask import Flask, jsonify
from flask_cors import CORS  # Giúp HTML có thể gọi sang Python mà không bị chặn safety

app = Flask(__name__)
CORS(app)  # Kích hoạt CORS cho phép mọi nguồn truy cập

@app.route('/run-game', methods=['GET'])
def run_game():
    try:
        # THAY THẾ 'game.py' THÀNH TÊN FILE GAME CỦA BẠN (Ví dụ: 'main.py')
        # Lệnh này tương đương với việc bạn gõ "python game.py" trong CMD
        subprocess.Popen(['python', 'main.py']) 
        return jsonify({"status": "success", "message": "Đang khởi động game Pygame!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Chạy server ở cổng 5000 cục bộ
    app.run(port=5000)
