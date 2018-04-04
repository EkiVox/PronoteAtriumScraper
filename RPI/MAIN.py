from LEDCONTROLLER import LedController
try:
    LedController().downloadCourses("localhost")
except IOError:
    print "impossible de se connecter"
list = LedController().getCourses()

ledlist = LedController().HandleCourses(list)
print ledlist
