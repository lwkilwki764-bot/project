from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/status')
def api_status():
    return jsonify({
        "status": "online",
        "app": "تطبيق مؤسسة الباقيات الصالحات",
        "services_count": 7,
        "engine": "C++ Native Core & SQLite DB"
    })

if __name__ == '__main__':
    print("=========================================================")
    print("   تم تشغيل سيرفر تطبيق مؤسسة الباقيات الصالحات بنجاح!  ")
    print("   افتح هذا الرابط في المتصفح: http://127.0.0.1:5000      ")
    print("=========================================================")
    app.run(host='0.0.0.0', port=5000, debug=True)
