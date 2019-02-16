import string
import re
import cflw工具_运算 as 运算
#===============================================================================
# 常量
#===============================================================================
#字符串
c字符串_半角字母数字符号 = string.ascii_letters + string.digits + string.punctuation
c字符串_全角数字 = '０１２３４５６７８９'
c字符串_全角小写字母 = 'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
c字符串_全角大写字母 = 'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
#编码范围，使用unicode编码
c编码范围_半角字符 = range(0x21, 0x7f)
c编码范围_全角字符 = range(0x2e80, 0xd7ff)
c编码范围_汉字 = range(0x4e00, 0x9fa6)
#正则表达式,需要编译
c正则表达式_文字 = r"[\w\u4e00-\u9fa6]"
ca汉字大小写 = [
	("一", "壹"),
	("二", "贰"),
	("三", "叁"),
	("四", "肆"),
	("五", "伍"),
	("六", "陆"),
	("七", "柒"),
	("八", "捌"),
	("九", "玖"),
	("十", "拾"),
	("百", "佰"),
	("千", "仟")
]
#===============================================================================
# 字符操作
#===============================================================================
def fi半角字符(a字符):
	v编码 = ord(a字符)
	return v编码 in c编码范围_半角字符
def fi汉字(a字符):
	v编码 = ord(a字符)
	return v编码 in c编码范围_汉字
def f计算字符宽度(a字符: str):
	"汉字，全角字符算2个字符宽，tab算8个字符宽"
	v编码 = ord(a字符)
	if v编码 in c编码范围_半角字符:	#半角字符
		return 1
	elif v编码 in c编码范围_全角字符:	#全角字符
		return 2
	elif v编码 == 9:	#制表符
		return 8
	else:	#未知
		return 0
#===============================================================================
# 字符串查找&计算
#===============================================================================
def f计算字符串宽度(a字符串):
	v字符串 = str(a字符串)
	v宽度 = 0
	for v in v字符串:
		v宽度 += f计算字符宽度(v)
	return v宽度
def f统计汉字数量(a字符串):
	"统计字符串中出现的汉字的字数"
	v字符串 = str(a字符串)
	v数量 = 0
	for v in v字符串:
		if fi汉字(v):
			v数量 += 1
	return v数量
def f全部找(a字符串: str, a找: str):
	v列表 = []
	v位置 = 0
	while True:
		v位置 = a字符串.find(a找, v位置)
		if v位置 >= 0:
			v列表.append(v位置)
			v位置 += 1
		else:
			break
	return v列表
def f重复找(a字符串: str, a找: str):
	v位置 = 0
	while True:
		v位置 = a字符串.find(a找, v位置)
		if v位置 >= 0:
			yield v位置
			v位置 += 1
		else:
			break
def f连续找最后(a字符串: str, *aa找, a开始 = 0):
	"根据要找的字符串一直往后找"
	v位置 = a开始 - 1
	for v找 in aa找:
		v位置 = a字符串.find(v找, v位置 + 1)
		if v位置 < 0:
			break
	return v位置
def fe分隔后每组长度(a字符串, a分隔):
	va分隔 = a字符串.split(a分隔)
	for v字符串 in va分隔:
		yield len(v字符串)
def f找前面匹配(aa字符串, a找, a标记 = 0):
	'从列表中找出前面与a字符串匹配的项'
	v正则 = re.compile(r"^" + a找, a标记)
	v长度 = len(a找)
	for v字符串 in aa字符串:
		if type(v字符串) != str:
			raise TypeError("元素类型必须是字符串")
		if re.search(v正则, v字符串):
			return v字符串
def fi前面匹配(a原始字符串, a查找字符串, a标记 = 0):
	v正则 = re.compile(a查找字符串, a标记)
	if re.match(v正则, a原始字符串):
		return True
	else:
		return False
def f找字符串之间(a字符串, a开始, a结束, a包含开始 = False, a反向查找 = False):
	"""找原始字符串中开始到结束字符串之间的字符串,返回切片
例如:f("a.b.c.d", "." ,".")返回slice(1,3)
	"""
	def f找不到(a位置):
		if a位置 == -1:	#找不到返回None
			return None
		else:	#找到返回位置
			return a位置
	def f新位置(a位置, a偏移):
		if a位置 != None:
			return a位置 + a偏移
		else:
			return None
	#找位置
	if a反向查找:
		if a结束:
			v结束位置 = a字符串.rfind(a结束)
			v结束位置 = f找不到(v结束位置)
		else:
			v结束位置 = -1
		if a开始:
			v结束位置1 = f新位置(v结束位置 , -1)
			v开始位置 = a字符串.rfind(a开始, None, v结束位置1)
			v开始位置 = f找不到(v开始位置)
		else:
			v开始位置 = 0
	else:	#正向查找
		if a开始:
			v开始位置 = a字符串.find(a开始)
			v开始位置 = f找不到(v开始位置)
		else:
			v开始位置 = 0
		if a结束:
			v开始位置1 = f新位置(v开始位置, 1)
			v结束位置 = a字符串.find(a结束, v开始位置1)
			v结束位置 = f找不到(v结束位置)
		else:
			v结束位置 = -1
	#返回
	if a包含开始 or v开始位置 == None:
		return slice(v开始位置, v结束位置)
	else:
		v开始长度 = len(a开始)
		return slice(v开始位置 + v开始长度, v结束位置)
#===============================================================================
# 字符串操作,返回字符串
#===============================================================================
def f去头尾空白(a字符串: str):
	return a字符串.strip()
def f去前面(a字符串: str, a前面: str):
	"前面及更前的字符串全部去除"
	v位置 = a字符串.find(a前面)
	if v位置 > 0:
		return a字符串[v位置 + len(a前面):]
	return a字符串
def f去后面(a字符串: str, a后面: str):
	"后面及更后的字符串全部去除"
	v位置 = a字符串.rfind(a后面)
	if v位置 > 0:
		return a字符串[:v位置]
	return a字符串
def f插入字符串(a字符串, a位置, a插入字符串):
	return a字符串[:a位置] + a插入字符串 + a字符串[a位置:]
def f隔段插入字符串(a字符串, a插入字符串, a间隔):
	v字符串 = str(a字符串)
	v类型 = type(a间隔)
	if v类型 == int:
		v长度 = len(a字符串)
		v余数 = v长度 % a间隔
		if v余数 == 0:	#不能包含尾
			i = v长度 - a间隔
		else:
			i = v长度 - v余数
		while i > 0:
			v字符串 = f插入字符串(v字符串, i, a插入字符串)
			i -= a间隔
	elif v类型 == range:
		v长度 = len(a字符串)
		v尾 = int(a间隔.stop)
		v头 = int(a间隔.start)
		v步进 = int(a间隔.step)
		if v头 < 0:
			v头 = v步进
		v余数 = (v尾 - v头) % v步进
		if v余数 == 0:	#不能包含尾
			i = v长度 - v步进
		else:
			i = v长度 - v余数
		while i >= v头:
			v字符串 = f插入字符串(v字符串, i, a插入字符串)
			i -= v步进
			if i == 0:
				break	#不能包含头
	else:
		raise TypeError
	return v字符串
def fe字符串特定字符之间(a字符串, a字符, a开始位置 = 0):
	v字符长度 = len(a字符)
	v开始位置 = a开始位置
	v结束位置 = 0
	while True:
		v结束位置 = a字符串.find(a字符, v开始位置 + 1)
		if v结束位置 == -1:
			yield a字符串[v开始位置 : ]
		else:
			yield a字符串[v开始位置 : v结束位置]
		v开始位置 = v结束位置 + v字符长度
def f提取字符串之间(a字符串, a开始, a结束, a包含开始 = False, a反向查找 = False):
	"""找原始字符串中开始到结束字符串之间的字符串,找不到返回""
例如:f("a.b.c.d", "." ,".")返回"b"
	"""
	v位置 = f找字符串之间(a字符串, a开始, a结束, a包含开始, a反向查找)
	#找不到则返回空字符串
	if v位置.start == None:
		return ""
	if v位置.stop == None:
		return ""
	#正常返回
	return a字符串[v位置]
def f转大写数字(a字符串):
	v字符串 = str(a字符串)
	for v in ca汉字大小写:
		v字符串.replace(v[0], v[1])
	return v字符串
def fe分割(a字符串, a分割 = "\n", a开始位置 = 0):
	v开始位置 = a开始位置
	v长度 = len(a字符串)
	while True:
		v结束位置 = a字符串.find(a分割, v开始位置)
		if v结束位置 == -1:
			yield a字符串[v开始位置:]
			break
		else:
			yield a字符串[v开始位置 : v结束位置]
			v开始位置 = v结束位置 + 1
			if v开始位置 >= v长度:
				break
def fe按位置分割(a字符串, *aa位置, af暂回 = str.strip):
	"包含位置字符"
	v开始 = 0
	vf暂回处理 = af暂回 if af暂回 else 运算.f原值
	for v位置 in aa位置:
		if v位置 == 0:
			continue
		v结束 = v位置
		yield vf暂回处理(a字符串[v开始:v结束])
		v开始 = v结束
	yield vf暂回处理(a字符串[v开始:])	#最后一列
def fe按字符分割(a字符串, *aa字符, af暂回 = str.strip):
	"不包含分割字符"
	v开始 = 0
	vf暂回处理 = af暂回 if af暂回 else 运算.f原值
	for v字符 in aa字符:
		v结束 = a字符串.find(v字符, v开始)
		yield vf暂回处理(a字符串[v开始:v结束])
		v开始 = v结束 + 1
	if v开始 < len(a字符串):
		yield vf暂回处理(a字符串[v开始:])
def f回车处理(a字符串: str):
	"\\r后的字符会覆盖行首内容"
	va行 = []
	for v原行 in a字符串.split("\n"):
		v新行 = ""
		#遍历\r,覆盖行首
		v开始位置 = 0
		while True:
			v结束位置 = v原行.find("\r", v开始位置)
			if v结束位置 >= 0:
				v新行 = f覆盖(v新行, v原行[v开始位置 : v结束位置])
			else:
				v新行 = f覆盖(v新行, v原行[v开始位置:])
				break
			v开始位置 = v结束位置 + 1
		va行.append(v新行)
	return "\n".join(va行)
def f覆盖(a原: str, a新: str, a开始位置 = 0):
	if not a新:	#没东西不覆盖
		return a原
	v原长度 = len(a原)
	if a开始位置 > v原长度:
		raise ValueError("开始位置不能超过原字符串长度")
	v目标长度 = a开始位置 + len(a新)
	if v目标长度 > v原长度:
		return a原[0 : a开始位置] + a新
	else:
		return a原[0 : a开始位置] + a新 + a原[v目标长度:]
#===============================================================================
# 字符串转换
#===============================================================================
def ft字符串(*a元组, a分隔符 = "\t"):
	v格式 = "%s" + a分隔符
	return (v格式 * len(a元组)) % a元组
def ft字符串序列(a序列):
	for v in a序列:
		yield str(v)
#===============================================================================
# 文本对齐
#===============================================================================
class C文本对齐处理:
	def __init__(self, a宽度, a对齐方向 = -1):
		self.m宽度 = a宽度
		self.fs对齐方向(a对齐方向)
		self.fs边距(0, 0)
	def fs对齐方向(self, a对齐方向):
		if type(a对齐方向) in (int, float):
			self.m对齐方向 = a对齐方向
		elif type(a对齐方向) == str:
			v字符 = a对齐方向[0]
			if 'l' == v字符:
				self.m对齐方向 = -1
			elif 'r' == v字符:
				self.m对齐方向 = 1
			elif 'c' == v字符:
				self.m对齐方向 = 0
			elif '左' == v字符:
				self.m对齐方向 = -1
			elif '右' == v字符:
				self.m对齐方向 = 1
			elif '中' == v字符 or '居中' == a对齐方向[0:2]:
				self.m对齐方向 = 0
			else:
				raise ValueError
		else:
			raise TypeError
	def fs边距(self, a左边距, a右边距):
		self.m左边距 = a左边距
		self.m右边距 = a右边距
	def f处理(self, a字符串):
		'把原字符串转换成对齐后的字符串'
		v宽度 = f取宽度(a字符串)
		v空格 = self.m宽度 - v宽度
		if v空格 < 0:
			raise ValueError('参数字符串的宽度超出范围')
		if self.fi左对齐():
			v处理后 = a字符串 + ' ' * v空格
		elif self.fi右对齐():
			v处理后 = ' ' * v空格 + a字符串
		return ' ' * self.m左边距 + v处理后 + ' ' * self.m右边距
	def fi左对齐():
		return self.m对齐方向 < 0
	def fi右对齐():
		return self.m对齐方向 > 0
	def fi居中对齐():
		return self.m对齐方向 == 0
#===============================================================================
# 模板
#===============================================================================
class C模板:
	c匹配括号 = re.compile(r"\{" + c正则表达式_文字 + r"+\}")
	def __init__(self, s: str):
		self.m字符串 = s
		self.ma参数 = []
		v列表 = C模板.c匹配括号.findall(s)
		for v in v列表:
			self.ma参数.append((C模板.f去括号(v), v))	#添加("k", "{k}"),前者用于查找,后者用于替换
	def f替换(self, **d):
		v字符串 = self.m字符串
		for v参数 in self.ma参数:
			k = v参数[0]
			if k in d:
				v = str(d[k])
				v字符串 = v字符串.replace(v参数[1], v)
		return v字符串
	@staticmethod
	def f去括号(s: str)->str:
		return s[1:-1]
	@staticmethod
	def f加括号(s: str)->str:
		return "{" + s + "}"