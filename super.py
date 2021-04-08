## Super Random, Copyright (c) 2021 TFB
## Use freely under zlib terms, see licence file.

from time import time_ns as nanoseconds

##  initialise the process, work out the numbers
##  then update the random seed, return a floating result
##  and do a nano hop.

def super_random() :

    global first, second, random_seed

    normalisation()

    new_seed=''; nines=0; whole=False;
    num1=0; num2=0; num3=0; num4=0; result='';

    for f in range(0,8,1) :
        num1=int(first[f])
        num2=int(second[f])
        if f>3 :
            num3=int(random_seed[f-4])
            num4=str(num1+num2+num3)
            if int(num4)>9 :
                if f>6 and nines>=7 :
                    whole=True
                if int(num4)>18 :
                    new_seed=new_seed+str(int(num4)-18)
                else :
                    new_seed=new_seed+str(int(num4)-9)
            else :
                new_seed=new_seed+str(int(num4))[-1]
        else :
            num4=str(num1+num2)
        result=result+num4[-1]
        if num4[-1]=='9' :
            nines=nines+1

    if whole :
        result=float(1.00000000)
    else :
        result=result+'.' ; result=float(result[-1:-10:-1])
    feed_the_seed(new_seed)

    nano_hop()

    return result

##  this is the same as super_random()
##  but without the hop delay.

def super_fast_random() :

    global first, second, random_seed

    normalisation()

    new_seed=''; nines=0; whole=False;
    num1=0; num2=0; num3=0; num4=0; result='';

    for f in range(0,8,1) :
        num1=int(first[f])
        num2=int(second[f])
        if f>3 :
            num3=int(random_seed[f-4])
            num4=str(num1+num2+num3)
            if int(num4)>9 :
                if f>6 and nines>=7 :
                    whole=True
                if int(num4)>18 :
                    new_seed=new_seed+str(int(num4)-18)
                else :
                    new_seed=new_seed+str(int(num4)-9)
            else :
                new_seed=new_seed+str(int(num4))[-1]
        else :
            num4=str(num1+num2)
        result=result+num4[-1]
        if num4[-1]=='9' :
            nines=nines+1

    if whole :
        result=float(1.00000000)
    else :
        result=result+'.' ; result=float(result[-1:-10:-1])
    feed_the_seed(new_seed)

    return result

##  update or manually change the random seed.

def feed_the_seed(seed='1234') :

    global random_seed

    random_seed=seed

    return

##  find the reference points where the time varies.

def find_refs() :
    
    global for_ref, back_ref, decimal_places
    
    samp_zeros=0 ; sample_size=12
    decimal_places=8
    reference_length=len(str(nanoseconds()))

    for samp_loops in range(sample_size) :
        sample1=str(nanoseconds()); sample2=str(nanoseconds())
        while sample1==sample2 :
            sample2=str(nanoseconds())
        sample2=sample2.rstrip('0')
        samp_zeros=samp_zeros+(len(sample1)-len(sample2))
    
    reference_zeros=int(samp_zeros/sample_size)
    for_ref=reference_length-(decimal_places+reference_zeros)
    back_ref=-(reference_zeros+decimal_places+1)
    
    return

##  ensures the timer has moved on since the last sample
##  as possible to run many times in a nanosecond.

def nano_hop() :
    
    sample1=str(nanoseconds()); sample2=str(nanoseconds())
    while sample1==sample2 :
        sample2=str(nanoseconds())
    return

##  make sure the numbers are in strings and padded with zeros.

def normalisation() :
    
    global first, second, random_seed

    first=str(nanoseconds())[for_ref:for_ref+decimal_places:1].zfill(8)
    second=str(nanoseconds())[back_ref+decimal_places:back_ref:-1].zfill(8)

    random_seed=str(random_seed).zfill(4)[0:4:1]    #user seed string, padded to 4 zeros.

    return

###########################################
## these run when the module is imported ##
###########################################

try : random_seed
except NameError : random_seed='1234'

try : for_ref
except NameError : find_refs()

###########################################
