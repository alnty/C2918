class Time:
    def __init__(self):
        super().__init__()
        self.current_time = "1:00AM"


class DND:
    def __init__(self):
        super().__init__()
        self.dnd_mode = "☾"


class Connection:
    def __init__(self):
        super().__init__()
        self.your_connection = "≣"


class WiFi:
    def __init__(self):
        super().__init__()
        self.your_Wi_Fi = "⌔"


class Battery:
    def __init__(self):
        super().__init__()
        self.battery_charge = "⌸"


class App:
    def __init__(self):
        super().__init__()
        self.all_apps = "▢"


class GoBack:
    def __init__(self):
        super().__init__()
        self.go_back = "◀"


class GoToHomeScreen:
    def __init__(self):
        super().__init__()
        self.go_home_screen = "◉"


class OpenRecentTabs:
    def __init__(self):
        super().__init__()
        self.go_recent_tabs = "☷"


class YourDisplay(Time, DND, Connection, WiFi, Battery, App, GoBack, GoToHomeScreen, OpenRecentTabs):
    def print_info(self):
        print(self.current_time + " " + self.dnd_mode + "    " + self.your_connection + " " + self.your_Wi_Fi + " " + self.battery_charge)
        print("   " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps)
        print("     " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps)
        print("   " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps)
        print("")
        print("     " + self.all_apps + "  " + self.all_apps + "  " + self.all_apps)
        print("  " + self.go_back + "     " + self.go_home_screen + "     " + self.go_recent_tabs)


your_phone = YourDisplay()
your_phone.print_info()