from nonebot import on_command,CommandSession
import nonebot
import requests,json
from datetime import datetime
import pytz

@on_command('say', aliases=('每日一句'))
async def everydaysay(session:CommandSession):
    says=session.state.get('says')
    url = 'http://open.iciba.com/dsapi/'
    res =requests.get(url)
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    data= res.json()
    content_e = data['content']
    content_c =data['note']
    img_url =data['fenxiang_img']
    # print(img_url)
    # await session.send_private_msg(user_id=1714004230, message=f'现在{now.hour}:{now.minute}啦！')
    await session.send(content_e)
    await session.send(content_c)
    await session.send(f'[CQ:image,file={img_url}]')
