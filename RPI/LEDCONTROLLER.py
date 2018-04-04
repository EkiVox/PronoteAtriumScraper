import pickle

class LedController:
    def getCourses(self):
        try:
            coursesfile = open('last-courses.conf', 'r')
            courseslist = pickle.load(coursesfile)
            return courseslist
        except (OSError, IOError, EOFError):
            print "veuillez creer un fichier last-courses.conf ou alors il est vide"
