import time
import requests

# 目标网址
url_1 = "https://xhsz.news.cn/curriculum/detail/2407"




url_FengJinghui = "https://zgylqxzz.xml-journal.net/article/doi/10.12455/j.issn.1671-7104.240014?_sowise_access=email_924621"
url_ANOVA = "https://bme.gzhmu.edu.cn/info/1147/6110.htm"


# 无限循环访问
try:
    while True:
        # 发起GET请求
        response_1 = requests.get(url_1)



        response_2 = requests.get(url_FengJinghui)
        response_3 = requests.get(url_ANOVA)


        # 每0.3秒访问一次
        time.sleep(10)
except KeyboardInterrupt:
    print("\n程序已停止。")
except Exception as e:
    print(f"发生错误: {e}")
