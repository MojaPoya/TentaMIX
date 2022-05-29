import MA1



#print(MA1.power(3,4))
#print(MA1.multiply(0,8))
#print(MA1.divide(12,3))
#print(MA1.harmonic(20))
#print(MA1.digit_sum(101207))
#print(MA1.reverse('0123456789'))


lst=[5,3,7,11,4]

#print(MA1.largest(lst))
#print(lst)
#print(MA1.count2(4, [1, [4, 4], 3, 1, 4, 2, ['a', [[4, 4], 4, 4],4,4 ],4 ] ))
#print(MA1.count([4,4],[[4,4]]))
#print(MA1.zippa([1,3,5,9],[2,4,6,7,8]))


def exchange(a, coins): #159 sätt 100, på 1000 hittas inte maxium recursion depth
    if a == 0:
        return 1
    elif (a < 0) or len(coins) == 0:
        return 0
    else:
        return exchange(a, coins[1:]) + \
        exchange(a-coins[0], coins)

#print(exchange(1000,[1,5,10,50,100]))

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

#print(fac(997)) Max 997
print(MA1.bricklek('f','t','h',3))