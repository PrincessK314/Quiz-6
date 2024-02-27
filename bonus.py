
#S: Different features are within different classes including the User, Activity, ActivityMoniter, DataStorage, and Display classes
#O: ActivityMoniter notifys the DataStorage whenever new data is added. This allows new activities to be added as subclasses of Activity without changing any code in Activity, ActivityMonitor, or DataStorage and its subclasses.
#L: The Activity class and its subclasses are substitutable. The activities are stored within an array of the Activity class, the subclasses are placed within that array.
#I: The data collection and display are handled with seperate interfaces. The display is handled by the Display class. The data collection is handled by ActivityMoniter and DataStorage.
#D: The DataStorage and Display classes have subclasses which can implement different types od databases or diaplay methods by adding a new subclass instead of altering the existing classes.

class Activity():
    def __init__(self, duration: int, cal: int) -> None:
        self.duration = duration
        self.calories = cal

    def add(self, duration: int, cal: int) -> None:
        self.duration += duration
        self.calories += cal

class Steps(Activity):
    def __init__(self, duration: int, cal: int) -> None:
        self.name = "Steps"
        super().__init__(duration, cal)

class Swimming(Activity):
    def __init__(self, duration: int, cal: int) -> None:
        self.name = "Swimming"
        super().__init__(duration, cal)

class DataStorage():
    def __init__(self) -> None:
        self.activities = []
    
    def addActivity(self, act: Activity) -> None:
        pass
    
    def addData(self, curAct: Activity, newData: Activity) -> None:
        pass

    def totalInfo(self):
        pass

class DatabaseType1(DataStorage):
    def addActivity(self, act: Activity) -> None:
        self.activities.append(act)
    
    def addData(self, curAct: Activity, newData: Activity) -> None:
        curAct.add(newData.duration, newData.calories)

    def totalInfo(self) -> tuple[int, int]:
        dur = 0
        cal = 0
        for act in self.activities:
            dur += act.duration
            cal += act.calories
        return dur, cal

class DatabaseType2(DataStorage):
    def addActivity(self, act: Activity) -> None:
        self.activities.append(act)
    
    def addData(self, curAct: Activity, newData: Activity) -> None:
        curAct.add(newData.duration, newData.calories)

    def totalInfo(self) -> tuple[int, int]:
        dur = 0
        cal = 0
        for act in self.activities:
            dur += act.duraction
            cal += act.calories
        return dur, cal

class ActivityMonitor():    
    def addData(self, act: Activity, data: DataStorage) -> None:
        a = [active for active in data.activities if active.name == act.name]
        if len(a) != 0:
            data.addData(a[0], act)
        else:
            data.addActivity(act)

class Display():
    def displayAll(self, data: DataStorage) -> None:
        pass
    
    def displayTotal(self, data: DataStorage) -> None:
        pass
    
class DisplayType1(Display):
    def displayAll(self, data: DataStorage) -> None:
        for act in data.activities:
            print(act.name)
            print("--------------------")
            print("Duration: " + str(act.duration) + " minutes")
            print("Calories Burned: " + str(act.calories) + " calories")
            print()
    
    def displayTotal(self, data: DataStorage) -> None:
        info = data.totalInfo()
        print("Total Duration: " + str(info[0]) + " minutes")
        print("Total Calories Burned: " + str(info[1]) + " calories")
        print()

class DisplayType2(Display):
    def displayAll(self, data: DataStorage) -> None:
        for act in data.activities:
            print(act.name)
            print("--------------------")
            print("Duration: " + str(act.duration) + " minutes")
            print("Calories Burned: " + str(act.calories) + " calories")
            print()
    
    def displayTotal(self, data: DataStorage) -> None:
        info = data.totalInfo()
        print("Total Duration: " + str(info[0]) + " minutes")
        print("Total Calories Burned: " + str(info[1]) + " calories")
        print()

class User():
    def __init__(self, data: DataStorage, dis: Display) -> None:
        self.actMonitor = ActivityMonitor()
        self.data = data
        self.display = dis
    
    def addInfo(self, act: Activity) -> None:
        self.actMonitor.addData(act, self.data)
    
    def displayInfo(self) -> None:
        self.display.displayAll(self.data)
    
    def displayTotal(self) -> None:
        self.display.displayTotal(self.data)

def main():
    user = User(DatabaseType1(), DisplayType1())

    user.addInfo(Steps(30, 250))
    user.displayInfo()

    user.addInfo(Swimming(120, 440))
    user.addInfo(Steps(60, 470))

    print("\n")
    user.displayTotal()
    print("\n")
    user.displayInfo()

main()