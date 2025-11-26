class Mobile:

    def __init__(self):
        pass

    def callings(self):
        print(f"Invoking calling function")

    def sms(self):
        print(f"Invoking SMS method")

    def games(self):
        print(f"Invoking games")


class Samsung(Mobile):

    def cam(self):
        print(f"Invoking cam method")

    def music(self):
        print(f"Invoking music method")

    def video_calls(self):
        print(f"Invoking video_call method")

samsung=Samsung()
samsung.music()
samsung.cam()
samsung.video_calls()

mobile=Mobile()
mobile.callings()
mobile.sms()
mobile.games()


