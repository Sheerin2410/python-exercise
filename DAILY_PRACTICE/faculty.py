class facultyclass :
    name = ""
    subject = ""
    contact = ""
    city = ""
    email = ""
    dict = {}
    def createFaculty(self,fname,subject,contact,city,email):
        innerdict = {}
        self.name = fname
        self.subject = subject
        self.number = contact
        self.city = city
        self.email = email
        innerdict['subject'] = self.subject
        innerdict['contact'] = self.contact
        innerdict['city'] = self.city
        innerdict['email'] = self.email

        self.dict["fname"] = innerdict
        print(self.dict)




