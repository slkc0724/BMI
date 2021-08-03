weight = input('Your weight(kg): ')
height = input('Your height(cm): ')
weight = float(weight)
height = float(height)
bmi = weight / ((height / 100) * (height / 100)) 
print('Your BMI: ', bmi)
if bmi < 18.5:
	print('--> 體重過輕 :(')
elif bmi >= 18.5 and bmi < 24:
	print('--> 正常範圍 :)')
elif bmi >= 24 and bmi < 27:
	print('--> 異常範圍: 過重 :(')
elif bmi >= 27 and bmi < 30:
	print('--> 異常範圍: 輕度肥胖 :(')
elif bmi >= 30 and bmi <35:
	print('--> 異常範圍: 中度肥胖 :(')
else:
	print('--> 異常範圍: 重度肥胖 :(')