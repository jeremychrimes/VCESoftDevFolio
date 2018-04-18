import tkinter
import datetime

class window (tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent) # Run the tkinter initiliser on the class
        self.parent = parent # Define parent as parent
        self.filename = str() # Create a placeholder variable for the program file name
        self.inittialize() # Run the initilisation method for this class
        self.today = datetime.date.today()  # Set the date of today in the application
    def inittialize(self):
        self.c = tkinter.Canvas(self, width=800, height=800, bg="black") # Create a
        self.c.pack()
        self.c.create_text(100, 50, anchor='w',fill="orange", font="Cursive 28 bold underline",text="My Calendar")
        self.newButton = tkinter.Button(self, text="Add New Event").pack()
    def refreshContet(self):
        self.get_events()
        verticalSpace = 100
        for event in self.eventList:
            eventName = event[0]
            eventDate = event[1]
            daysUntil = event[2]
            display = 'It is {0} days until {1}'.format(daysUntil, eventName)
            self.c.create_text(100,verticalSpace, anchor="w", fill='lightblue', font="Arial 28 bold", text=display)
            verticalSpace += 30
    def get_events(self):
        self.eventList = list()
        with open(self.filename) as file:
            for line in file:
                # print(line)
                line = line.rstrip('\n')
                currentEvent = line.split(",")
                eventDate = datetime.datetime.strptime(currentEvent[1], '%d/%m/%y').date()
                currentEvent[1] = eventDate
                currentEvent.append(self.daysBetweenDates(eventDate, self.today))
                self.eventList.append(currentEvent)
                print(self.eventList)
        return self.eventList
    def daysBetweenDates(self,date1, date2):
        timeBetween = str(date1 - date2)
        numberOfDays = timeBetween.split(' ')
        return numberOfDays[0]

#class dateInsertWindow(tkinter.Tk):
  #  def __init__(self, parent):


def main():
    win = window(None)
    win.filename = 'dates.csv'
    win.refreshContet()
    win.mainloop()

if __name__ == "__main__":
    main()

