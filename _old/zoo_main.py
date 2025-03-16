import time, threading

WIDTH = 6
HEIGHT  = 4

baby_found = threading.Event()


def main():
    zoo_map =[]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            zoo_map.append({"point":(i,j), "isThere":False})
    zoo_map[2*WIDTH + 0]["isThere"] = True

    father = threading.Thread(target=searcher, args=(zoo_map[0:8], 1))
    mother = threading.Thread(target=searcher, args=(zoo_map[8:16], 1))
    boy = threading.Thread(target=searcher, args=(zoo_map[16:20], 0.5))
    girl = threading.Thread(target=searcher, args=(zoo_map[20:24], 0.5))

    father.start()
    mother.start()
    boy.start()
    girl.start()

def searcher(zoo_map_slice, speed):
    for slice in zoo_map_slice:
        if baby_found.is_set():
            break;
        if(slice["isThere"] == True):
            print("Found baby!")
            baby_found.set()
        else:
            print("Not Found...")
        time.sleep(speed)

    baby_found.wait()
    print("Going to entrance")

if __name__ == "__main__":
    main()
