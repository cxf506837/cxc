from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from DrissionPage import Chromium
import logging
import requests
from openai import OpenAI
import time
from time import sleep

def scroll_down(tab, max_scrolls=50, step=1200, delay=1):
    """
    缓慢向下滚动，到底后自动停止
    :param tab: DrissionPage 的标签页对象
    :param max_scrolls: 最多尝试滚动多少次
    :param step: 每次滚动多少像素
    :param delay: 滚动后等待时间（秒）
    """
    for i in range(max_scrolls):
        current_position = tab.run_js('return window.scrollY')
        tab.run_js(f'window.scrollBy(0, {step});')  # 向下滚动 step 像素
        print(f"正在滚动第 {i + 1} 次... 当前位置: {current_position}")
        sleep(delay)

        new_position = tab.run_js('return window.scrollY')
        if new_position == current_position:
            print("已滚动到底部，停止滚动。")
            break
# 配置日志记录
logger = logging.getLogger(__name__)

# 假设这是你的用户字典
users = {
    'cxf': 'cxf'
}

class pachongView(View):
    def get(self, request):
        return render(request, 'pachong.html')
    
    def post(self, request):
        user_input = request.POST.get('user_input')
        action = request.POST.get('action')

        if action == '毕业' or user_input == '毕业':
            return redirect('biye')
        elif action == '爬虫' or user_input == '爬虫':
            return redirect('chong')
        elif action == '查询' or user_input == '查询':
            return redirect('chaxun')
        elif user_input == '文本':
            text = "这是文本内容"
            return HttpResponse(text)
        else:
            return HttpResponse('输入错误')


class UserView(View):
    def get(self, request):
        return render(request, 'index1.html')
    
    def post(self, request):
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username in users and users[username] == password:
            return redirect('cbv:pachong')
        else:
            logger.warning(f"用户名或密码错误 - 用户名: {username}, 密码: {password}")
            return HttpResponse('账号或密码错误', status=401)


class BiyeView(View):
    def get(self, request):
        return render(request, 'biye.html')


class ChaxunView(View):
    def get(self, request):
        return render(request, 'chaxun.html')


class ChongView(View):
    brands = ['德芙', '费列罗']
    def get(self, request):
        return render(request, 'chong.html')


class BijiaView(View):
    def get(self, request):
        return render(request, 'bijia.html')

    def post(self, request):
        user_input = request.POST.get('user_input')
        jd_results = self.search_jingdong(user_input)
        tb_results = self.search_taobao(user_input)  # 这里调用类内方法没问题

        # 构造 AI 提示词（仅含 name + price）
        ai_jd_products = [f"{item['name']} ¥{item['price']}" for item in jd_results]
        ai_tb_products = [f"{item['name']} ¥{item['price']}" for item in tb_results]

        prompt = f"""
请分析以下两个平台的商品价格和品牌进行对比，得出哪个平台性价比更高的商品更多。
搜索关键词：{user_input}

京东商品：
{'、'.join(ai_jd_products)}

淘宝商品：
{'、'.join(ai_tb_products)}
"""

        client = OpenAI(
            api_key="sk-446236bd68f948b6bff622cf2b7f6493",
            base_url="https://api.deepseek.com"
        )

        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个商品比价助手，请根据两个平台的商品价格和品牌进行对比，得出哪个平台性价比更高的商品更多。简短说明"},
                    {"role": "user", "content": prompt},
                ],
                stream=False
            )
            answer = response.choices[0].message.content.strip()
        except Exception as e:
            logger.error("AI 请求失败:", str(e))
            answer = "抱歉，暂时无法分析商品，请稍后再试。"

        context = {
            'jd_results': jd_results,
            'tb_results': tb_results,
            'ai_response': answer,
        }

        return render(request, 'bijia.html', context)

    def search_jingdong(self, user_input):
        results = []
        url = f'https://re.jd.com/search?keyword={user_input}'
        bs = Chromium()
        tab = bs.latest_tab
        tab.get(url)
        time.sleep(3)
        commodity = tab(".clearfix").children()
        for i in commodity:
            name = i(".commodity_tit").text
            price = i(".commodity_info").text
            urls = i('tag:a').attr('href')
            pic = i('.img_k')
            img_src = pic.attr('src') if pic else None
            img_url = f"{img_src}" if img_src else None
            results.append({'name': name, 'price': price, 'urls': urls, 'img_url': img_url})
        return results

    def search_taobao(self, user_input):  # 👈 现在这个方法属于 BijiaView 类
        results = []
        url = f'https://uland.taobao.com/sem/tbsearch?bc_fl_src=tbsite_T9W2LtnM&channelSrp=bingSomama&clk1=ae056e0469d46c828d91b597923d08de&commend=all&ie=utf8&initiative_id=tbindexz_20170306&localImgKey=&msclkid=349da7ff3f0f1404b034cff97e56b8ba&page=1&q={user_input}&refpid=mm_2898300158_3078300397_115665800437&search_type=item&sourceId=tb.index&spm=tbpc.pc_sem_alimama%2Fa.201856.d13&ssid=s5-e&tab=all'
        
        bs = Chromium()
        tab = bs.latest_tab
        tab.get(url)
        scroll_down(tab, max_scrolls=50, step=700, delay=1)

        try:
            # 使用 wait 方法等待元素加载
            time.sleep(5)
            all_items = tab('.Content--contentInner--QVTcU0M').children()

            for i in all_items:
                try:
                    name = i('.Title--title--wJY8TeA ').text
                    price1 = i('.Price--priceInt--BXYeCOI').text
                    price2 = i('.Price--priceFloat--rI_BYho').text
                    full_price = f"{price1}{price2}"
                    urls = i.attr('href')
                    
                    pic = i('.MainPic--mainPic--aVle5J9')
                    img_src = pic.attr('src') if pic else None
                    img_url = f"{img_src}" if img_src else None

                    results.append({
                        'name': name,
                        'price': full_price,
                        'urls': urls,
                        'img_url': img_url
                    })
                except Exception as e:
                    print(f"Error processing item: {e}")
        except Exception as e:
            print(f"Error in search_taobao: {e}")

        return results