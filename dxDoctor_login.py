import time
from selenium import webdriver
#from selenium.webdriver.common.keys import keys  # 用于弹窗输入框的内容清空
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()                 ##打开谷歌浏览器
driver.get('https://dxt.yayi360.com/#/')    ##登录网址
driver.maximize_window()                    ##最大化浏览器

driver.find_element_by_xpath('//input[@placeholder = "请输入手机号"]').send_keys('18689490411')   ##定位手机号元素，并输入
driver.find_element_by_xpath('//input[@placeholder = "请输入密码"]').send_keys('123456')          ##定位密码元素，并输入
driver.find_element_by_xpath('//div[text() = "登录"]').click()                                   ##定位登录按钮，并点击

time.sleep(3)

url = driver.current_url ##获取当前页面URL
print(url)
print('👆 登录成功，当前页面的URL')

if url != 'https://dxt.yayi360.com/#/indexDoc':
    print('登录失败，请检查登录信息')
    driver.quit()
else:
    print(url)
    print('当前页面URL与预期一致，登录成功')

driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/span/img').click()   ##定位小三角，打开个人中心，相对路径
time.sleep(1)
#driver.find_element_by_xpath('//html/body/div/div[1]/div/div[2]/span/img ').click() ##定位小三角，打开个人中心，绝对路径
pass

driver.find_element_by_xpath('/html/body/ul/li[1]/a').click()    ##点击‘个人中心’，进入个人中心
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/button').click()                             ##点击修改
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/form/div/div/div/input').send_keys(Keys.CONTROL,'a')      ##全选医生名称
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/form/div/div/div/input').send_keys(Keys.BACKSPACE)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[4]/div/div[2]/div/form/div/div/div/input').send_keys('医生-黄金锋12修改')      ##修改医生名称
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[4]/div/div[3]/input[1]').click()     ##点击确定按钮
time.sleep(2)

driver.quit()