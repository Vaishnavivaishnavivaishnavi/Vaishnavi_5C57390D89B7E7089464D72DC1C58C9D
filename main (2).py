def isleapyear(year):
  if(year % 4==0 and year % 100!=0)or year % 400==0:
    return true
  else:
    return false
year=int(input("enter a year:"))
if islapyear(year):
  print('{} is a leap year.'.formate(year))
else:
  print('{} is not a leapyear.'.format(year))