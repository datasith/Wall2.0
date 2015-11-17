import multiprocessing, time

def worker1():
    #print 'Worker_1'
    print "WTF"
    i=0
    while 1:
        i+=1
        print 'Worker_'+str(i)
        time.sleep(3)
    return

if __name__ == '__main__':
    jobs = []
    p = multiprocessing.Process(target=worker1)
    jobs.append(p)
    p.start()
