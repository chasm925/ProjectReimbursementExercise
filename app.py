import datetime
from constant import *


def calc_rate(is_travel_day, city_type):
    """
    calculates rate based on city type and if travel day
    """
    if (city_type == LOW_COST_CITY_TYPE and is_travel_day):
        return LOW_COST_CITY_TRAVEL_RATE
    if (city_type == LOW_COST_CITY_TYPE and not is_travel_day):
        return LOW_COST_CITY_FULL_RATE
    if (city_type == HIGH_COST_CITY_TYPE and is_travel_day):
        return HIGH_COST_CITY_TRAVEL_RATE
    if (city_type == HIGH_COST_CITY_TYPE and not is_travel_day):
        return HIGH_COST_CITY_FULL_RATE

def calc_reimbursement_on_day(projects, is_traveling):
    """
    calculates reimbursement rate for set of projects on a date
    prefers high cost city rate if it exists in set
    """
    if not any(projects):
        return 0

    is_high_cost = any([p for p in projects if p.city_type == HIGH_COST_CITY_TYPE])

    if is_high_cost:
        return calc_rate(is_traveling, HIGH_COST_CITY_TYPE)
    return calc_rate(is_traveling, LOW_COST_CITY_TYPE)

def calc_reimbursement(project_set):
    """
    calculates total reimbursment for set of projects
    """
    reimbursement = 0
    is_travel_day = True

    # get the min start date and max end date across all projects
    min_date = min(p.start_date for p in project_set)
    max_date = max(p.end_date for p in project_set)

    # iterate over all dates from min to max
    current_date = min_date
    while current_date <= max_date:
        next_date = current_date + datetime.timedelta(days=1)

        # query projects active today and on next day
        projects_on_date = [p for p in project_set if p.is_active(current_date)]
        projects_on_next_date = [p for p in project_set if p.is_active(next_date)]

        # if there are no projects on the next day, this must be a travel day
        # since it implies there is a gap or it's the final day in a sequence
        if not any(projects_on_next_date):
            is_travel_day = True

        # add to total reimbursement from this day
        reimbursement += calc_reimbursement_on_day(projects_on_date, is_travel_day)

        # set travel state for next iteration
        # if this is a gap day, next day will always be a travel day
        is_travel_day = not any(projects_on_date)

        current_date = next_date

    return reimbursement
