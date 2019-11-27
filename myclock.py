class Clock(object):
    def __init__(self, hour=0, minite=0, second=0):
        self.__hour = hour
        self.__minite = minite
        self.__second = second

    def run(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minite += 1
            if self.__minite == 60:
                self.__minite = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def show(self):
        return '{}:{}:{}'.format(self.__hour, self.__minite, self.__second)

