# encoding: utf-8
from translate import Translator
# translator包经过实验暂时只发现可以将部分中文和英文互译，并且英文结果不是很准确


# 输入需要翻译的文本（中文）
originalText = input("=====请输入您要翻译的内容：=====\n")

# 中文->英文
translator = Translator(from_lang="chinese", to_lang="english")
translation = translator.translate(originalText)
print("=====翻译的英文为：=====\n%s"%(translation))

# 英文->中文（转换失败，暂未找到原因）
translator = Translator(from_lang="english", to_lang="chinese")
translation = translator.translate(translation)
print("=====转换后的中文为：=====\n%s"%(translation))

