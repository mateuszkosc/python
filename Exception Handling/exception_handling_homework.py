def exceptionHandling():
    try:
        car = {"make": "bmw", "model": "550i", "year": "2016"}
        print(car["color"])
    except:
        print("Key not found")
        raise Exception()
    finally:
        print("Please try a different key")

exceptionHandling()
