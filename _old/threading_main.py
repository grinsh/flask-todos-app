import time, threading

airplain_is_taking_off = threading.Event()
runway_is_empty = threading.Event()
runway_is_empty.set()   #תפעיל את האירוע
airplain_is_landing = threading.Event()
# airplain_is_taking_off.set()   #האירוע פועל
# airplain_is_taking_off.clear()   #האירוע מבוטל
# airplain_is_taking_off.is_set()   #בודקת האם האירוע פועל
# airplain_is_taking_off.wait()   #חכה עד שהאירוע יופעל



def main():
    ap1 = threading.Thread(target=airplain, kwargs={"id":1, "duration":5})
    ap2 = threading.Thread(target=airplain, kwargs={"id":2, "duration":3})
    ap3 = threading.Thread(target=airplain, kwargs={"id":3, "duration":3})
    ap4 = threading.Thread(target=airplain, kwargs={"id":4, "duration":3})

    ap1.start()
    ap2.start()
    ap3.start()
    ap4.start()

def airplain(id, duration):
    print(f"Airplain {id} is ready to take off")

    while airplain_is_taking_off.is_set():        #  אם יש מטוס שממריא עכשיו
        print(f"Airplain {id} is waiting..... (take of).   Time: {time.time()}")
        time.sleep(1)
    else:
        airplain_is_taking_off.set() #עכשיו מטוס מתחיל המראה
        print(f"Airplain {id} is taking off.  Time: {time.time()}")
        time.sleep(3)
        airplain_is_taking_off.clear()  # עכשיו המטוס סיים את ההמראה

    print(f"Airplain {id} is flying")
    time.sleep(duration)
    print(f"Airplain {id} is ready to land")


    while airplain_is_landing.is_set():
        print(f"Airplain {id} is waiting..... (land).  Time: {time.time()}")
        time.sleep(1)
    else:
        airplain_is_landing.set()
        print(f"Airplain {id} is landing.  Time: {time.time().real}")
        time.sleep(3)
        airplain_is_landing.clear()

    print(f"Airplain {id} landed successfully")


if __name__ == "__main__":
    main()
