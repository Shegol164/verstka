from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/<path:subpath>', methods=['GET'])
def get_contacts(subpath=None):
    # Читаем содержимое HTML-файла
    with open('сontacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()


    # Возвращаем HTML с правильным Content-Type
    return html_content, 200, {'Content-Type': 'text/html'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)