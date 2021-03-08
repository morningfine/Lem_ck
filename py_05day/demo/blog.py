from dev_05day.demo.grass import Grass

app = Grass()


@app.router('/home')
def home():
    return "home"


@app.router('/index')
def index():
    return "index"


def run():
    while True:
        url = input("请输入url：")
        try:
            print(app.url_map[url]())
        except Exception as e:
            print(404)


if __name__ == '__main__':
    run()
