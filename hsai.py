#CREATED BY SMJ
import colored

from colored import fg , attr

col1 = fg('red')
col2 = fg('green')
reset = attr('reset')
x = ('HAMZAH' , 'hamzah' , 'SABA' , 'saba' , 'Saba' , 'Hamzah' ,'Sarim' , 'SARIM' , 'sarim')

n=str(input('ENTER YOUR NAME:'))

if n in x:
   print(col1,'BLOODY MORONNNN',reset)
else:
   print(col2,'SHAREEF',reset)
