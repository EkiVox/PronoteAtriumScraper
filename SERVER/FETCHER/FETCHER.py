from PRONOTE import CoursesFetcher
from PRONOTE import Atrium
import time
import pickle
import hashlib


class OPwithID:
    def Fetch(self, id):
        creditentials = Atrium().reuseCreditentials(id)
        CoursesFetcher().initialize()
        CoursesFetcher().login(creditentials[0], creditentials[1])
        courseslist = CoursesFetcher().fetch() #fetch courses and teachers
        CoursesFetcher().close() #Close browser
        return courseslist

    def Store(self, id, password, credits):
        self.hasher = hashlib.md5()
        self.hasher.update(password)
        password = self.hasher.digest()
        passfile = open('password-' + id + '.conf', 'r')
        stockedpassword = pickle.load(passfile)
        if stockedpassword == password:
            Atrium().storeCreditentials(id, credits)
            print "[" + id + "] credits stocked"