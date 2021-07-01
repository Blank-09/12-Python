from math import floor

def createPattern(sym, val=9, spacing=' ', terminate=' '):
  height = floor(val/2)

  for i in range(val):
    for j in range(val):
      if j < (val + height  - i) and j >= (i + height + 1 - val) and j >= (height - i) and j <= (height + i):
        j = sym
      else: j=spacing
      print(j, end=terminate)
    print()

createPattern('}-{')
createPattern(')-(')

'''
createPattern(')-(')

            }-{
          }-{ }-{ }-{
        }-{ }-{ }-{ }-{ }-{
      }-{ }-{ }-{ }-{ }-{ }-{ }-{       
    }-{ }-{ }-{ }-{ }-{ }-{ }-{ }-{ }-{ 
      }-{ }-{ }-{ }-{ }-{ }-{ }-{       
        }-{ }-{ }-{ }-{ }-{
          }-{ }-{ }-{
            }-{


createPattern(')-(')

            )-(
          )-( )-( )-(
        )-( )-( )-( )-( )-(
      )-( )-( )-( )-( )-( )-( )-(
    )-( )-( )-( )-( )-( )-( )-( )-( )-(
      )-( )-( )-( )-( )-( )-( )-(
        )-( )-( )-( )-( )-(     
          )-( )-( )-(
            )-(


createPattern('PRIYANSHU')

        PRIYANSHU
      PRIYANSHU PRIYANSHU PRIYANSHU
    PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU
  PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU
PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU
  PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU
    PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU PRIYANSHU
      PRIYANSHU PRIYANSHU PRIYANSHU
        PRIYANSHU


createPattern('<')
          <
        < < <       
      < < < < <     
    < < < < < < <   
  < < < < < < < < < 
    < < < < < < <   
      < < < < <     
        < < <       
          <

createPattern('<>')
        <>
      <> <> <>
    <> <> <> <> <>
  <> <> <> <> <> <> <>
<> <> <> <> <> <> <> <> <>
  <> <> <> <> <> <> <>
    <> <> <> <> <>
      <> <> <>
        <>

createPattern('><')
         ><
      >< >< ><
    >< >< >< >< ><
  >< >< >< >< >< >< ><
>< >< >< >< >< >< >< >< ><
  >< >< >< >< >< >< ><
    >< >< >< >< ><
      >< >< ><
        ><

createPattern('{}')
        {}
      {} {} {}
    {} {} {} {} {}
  {} {} {} {} {} {} {}
{} {} {} {} {} {} {} {} {}
  {} {} {} {} {} {} {}
    {} {} {} {} {}
      {} {} {}
        {}

createPattern('}-{')
        }-{
      }-{ }-{ }-{
    }-{ }-{ }-{ }-{ }-{
  }-{ }-{ }-{ }-{ }-{ }-{ }-{
}-{ }-{ }-{ }-{ }-{ }-{ }-{ }-{ }-{
  }-{ }-{ }-{ }-{ }-{ }-{ }-{
    }-{ }-{ }-{ }-{ }-{
      }-{ }-{ }-{
        }-{

createPattern('}{')
        }{
      }{ }{ }{
    }{ }{ }{ }{ }{
  }{ }{ }{ }{ }{ }{ }{
}{ }{ }{ }{ }{ }{ }{ }{ }{
  }{ }{ }{ }{ }{ }{ }{
    }{ }{ }{ }{ }{     
      }{ }{ }{
        }{

createPattern('-Z-')
        -Z-
      -Z- -Z- -Z-
    -Z- -Z- -Z- -Z- -Z-
  -Z- -Z- -Z- -Z- -Z- -Z- -Z-
-Z- -Z- -Z- -Z- -Z- -Z- -Z- -Z- -Z-
  -Z- -Z- -Z- -Z- -Z- -Z- -Z-
    -Z- -Z- -Z- -Z- -Z-
      -Z- -Z- -Z-
        -Z-

createPattern('-Z-', 9, ' ', '')
    -Z-
   -Z--Z--Z-
  -Z--Z--Z--Z--Z-
 -Z--Z--Z--Z--Z--Z--Z-
-Z--Z--Z--Z--Z--Z--Z--Z--Z-
 -Z--Z--Z--Z--Z--Z--Z-
  -Z--Z--Z--Z--Z-
   -Z--Z--Z-
    -Z-

createPattern(sym='Z',spacing='-')
- - - - Z - - - - 
- - - Z Z Z - - -
- - Z Z Z Z Z - -
- Z Z Z Z Z Z Z -
Z Z Z Z Z Z Z Z Z
- Z Z Z Z Z Z Z -
- - Z Z Z Z Z - -
- - - Z Z Z - - -
- - - - Z - - - -

createPattern('X', 9, '','')
    X    
   XXX
  XXXXX
 XXXXXXX
XXXXXXXXX
 XXXXXXX
  XXXXX
   XXX
    X
'''