try:
    from pynput.keyboard import Listener
    import time, keyboard, threading
    from plyer import notification
    from datetime import datetime
except Exception as err:
    print(f'Error: {err}\nPlease install the required libraries using the command: pip install -r requirements.txt')
    exit()

class Logger:
    def get_time():
        return datetime.fromtimestamp(round(BadUSBDetector.get_ms()/1000))
    def log(symbol: str, text: str):
        print(f'{Logger.get_time()} | [{symbol}] {text}')

class BadUSBDetector:
    def __init__(self, max_trigger: int = 10, log: bool = False):
        self.trigger            : int    = 0               # Number of key pressed in a short time
        self.max_trigger        : int    = max_trigger     # Maximum number of key pressed in a short time to block the keyboard
        self.last_time_release  : int    = 0               # Last time a key was released
        self.blocked_start_time : int    = 0               # Time when the keyboard was blocked
        self.maj                : bool   = False           # Maj key status
        self.blocked            : bool   = False           # Keyboard blocked status
        self.keys_hook          : bool   = None            # Keyboard hook
        self.log = log
    
    def new_notification(self, title: str, message: str):
        try:
            notification.notify(
                title=title,
                message=message,
                app_name='BadUSB Detector'
            )
            Logger.log('INFO', f'New notification: {title} - {message}') if self.log else None
        except Exception as err:
            print(f'Error: {err}')
    
    def get_ms():
        return round(time.time()*1000)
    
    def key_callback(self, key: keyboard.KeyboardEvent):
        return # you can use this function to capture the BadUSB payload but it's not working properly as the keyboard layout is different for each user
    
    def block_keyboard(self):
        Logger.log('WARNING', 'BadUSB Detected, blocking keyboard !') if self.log else None
        self.keys_hook = keyboard.hook(self.key_callback, suppress=True)
    
    def unblock_keyboard(self):
        Logger.log('INFO', 'Keyboard unblocked !') if self.log else None
        keyboard.unhook(self.keys_hook)
        threading.Thread(
            target=self.new_notification,
            args=('BadUSB', 'Keyboard unblocked.',)
        ).start()
        
        self.keys_hook = None
        self.blocked = False
        self.trigger = 0
        self.last_time_release = 0
    
    def unblock_keyboard_thread(self):
        while True:
            if self.blocked:
                if BadUSBDetector.get_ms() - self.blocked_start_time > 5000:
                    self.unblock_keyboard()
                    return
                else:
                    time.sleep(1)
    
    def on_release(self, key):
        if not self.blocked:
            if self.last_time_release == 0:
                self.last_time_release = BadUSBDetector.get_ms()
            else:
                current_time = BadUSBDetector.get_ms()
                time_between_two_keys = current_time - self.last_time_release
                if time_between_two_keys <= 30:
                    self.trigger += 1
                elif time_between_two_keys > 100:
                    self.trigger = 0
                
                self.last_time_release = current_time
                
                if self.trigger >= self.max_trigger:
                    threading.Thread(
                        target=self.new_notification,
                        args=('BadUSB Detected', 'Keyboard input blocked !\nPlease wait 5 seconds to be able to use the keyboard again.',)
                    ).start()

                    self.block_keyboard()
                    self.blocked = True
                    self.blocked_start_time = BadUSBDetector.get_ms()
                    threading.Thread(target=self.unblock_keyboard_thread).start()
    
    def start(self):
        Logger.log('INFO', 'BadUSB Detector started !') if self.log else None
        with Listener(on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    detector = BadUSBDetector(log=True)
    detector.start()