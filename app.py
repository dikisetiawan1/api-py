from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Fungsi untuk baca file Excel
def read_excel():
    df = pd.read_excel('data.xlsx')  # Bisa tambahkan sheet_name jika perlu
    return df.to_dict(orient='records')  # Mengembalikan data sebagai list of dicts
@app.route('/')
def home():
    return 'API is running!'


@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = read_excel()
        return jsonify({'status': 'success', 'data': data})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
