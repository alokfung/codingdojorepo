from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(a_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        print "Current call queue is: "+str(self.get_queue_size())+" calls."
        for call in self.calls:
            call.display_info()

call1 = Call("Adrian",5626072419,"No clue")
call2 = Call("Bozo",5614624719,"No clue")
call3 = Call("Lonzo",8765074719,"To be annoying")

callcenter = CallCenter()
callcenter.add(call1)
callcenter.add(call2)
callcenter.add(call3)

callcenter.info()