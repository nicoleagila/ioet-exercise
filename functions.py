
def split_hour(hour_str):
    hour,minute=hour_str.split(":")
    return(int(hour),int(minute))

def range_hours(time_frame):
    start,end = time_frame.split("-")
    hour_start = split_hour(start)[0]
    hour_end,min_end = split_hour(end)
    if hour_start != hour_end:
        if int(min_end)>0:
            return set(range(hour_start,hour_end+1))
        else:
            return set(range(hour_start,hour_end))
    else:
        return {hour_start}

def file_to_dict(file_name):
    try:
        file = open(file_name,"r")
    except FileNotFoundError:
        return None

    schedules = {}
    for line in file:
        name, schedule = line.strip().split("=")
        days = schedule.split(",")
        days_dict = {}
        for day in days:
            days_dict[day[:2]] = range_hours(day[2:])
        schedules[name] = days_dict
    file.close()

    return schedules

def is_a_match(employee0,employee1,schedules):
    match=0
    data_pivot=schedules.get(employee0)
    data_employee=schedules.get(employee1)
    if data_pivot!=None and data_employee!=None:
        for k,v in data_pivot.items():
            employee_sch = data_employee.get(k)
            if employee_sch!= None:
                if len(employee_sch&v)>0:
                    match+=1
    return match