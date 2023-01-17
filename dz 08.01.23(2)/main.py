class FuttbolError(Exception):
    def __str__(self):
        return f'Без цих людей не може роспочатися гра в футбол'
def check_people(amout_of_people, limit_value):
    if amout_of_people > limit_value:
        return 'Людей достатньо'
    else:
        raise FuttbolError(amout_of_people)
people = 40
check_people(people, 200)