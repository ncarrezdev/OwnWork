from threading import Thread as Th
from threading import Event
from time import sleep

from Enums      import E_THREAD_STATE
from Exceptions import Exceptions

class ThreadException(Exceptions):pass

class Thread(Th):
    __quit  = Event()
    __start = Event()
    __loop  = Event()
    __stop  = Event()
    __idle  = Event()
    def __del__(self):
        self.quit()
        Th.join(self)
        
    def __clear_state__(self):
        self.__quit.clear()
        self.__start.clear()
        self.__loop.clear()
        self.__stop.clear()
        self.__idle.clear()

    def __set_state__(self, new_state):
        self.__clear_state__()
        if(new_state == E_THREAD_STATE.QUIT):
            self.__quit.set()
        if(new_state == E_THREAD_STATE.START):
            self.__start.set()
        if(new_state == E_THREAD_STATE.LOOP):
            self.__loop.set()
        if(new_state == E_THREAD_STATE.STOP):
            self.__stop.set()
        if(new_state == E_THREAD_STATE.IDLE):
            self.__idle.set()

            
    def __init__(
        self, 
        do_repeat = True, 
        repeat_time = 0, 
        idle_time = 0.5
        ):
        Th.__init__(self)
        self.__do_repeat      = do_repeat
        self.__repeat_time    = repeat_time
        self.__idle_time      = idle_time
        self.__curr_iteration = 0
        self.__curr_state     = ''

        self.__set_state__(E_THREAD_STATE.IDLE)
        Th.start(self)

    def run(self):
        while(not self.__quit.is_set()):
            if(self.__idle.is_set()):
                self.idle()  
            elif(self.__start.is_set()):
                self.before()    
                self.__curr_iteration = 0
                self.__set_state__(E_THREAD_STATE.LOOP)
            elif(self.__loop.is_set()):
                self.loop()
                self.__curr_iteration += 1 
                if(not self.__do_repeat):
                    self.__set_state__(E_THREAD_STATE.STOP)
                elif(
                    self.__repeat_time != 0 and 
                    self.__curr_iteration <= self.__repeat_time
                    ):
                    self.__set_state__(E_THREAD_STATE.STOP)
            elif(self.__stop.is_set()):
                self.after()
                self.__set_state__(E_THREAD_STATE.IDLE) 
        
    #VIRTUAL FUNCTIONS
    def before(self):
        pass
        
    def loop(self):
        raise ThreadException.NotImplementedException('loop')
        pass
        
    def after(self):
        pass
    
    def idle(self):
        sleep(self.__idle_time)
        pass

    #USER SIDE FUNCTIONS
    def get_curr_state(self):
        return self.__curr_state
    
    def get_curr_iteration(self):
        return self.__curr_iteration

    def quit(self):
        self.__set_state__(E_THREAD_STATE.QUIT)

    def start(self):
        self.__set_state__(E_THREAD_STATE.START)

    def stop(self):
        self.__set_state__(E_THREAD_STATE.STOP)