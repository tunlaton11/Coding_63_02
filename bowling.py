

score_value = {
	'-': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'X': 10,
	'/': 10
} #ค่าของคะแนนใน frame

def cal_score(score_sheet): #ฟังชั่นคำนวณคะแนนใน frame
	score_sheet = score_sheet.split()	
	total_score = 0
	for i, frame in enumerate(score_sheet): # i เป็น count , frame เป็นค่าใน score_sheet
		score = 0
		if frame == 'X':
			score = 10
			next_frame = score_sheet[i + 1]
			score += score_value[next_frame[0]]
			if len(next_frame) == 1:
				score += score_value[score_sheet[i + 2][0]]
			else:
				score += score_value[next_frame[1]]
		elif frame[1] == '/' and len(frame) == 2:
			score = 10
			score += score_value[score_sheet[i + 1][0]]
		else:
			if i == 9 and frame[1] == '/': 
				score += 10 + score_value[frame[2]]
			else:
				for c in frame:
					score += score_value[c]

		total_score += score

		print('\t'.join([str(i), frame, str(score), str(total_score)]))

	return total_score


def input_score(): #ฟังชั่นหลักในการ input และ output
    score_sheet = input("Input bowling's frame : ") # ตัวอย่าง input (ใส่บรรทัดเดียวคั่นด้วย space) -> X -/ X 5- 8/ 9- X 81 1- 4/X
    print('\t'.join(['Round', 'frame', 'score', 'total']))
    print("Total Score: ", cal_score(score_sheet))

input_score()
