from httprunner.api import HttpRunner


httprun = HttpRunner()
httprun.run(r'C:\Users\KeYou\PycharmProjects\dev07\dev07_httprunner\api\login_api.yml')
print(httprun._summary)
