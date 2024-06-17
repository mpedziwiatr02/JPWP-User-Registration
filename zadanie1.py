#import asyncio
import random
import time

# funkcja definiujaca partie szachow
def mecz(value):
    mecz_start = time.time()

    for i in range(3):
        print(f'>wykonuje {i+1} ruch w meczu {value+1} ')
        # losowy ( od 0 do 1s ) czas na ruch przeciwnika
        rand = random.random()
        time.sleep(rand)
        print(f'>przeciwnik wykonal {i+1} ruch w meczu {value+1} ')

    mecz_end = time.time()
    print(f'>czas meczu {value+1} wyniosl {mecz_end - mecz_start} ')


# funkcja main
def main():
    # info o rozpoczeciu main
    print('main starting')
    # utworzenie meczy
    mecze = [mecz(i) for i in range(4)]
    # uruchomienie wszystkich meczy
    for i in mecze:
        mecz
    # info o zakonczeniu main
    print('main done')


#pomiar czasu calego programu
start = time.time()
# start programu
main()
#koniec pomiaru czasu
end = time.time()
print(f'Time: {end-start:.2f} sec')