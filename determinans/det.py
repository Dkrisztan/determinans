import sys

print 'Add meg a11-et:',
a11=input()
print 'Add meg a12-t:',
a12=input()
print 'Add meg a13-at:',
a13=input()
print 'Add meg a21-et:',
a21=input()
print 'Add meg a22-t:',
a22=input()
print 'Add meg a23-at:',
a23=input()
print 'Add meg a31-et:',
a31=input()
print 'Add meg a32-t:',
a32=input()
print 'Add meg a33-at:',
a33=input()

eredmeny=a11*a22*a33+a21*a32*a13+a31*a12*a23-a13*a22*a31-a23*a32*a11-a33*a12*a21
print 'Az eredmeny:',eredmeny
