def printinfo( arg, *var ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg
   for var in var:
      print var
   return;


# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
