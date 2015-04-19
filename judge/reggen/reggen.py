#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 2:
	print "Launch with 'python reggen FILTHY_WORD'"
	sys.exit(1)

word = unicode(sys.argv[1], 'utf-8')

letter_replacement = {
	u'\u0430': ['а', 'a', '@'],
	u'\u0430': ['а', 'a', '@'],
	u'\u0431': ['б', '6', 'b'],
	u'\u0432': ['в', 'b', 'v'],
	u'\u0433': ['г', 'r', 'g'],
	u'\u0434': ['д', 'd', 'g'],
	u'\u0435': ['е', 'e'],
	u'\u0451': ['ё', 'е', 'e'],
	u'\u0436': ['ж', 'zh', '*'],
	u'\u0437': ['з', '3', 'z'],
	u'\u0438': ['и', 'u', 'i'],
	u'\u0439': ['й', 'u', 'y', 'i'],
	u'\u043a': ['к', 'k', 'i{', '|{'],
	u'\u043b': ['л', 'l', 'ji'],
	u'\u043c': ['м', 'm'],
	u'\u043d': ['н', 'h', 'n'],
	u'\u043e': ['о', 'o', '0'],
	u'\u043f': ['п', 'n', 'p'],
	u'\u0440': ['р', 'r', 'p'],
	u'\u0441': ['с', 'c', 's'],
	u'\u0442': ['т', 'm', 't'],
	u'\u0443': ['у', 'y', 'u'],
	u'\u0444': ['ф', 'f'],
	u'\u0445': ['х', 'x', 'h', 'к', 'k', '}{'],
	u'\u0446': ['ц', 'c', 'u,'],
	u'\u0447': ['ч', 'ch'],
	u'\u0448': ['ш', 'sh'],
	u'\u0449': ['щ', 'sch'],
	u'\u044a': ['ь', 'b'],
	u'\u044b': ['ы', 'bi'],
	u'\u044c': ['ъ'],
	u'\u044d': ['э', 'е', 'e'],
	u'\u044e': ['ю', 'io'],
	u'\u044f': ['я', 'ya']
}

ANYCHAR_REGEX = '[^а-яА-ЯA-Za-z0-9_]{0,2}'

def genForChar(c):
	res = ANYCHAR_REGEX + '(' + letter_replacement[c][0]
	for replacement in letter_replacement[c][1:]:
		res += '|' + replacement
	res += ")"

	return res
	
result = "^((?:"

result += letter_replacement[word[0]][0]

for replacement in letter_replacement[word[0]][1:-1]:
	result += '|' + replacement
result += ')'

for c in word[1:-1]:
	result += genForChar(c)
	
result += '' + ANYCHAR_REGEX + '((о|o|0)' + ANYCHAR_REGEX + '(й|u|y|i)|(е|e)' + ANYCHAR_REGEX + '(й|u|y|i)|(ё|е|e)' + ANYCHAR_REGEX + '(й|u|y|i)|(о|o|0)' + ANYCHAR_REGEX + '(м|m)|(е|e)' + ANYCHAR_REGEX + '(м|m)|(я|ya)' + ANYCHAR_REGEX + '(м|m)|[а-я])?)$'

print result
