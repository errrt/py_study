#print関数(v.3から)
print("Hello World")

#セミコロンで区切る
a = 12; b = 68; c = a*a-b
print(a+b, c)

#複数行にまたがる場合はバックスラッシュ
total = 123\
    +34\
    +789
print(total)

#,ノオ後ろのバックスラッシュは省略可能である
months = [ 'Jan', 'Feb', 'Mar', 'Apr',
           'May', 'Jun', 'Jul', 'Aug',
           'Sep', 'Oct', 'Nov', 'Dec' ]
print(months)

#indent---boolはif文に含まれるがcccはif文に含まれない
a = 3
if a == 3:
    print("TRUE")   
    print("FALSE")
print("ccc")

#コーディング
# coding: utf-8
print("よろしく")