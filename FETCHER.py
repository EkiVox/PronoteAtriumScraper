from PRONOTE import CoursesFetcher
from PRONOTE import Atrium
import time
import pickle
class automateFetch:
    def automateFetch(self):
        try:
            creditentials = Atrium().reuseCreditentials()
            CoursesFetcher().login(creditentials[0], creditentials[1])
            courseslist = CoursesFetcher().fetch() #fetch courses and teachers
            CoursesFetcher().close() #Close browser
            CoursesFetcher().displaying(courseslist[0], courseslist[1]) #display the returned courses and teaches
            CoursesFetcher().saveCourses(courseslist)
            return courseslist
        except:
            quit()
