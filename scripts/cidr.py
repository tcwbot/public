###
# Calculates CIDR
# written : tcwbot
###

def cidr_all(block):
    cidr=32
    for x in range(33-block):
        if (cidr<=32 and cidr>=25):
            print(f'{32-x} 255.255.255.{256-pow(2,x%8)} ')
        if (cidr<=24 and cidr>=17):
            print(f'{32-x} 255.255.{256-pow(2,x%8)}.0')
        if (cidr<=16 and cidr>=9):
            print(f'{32-x} 255.{256-pow(2,x%8)}.0.0')
        if (cidr<=8 and cidr>0):
            print(f'{32-x} {256-pow(2,x%8)}.0.0.0')
        if (cidr==0):
            print(f'{32-x} 0.0.0.0')
        cidr-=1

def cidr(block):
    cidr=32
    for x in range(33-block):
        if (cidr<=32 and cidr>=25):
            result=(f'{32-x} 255.255.255.{256-pow(2,x%8)} {pow(2,x):,d}')
        if (cidr<=24 and cidr>=17):
            result=(f'{32-x} 255.255.{256-pow(2,x%8)}.0 {pow(2,x):,d}')
        if (cidr<=16 and cidr>=9):
            result=(f'{32-x} 255.{256-pow(2,x%8)}.0.0 {pow(2,x):,d}')
        if (cidr<=8 and cidr>0):
            result=(f'{32-x} {256-pow(2,x%8)}.0.0.0 {pow(2,x):,d}')
        if (cidr==0):
            result=(f'{32-x} 0.0.0.0 {pow(2,x)}')
        cidr-=1
    print(result)

def print_ips(x,):
    cidr(x)



print_ips(13)
