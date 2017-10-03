'''Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
an + bn = cn
for any values of n greater than 2.
This method does not prove the theorem, but rather allows the user to input integer values
to see whether the valeues are contstrained to Fermat's Theorem
'''

def check_fermat(a,b,c,n):
    l=a**n + b**n
    r=c**n
    if l==r and n>2:
        print("Holy smaokes,Fermat was wrong!")
    else:
        print("No,that doesn't work")
        
check_fermat(9,80,56,2)
