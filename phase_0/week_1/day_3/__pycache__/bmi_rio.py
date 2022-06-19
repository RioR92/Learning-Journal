def bmi (weight,height) :
  bmi_calc = weight / ((height/100)**2)
  if bmi_calc > 0 :
    if bmi_calc > 30 :
      print(f'your bmi index is {bmi_calc} and categorized as VERY OVERWEIGHT')
    elif 25 <= bmi_calc <= 29.9 :
      print(f'your bmi index is {bmi_calc} and categorized as OVERWEIGHT')
    elif 18.5 <= bmi_calc < 25 :
      print(f'your bmi index is {bmi_calc} and categorized as NORMAL')
    else :
      print(f'your bmi index is {bmi_calc} and categorized as UNDERWEIGHT')