class studentclass :
    name = ""
    subject = ""
    contact = ""
    city = ""
    email = ""
    marks = ""
    fees = ""
    dict = {}
    def createFaculty(self,fname,subject,contact,city,email,marks,fees):
        innerdict = {}
        self.name = fname
        self.subject = subject
        self.number = contact
        self.city = city
        self.email = email
        self.score = marks
        self.fees = fees

        innerdict['subject'] = self.subject
        innerdict['contact'] = self.contact
        innerdict['city'] = self.city
        innerdict['email'] = self.email
        innerdict['score'] = self.marks
        innerdict['fees'] = self.fees

        self.dict["fname"] = innerdict
        print(self.dict)


