import pathlib
import csv

subject_list = []
start_hour = 8 # school day start at 8.am
next_hour = 9 # next hour is 9.am
school_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
time_slot_list = [] # get list of time slot
subject_per_slot = {}
MAX_HOUR_PER_SUBJECT = 6 # a constant variable
subject_hour_count = {}

def fill_out_subject_list():
    """Ask user subjects and fill in project list"""

    enter_another_subject = True

    while enter_another_subject:
        subject = input('Type another subject : ')
        subject = subject.capitalize()

        if not subject in subject_list:
            subject_list.append(subject)
            subject_hour_count[subject] = MAX_HOUR_PER_SUBJECT
        else:
            print(f'You\'ve already type {subject} in list.')

        question = input('Enter another subject (type "n" to exit)?')

        if question.lower() == 'n':
            enter_another_subject = False


def ask_hour():
    """Ask hour to user"""

    print(f'Subject list : {subject_list}')

    print(f'Planning time : {start_hour}h-{next_hour}h')
    user_answer = input('What\'s subject do you want put here?')

    return user_answer


def fill_in_timetable():
    """Display an hour & ask user which subject he want to put there"""

    global start_hour
    global next_hour

    for day in school_days:
        # Reset start and next hour
        the_hour = {}
        time = 0
        start_hour = 8 # suppose that school start at 8.am
        next_hour = 9

        print('\n------------------------------')
        print(f'{day.capitalize()} timetable')
        print('-------------------------------\n')

        while time < 8: # Suppose we've 08 hours course/day (you can change it)
            hour_format = f'{start_hour}h-{next_hour}h' # format time slot
            
            # represent 8 hours/per day for school
            if time == 4: # if it's a midday (12.am), make a break
                # Add a break in timetable with 'Break time' as inscription
                subject_per_slot[hour_format] = ['Break Time']
                # Add hour format while making sure we avoid duplicate
                if not hour_format in time_slot_list:
                    time_slot_list.append('hour_format')
            else:
                chosen_subject = ask_hour().capitalize()
                print(f'start_hour : {start_hour}')
                print(f'next_hour : {next_hour}')

                # Check that subject chosen by user is in subjects list
                while not chosen_subject in subject_list:
                    print(f'{chosen_subject} is not in subject list.')
                    print('Choose another subject.')
                    chosen_subject = ask_hour().capitalize()

                # Add hour format while making sure we avoid duplicate
                if not hour_format in time_slot_list:
                    time_slot_list.append(hour_format)
                    subject_per_slot[hour_format] = [chosen_subject]
                else:
                    subject_per_slot[hour_format] += [chosen_subject]

                # Check that chosen subject max hours didn't reached
                for subject, max_hour in subject_hour_count.items():
                    if chosen_subject == subject:
                        subject_hour_count[chosen_subject] = max_hour - 1 # remove one hour on subject max hour

            # go to next hour
            start_hour += 1
            next_hour += 1
            time += 1

fill_out_subject_list()
fill_in_timetable()
print(f'Subject per slot : {subject_per_slot}')

timetable_path = pathlib.Path.cwd() / 'timetable.csv'

# write process to save timetable into a csv file
with open(timetable_path, 'w') as timetable_file:
    timetable_writing = csv.writer(timetable_file)

    # Write headers into csv file
    csv_headers = ['Hours']
    csv_headers.extend(school_days)
    timetable_writing.writerow(csv_headers)

    # Write content into csv file
    for time_slot, concerned_subjects in subject_per_slot.items():
        time_line = [time_slot]
        concerned_subjects_list = []
        
        if concerned_subjects == ['Break Time']:
            for x in range(0, len(school_days)):
                concerned_subjects_list.append('Break Time')
        else:
            concerned_subjects_list = concerned_subjects

        final_line = time_line + concerned_subjects_list
        timetable_writing.writerow(final_line)

    print('Your timetable is ready')
