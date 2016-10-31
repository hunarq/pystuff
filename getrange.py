def getRange( strIP) :

  ip = strIP.split('/')
  n = int(ip[1] )
  sb = ip[0].split('.')
  hh =  ( long(sb[0] ) << 24 )  +  ( long(sb[1] ) << 16)  + ( long(sb[2] ) << 8)  +  long(sb[3] )

  st = int('1' * n + '0' * ( 32-n) , 2)
  en = int( '1' * n + '1' * ( 32-n), 2)

  return  (st & hh), ( en & hh )

#calling the function
a, b = getRange('2.3.4.124/30')
print a, b

