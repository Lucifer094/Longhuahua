from urllib import request, parse
import json
# 通过有道进行翻译，自己不太懂网页响应，暂时只能找到智能翻译的，智能翻译默认英语-汉语互译

# 有道翻译：中文→英文
def translate_zh_en(text):
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
    # 创建要提交的数据
    Form_Date = {}
    Form_Date['i'] = text
    Form_Date['doctype'] = 'json'
    Form_Date['form'] = 'zh'                    # 原始语言
    Form_Date['to'] = 'en'                      # 目标语言
    Form_Date['smartresult'] = 'dict'
    Form_Date['client'] = 'fanyideskweb'
    Form_Date['salt'] = '1526995097962'
    Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
    Form_Date['version'] = '2.1'
    Form_Date['keyform'] = 'fanyi.web'
    Form_Date['action'] = 'FY_BY_REALTIME'
    Form_Date['typoResult'] = 'false'

    data = parse.urlencode(Form_Date).encode('utf-8')  # 数据转换
    response = request.urlopen(req_url, data)  # 提交数据并解析
    html = response.read().decode('utf-8')  # 服务器返回结果读取
    # print(html)
    # 可以看出html是一个json格式
    translate_results = json.loads(html)  # 以json格式载入
    translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
    # print(translate_results)  # 输出结果
    return translate_results  # 返回结果


# 输入需要翻译的文本（中文）
originalText = input("=====请输入您要翻译的内容：=====\n")


translation = translate_zh_en(originalText)
print("=====翻译的英文为：=====\n%s"%(translation))

res = translate_zh_en(translation)
print(res)  # 这是一只狗