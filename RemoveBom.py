#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 15:11
# @Author  : Zhangyp
# @File    : RemoveBom.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import codecs


def remove_bom(file_path):
	with open(file_path, 'r+b') as file:
		data = file.read(3)
		if data == codecs.BOM_UTF8:  # 判断首字符是否为UTF8的BOM
			content = file.read()
			file.seek(0)
			file.write(content)
			file.truncate()


# def main():
# 	remove_bom(r'appsettings.ini')
#
#
# with open(r'appsettings.ini', 'r+b') as fd:
# 	data1 = fd.read()
# 	print(data1)
#
# if __name__ == main():
# 	main()
