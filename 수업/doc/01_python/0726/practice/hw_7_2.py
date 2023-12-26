# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   def repeat_string(self, count, text):
      for _ in range(3):  # 0 ~ 2
         print(text) 

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")