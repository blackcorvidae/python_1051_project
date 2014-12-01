import datetime

class Bill:
    def __init__(self,bill_number):
        self.bill_number = bill_number
    bill_number = ''
    short_title = ''
    long_title = ''
    printers_number = ''
    text = ''
    #these should all be classes too
    amendments = []
    fiscal_notes = []
    prime_sponsor = Nothing  #Person class
    acts = []
    votes = []
    workflows = []
    #BillHistory class for history
    def save(self):
       #save to mongodb here
   
