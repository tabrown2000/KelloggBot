import time, sys, threading

class Loading_Animation:
    def __init__(self):
        self.stop = False

    def __del__(self):
        try:
            self.stop = True
            self.animation.join()
        except: pass

    def animated_loading(self, stop):
        chars = "/—\|" 
        i = 0
        while i < 3000: 
            for char in chars:
                sys.stdout.write('\r' + self.start_message + '.'*(45-len(self.start_message)) + char )
                time.sleep(.1)
                sys.stdout.flush()
            if self.stop == True:
                sys.stdout.write('\r' + self.start_message + '.'*(45-len(self.start_message)) + self.stop_message + '\n')
                break
            i += 1
            # if i == 3000: 
            #     self.animation.join() # thread is freed after 5 min if it hangs

    def start_animation(self, start_message):
        self.stop = False
        self.start_message = start_message
        self.animation = threading.Thread(target=self.animated_loading, args =(lambda : self.stop, ))
        self.animation.daemon = True
        self.animation.start()

    def stop_animation(self, stop_message):
        self.stop_message = stop_message
        self.stop = True
        self.animation.join()
