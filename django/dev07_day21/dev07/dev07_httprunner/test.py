from httprunner.api import HttpRunner


httprun = HttpRunner(save_tests=True)
httprun.run(r'C:\Users\KeYou\PycharmProjects\dev07\dev07_httprunner\api\login_api_bk.yml')
print(httprun._summary)
