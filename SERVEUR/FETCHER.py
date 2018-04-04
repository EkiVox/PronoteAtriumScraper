from PRONOTE import CoursesFetcher
from PRONOTE import Atrium
import time
import pickle
class automateFetch:
    def automateFetch(self):
        try:
            creditentials = Atrium().reuseCreditentials()
            CoursesFetcher().initialize()
            CoursesFetcher().login(creditentials[0], creditentials[1])
            courseslist = CoursesFetcher().fetch() #fetch courses and teachers
            CoursesFetcher().close() #Close browser
            CoursesFetcher().saveCourses(courseslist)
            return courseslist
        except:
            print "error in fetching"
