#CREATED BY SMJ
import colored

from colored import fg , attr

col1 = fg('red')
col2 = fg('green')
col3 = fg('blue')
reset = attr('reset')
x = ('HAMZAH' , 'hamzah' , 'Hamzah' ,'Sarim' , 'SARIM' , 'sarim')
y = ('SALAH' , 'Salah' , 'salah')

n=str(input('ENTER YOUR NAME:'))

if n in x:
	print(col1,'BLOODY MORONNNN',reset)
elif n in y:
	print(col2,'SHAREEF',reset)
else:
	print(col3,'I DON\'T KNOW HIM',reset)
