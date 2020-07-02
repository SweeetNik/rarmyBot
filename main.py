# -*- coding: utf-8 -*-
import vk
import time

time.sleep(7200)

my_app_id = 7496109
user_login = 'соси член'
user_password = 'я сказал член соси'


def subtract():
    global a
    a -= 1
    api.wall.post(owner_id='-195777168', message="Димас еще в армии\nДимасу осталось служить " + str(a) + " дней",
                  attachments='photo201342171_456272777', v=5.107)
    print(a)
    time.sleep(86400)
    if a == 1:
        api.wall.post(owner_id='-195777168', message="Димас ДЕМБЕЛЬНУЛСЯ", attachments='photo201342171_456272777',
                      v=5.107)


session = vk.AuthSession(scope='wall', app_id=my_app_id, user_login=user_login, user_password=user_password)
vk.api.access_token = "e47a840ce7af354b18208aac442f84ba6512644590bc55cb5a643e97282b78d72a6c4479271b6f9a7ca3d"
api = vk.API(session)
a = 8
while a > 1:
    try:
        subtract()
    except Exception as E:
        time.sleep(5)
        subtract()
