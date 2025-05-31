from DrissionPage import ChromiumPage

# 初始化 ChromiumPage
driver = ChromiumPage()

# 打开目标 URL
urls = 'https://www.baidu.com/'
driver.get(urls)

# 获取元素列表
elements = driver.eles('xpath=//span[@class="title-content-title"]')

# 检查元素列表是否为空
if elements:
    # 提取第一个元素的文本
    text = elements[0].text
    print(text)
else:
    print("未找到匹配的元素")