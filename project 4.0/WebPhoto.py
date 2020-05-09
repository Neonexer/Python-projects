import cv2
import os
class MakePhoto():
	def Photo():
		cap = cv2.VideoCapture(0)

		for i in range(30):
			cap.read()

		ret, frame = cap.read()

		cv2.imwrite(f'C:\\Users\\{os.getlogin()}\\Desktop\\cam.png', frame)

		cap.release()
		
if __name__ == '__main__':
	print('Вы запустили это как основную программу, а это модуль!')
	input()