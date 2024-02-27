
class Logger():
    def log(self, message: str):
        pass

class LoggerLibrary(Logger):
    def log(self, message: str) -> None:
        print(message)

class Loguru(Logger):
    def log(self, message: str) -> None:
        print(message)

class GoogleAuth(Logger):
    def log(self, message: str) -> None:
        print(message)

class Log():
    def __init__(self, log: Logger) -> None:
        self.logger = log
    
    def log(self, message: str) -> None:
        self.logger.log(message)

def main():
    test1 = Log(LoggerLibrary())
    test2 = Log(Loguru())
    test3 = Log(GoogleAuth())

    test1.log("Test 1")
    test2.log("Test 2")
    test3.log("Test 3")

main()