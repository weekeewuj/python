class Student(object):
    def init(self,name,score):
        self.name=name
        self.score=score
    def get_grade(self,n):
        if n==1:
            if self.score >= 90:
                return 'A'
            elif self.score >= 60:
                return 'B'
            else:
                return 'C'
        if n==2:
            if self.score >= 90:
                return 'A'
            elif self.score>=80:
                return 'B'
            else:
                return 'C'

bart=Student('bart',65)
print bart.get_grade(1)
print bart.get_grade(2)
