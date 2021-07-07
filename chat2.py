#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


# 對話紀錄記數
def convert(lines):
	person = None # 宣告變數 避免開頭無名字的狀況
	allen_word_count = 0
	allen_sticker_count = 0
	allen_photo_count = 0
	viki_word_count = 0
	viki_sticker_count =0
	viki_photo_count = 0

	for line in lines:
		s = line.split(' ') # 以空白作切割 切完會變清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_photo_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_photo_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen說了', allen_word_count, '字',',傳了', allen_sticker_count, '個貼圖')
	print('Allen傳了', allen_photo_count, '張圖片')
	print('Viki說了', viki_word_count, '字', ',傳了', viki_sticker_count, '個貼圖')
	print('Viki傳了', viki_photo_count, '張圖片')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)

main()