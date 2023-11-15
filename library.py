def can_drive_car(age: int) -> bool:
    if age < 1:
        raise ValueError("нема нікого молодше 1 року та старше 130 років")
    if age > 130:
        raise ValueError("нема нікого молодше 1 року та старше 130 років")
    print(f"{age+50=}")
    # if age > 18:
    #     return True
    # return False

    # return True if age > 18 else False
    return age > 18
