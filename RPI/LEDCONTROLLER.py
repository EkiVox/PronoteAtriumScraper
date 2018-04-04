import pickle
import urllib

class LedController:
    def downloadCourses(self, ip):
        urllib.urlretrieve ("http://" + ip + ":8000/last-courses.conf", "last-courses.conf")
    def getCourses(self):
        try:
            coursesfile = open('last-courses.conf', 'r')
            courseslist = pickle.load(coursesfile)
            return courseslist
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier last-courses.conf ou alors il est vide"
