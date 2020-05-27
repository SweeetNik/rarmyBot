# -*- coding: utf-8 -*-
import vk
import time
my_app_id = 7486921
user_login = '+79883214673'
user_password = '1029384756Nikersss'

session = vk.AuthSession(scope='wall', app_id=my_app_id, user_login=user_login, user_password=user_password)
vk.api.access_token="e47a840ce7af354b18208aac442f84ba6512644590bc55cb5a643e97282b78d72a6c4479271b6f9a7ca3d"
api = vk.API(session)
a = 44
while a > 1:
    api.wall.post(owner_id='-195777168', message="Димасу осталось служить " + str(a) + " дня", attachments='photo201342171_456272777', v=5.50)
    a -= 1
    time.sleep(86400)
