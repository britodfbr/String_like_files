from io import StringIO
import sys

iostr = StringIO('''Boa Noite,
Venho dizer que a noite é boa.
Att.
Brito ''')


print(iostr.readline())
print(iostr.readline())


print('='*10)

fp = StringIO()
def func(f):
    f.write("hello")

func(fp)
print(fp.getvalue())

print('='*10)


 
backup_stdout = sys.stdout
sys.stdout = StringIO()
 
# será escrito em um StringIO
print("hello world")
 
# pega uma referência ao objeto StringIO antes de restaurar a stdout
fp = sys.stdout
sys.stdout = backup_stdout
print("stdout: " + fp.getvalue())