def get_error_numbers(position, error_rating):
    error_numbers = ''
    if position == 1:
        error_numbers = errors_p(error_rating)
    elif position == 2:
        error_numbers = errors_c(error_rating)
    elif position == 3:
        error_numbers = errors_1b(error_rating)
    elif position == 4:
        error_numbers = errors_2b(error_rating)
    elif position == 5:
        error_numbers = errors_3b(error_rating)
    elif position == 6:
        error_numbers = errors_ss(error_rating)
    elif position == 7:
        error_numbers = errors_lf(error_rating)
    elif position == 8:
        error_numbers = errors_cf(error_rating)
    elif position == 9:
        error_numbers = errors_rf(error_rating)
    return error_numbers


def errors_p(error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 4:
        error_numbers = '14/18'
    elif error_rating == 6:
        error_numbers = '3,13/18'
    elif error_rating == 7:
        error_numbers = '3,12/18'
    elif error_rating == 8:
        error_numbers = '6,15-17/18'
    elif error_rating == 10:
        error_numbers = '11,15/3,18'
    elif error_rating == 11:
        error_numbers = '12,15,16/3,18'
    elif error_rating == 13:
        error_numbers = '11,13/17'
    elif error_rating == 14:
        error_numbers = '7,13,14/17'
    elif error_rating == 15:
        error_numbers = '4,11,12/17'
    elif error_rating == 16:
        error_numbers = '4,9,12,16/17'
    elif error_rating == 17:
        error_numbers = '3,6,11,12/17'
    elif error_rating == 18:
        error_numbers = '11,12,14/17'
    elif error_rating == 19:
        error_numbers = '6,9,12,15/17,18'
    elif error_rating == 20:
        error_numbers = '6,10,11,15/17,18'
    elif error_rating == 21:
        error_numbers = '7,11,13,14/17,18'
    elif error_rating == 22:
        error_numbers = '8,12-14/17,18'
    elif error_rating == 23:
        error_numbers = '10-12,16/17,18'
    elif error_rating == 24:
        error_numbers = '10-12,15/17,18'
    elif error_rating == 26:
        error_numbers = '9,12-15/3,17,18'
    elif error_rating == 27:
        error_numbers = '10-13/3,17,18'
    elif error_rating == 28:
        error_numbers = '9-12/3,17,18'
    elif error_rating == 30:
        error_numbers = '3,10-13,15/16'
    elif error_rating == 31:
        error_numbers = '10-14/16'
    elif error_rating == 33:
        error_numbers = '3,8,10-13/16'
    elif error_rating == 34:
        error_numbers = '9-13/16,18'
    elif error_rating == 35:
        error_numbers = '9-12,14,15/16,18'
    elif error_rating == 36:
        error_numbers = '3,5,6,7,9-12/16,18'
    elif error_rating == 38:
        error_numbers = '6,8,10-13,15/16,18'
    elif error_rating == 39:
        error_numbers = '6-10,12,13/3,16,18'
    elif error_rating == 40:
        error_numbers = '4,6,9-13,15/3,16,18'
    elif error_rating == 42:
        error_numbers = '7,9-14/3,16,18'
    elif error_rating == 43:
        error_numbers = '6-10,12-14/3,16,18'
    elif error_rating == 44:
        error_numbers = '3,7-13/16,17'
    elif error_rating == 46:
        error_numbers = '6,8-13,15/16-18'
    elif error_rating == 47:
        error_numbers = '7-13,15/16-18'
    elif error_rating == 48:
        error_numbers = '7-14/16-18'
    elif error_rating == 50:
        error_numbers = '7-14/15,17'
    elif error_rating == 51:
        error_numbers = '7-14/15,16'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_c (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 1:
        error_numbers = '17/-'
    elif error_rating == 2:
        error_numbers = '3,17,18/-'
    elif error_rating == 3:
        error_numbers = '3,16,18/-'
    elif error_rating == 4:
        error_numbers = '16,17/18'
    elif error_rating == 5:
        error_numbers = '4,16,17/18'
    elif error_rating == 6:
        error_numbers = '14/18'
    elif error_rating == 7:
        error_numbers = '3,15,16/18'
    elif error_rating == 8:
        error_numbers = '6,15/18'
    elif error_rating == 9:
        error_numbers = '3,13/18'
    elif error_rating == 10:
        error_numbers = '12/18'
    elif error_rating == 11:
        error_numbers = '3,11/18'
    elif error_rating == 12:
        error_numbers = '6,15-17/3,18'
    elif error_rating == 13:
        error_numbers = '4,6,15-17/3,18'
    elif error_rating == 14:
        error_numbers = '12,16,17/3,18'
    elif error_rating == 15:
        error_numbers = '11,15/3,18'
    elif error_rating == 16:
        error_numbers = '7,14,16,17/3,18'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_1b (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 1:
        error_numbers = '17,18/-'
    elif error_rating == 2:
        error_numbers = '3,16,18/-'
    elif error_rating == 3:
        error_numbers = '3,15/18'
    elif error_rating == 4:
        error_numbers = '14/18'
    elif error_rating == 5:
        error_numbers = '14,17/18'
    elif error_rating == 6:
        error_numbers = '3,13/18'
    elif error_rating == 7:
        error_numbers = '3,9/18'
    elif error_rating == 8:
        error_numbers = '6,15-17/3,18'
    elif error_rating == 9:
        error_numbers = '7,14,17/3,18'
    elif error_rating == 10:
        error_numbers = '11,15/3,18'
    elif error_rating == 11:
        error_numbers = '6,8,15/3,18'
    elif error_rating == 12:
        error_numbers = '6,9,15/3,18'
    elif error_rating == 13:
        error_numbers = '11,13/17'
    elif error_rating == 14:
        error_numbers = '3,9,12/17'
    elif error_rating == 15:
        error_numbers = '7,12,14/17'
    elif error_rating == 16:
        error_numbers = '3,11,12,16/17'
    elif error_rating == 17:
        error_numbers = '3,6,11,12/17'
    elif error_rating == 18:
        error_numbers = '11,12,14/17'
    elif error_rating == 19:
        error_numbers = '10,11,15,16/17,18'
    elif error_rating == 20:
        error_numbers = '6,10,11,15/17,18'
    elif error_rating == 21:
        error_numbers = '3,9,10,12/17,18'
    elif error_rating == 22:
        error_numbers = '7,11,12,14/17,18'
    elif error_rating == 23:
        error_numbers = '10-12,16/17,18'
    elif error_rating == 24:
        error_numbers = '11-14/3,17,18'
    elif error_rating == 25:
        error_numbers = '9,11,12,14/3,17,18'
    elif error_rating == 26:
        error_numbers = '9,12-15/3,17,18'
    elif error_rating == 27:
        error_numbers = '7,8,11,13,14/3,17,18'
    elif error_rating == 28:
        error_numbers = '7,11-14/3,17,18'
    elif error_rating == 29:
        error_numbers = '9-12,17/16'
    elif error_rating == 30:
        error_numbers = '10-13,15,18/16'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_2b (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 4:
        error_numbers = '3,17/18'
    elif error_rating == 5:
        error_numbers = '16/18'
    elif error_rating == 6:
        error_numbers = '3,16/18'
    elif error_rating == 8:
        error_numbers = '16,17/18'
    elif error_rating == 10:
        error_numbers = '4,16,17/18'
    elif error_rating == 11:
        error_numbers = '15,17/18'
    elif error_rating == 12:
        error_numbers = '15,17/3,18'
    elif error_rating == 13:
        error_numbers = '14/3,18'
    elif error_rating == 14:
        error_numbers = '15,16/3,18'
    elif error_rating == 15:
        error_numbers = '14,17/3,18'
    elif error_rating == 16:
        error_numbers = '15-17/3,18'
    elif error_rating == 17:
        error_numbers = '6,15/3,18'
    elif error_rating == 18:
        error_numbers = '13/3,18'
    elif error_rating == 19:
        error_numbers = '6,15,17/3,18'
    elif error_rating == 20:
        error_numbers = '3,13,18/17'
    elif error_rating == 21:
        error_numbers = '4,13/17'
    elif error_rating == 22:
        error_numbers = '12,18/17'
    elif error_rating == 23:
        error_numbers = '11/17'
    elif error_rating == 24:
        error_numbers = '11,18/17'
    elif error_rating == 25:
        error_numbers = '3,11,18/17'
    elif error_rating == 26:
        error_numbers = '13,15/17'
    elif error_rating == 27:
        error_numbers = '13,15,18/17'
    elif error_rating == 28:
        error_numbers = '3,13,15/17,18'
    elif error_rating == 29:
        error_numbers = '3,11,16/17,18'
    elif error_rating == 30:
        error_numbers = '12,15/17,18'
    elif error_rating == 32:
        error_numbers = '11,15/17,18'
    elif error_rating == 34:
        error_numbers = '12,14/17,18'
    elif error_rating == 37:
        error_numbers = '11,15,16/3,17,18'
    elif error_rating == 39:
        error_numbers = '12,13/3,17,18'
    elif error_rating == 41:
        error_numbers = '11,13/3,17,18'
    elif error_rating == 44:
        error_numbers = '9,12,18/16'
    elif error_rating == 47:
        error_numbers = '7,12,14/16'
    elif error_rating == 50:
        error_numbers = '11,13,15,18/16'
    elif error_rating == 53:
        error_numbers = '11,12,15/16,18'
    elif error_rating == 56:
        error_numbers = '6,12,13,15/16,18'
    elif error_rating == 59:
        error_numbers = '6,11,13,15/3,16,18'
    elif error_rating == 62:
        error_numbers = '6,11,12,15/3,16,18'
    elif error_rating == 65:
        error_numbers = '7,12-14/3,16,18'
    elif error_rating == 68:
        error_numbers = '10-12/16,17'
    elif error_rating == 71:
        error_numbers = '11-13,15/16,17'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_3b (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 5:
        error_numbers = '15/17'
    elif error_rating == 6:
        error_numbers = '4,15/17'
    elif error_rating == 8:
        error_numbers = '3,15,16/17,18'
    elif error_rating == 10:
        error_numbers = '13/3,17,18'
    elif error_rating == 11:
        error_numbers = '6,15,17/16'
    elif error_rating == 12:
        error_numbers = '12/16'
    elif error_rating == 13:
        error_numbers = '11/16,18'
    elif error_rating == 14:
        error_numbers = '3,4,14,15/16,18'
    elif error_rating == 15:
        error_numbers = '13,15/3,17,18'
    elif error_rating == 16:
        error_numbers = '4,7,14/3,16,18'
    elif error_rating == 17:
        error_numbers = '12,15/16,17'
    elif error_rating == 18:
        error_numbers = '3,11,15/16,17'
    elif error_rating == 19:
        error_numbers = '7,14,16,17/15'
    elif error_rating == 20:
        error_numbers = '11,14/15'
    elif error_rating == 21:
        error_numbers = '6,11,16/15,18'
    elif error_rating == 22:
        error_numbers = '12,14,16/15,18'
    elif error_rating == 23:
        error_numbers = '11,13/3,15,18'
    elif error_rating == 24:
        error_numbers = '9,12/15,17,18'
    elif error_rating == 25:
        error_numbers = '6,8,13/15,17'
    elif error_rating == 26:
        error_numbers = '10,11/15,17'
    elif error_rating == 27:
        error_numbers = '9,12,16/15,17,18'
    elif error_rating == 28:
        error_numbers = '11,13,15/14'
    elif error_rating == 29:
        error_numbers = '9,12,15/14'
    elif error_rating == 30:
        error_numbers = '6,8,13,15/14,18'
    elif error_rating == 31:
        error_numbers = '10,11,15/14,18'
    elif error_rating == 32:
        error_numbers = '11,13,14,17/15,16,18'
    elif error_rating == 33:
        error_numbers = '8,11,13/15,16,18'
    elif error_rating == 34:
        error_numbers = '6,9,12,15/14,17'
    elif error_rating == 35:
        error_numbers = '11-13/14,17'
    elif error_rating == 37:
        error_numbers = '9,11,12/15-17'
    elif error_rating == 39:
        error_numbers = '7,9,12,14,18/6,15'
    elif error_rating == 41:
        error_numbers = '10-12,16/13'
    elif error_rating == 44:
        error_numbers = '4,11-14/6,15,17'
    elif error_rating == 47:
        error_numbers = '8,9,11,12/13,17'
    elif error_rating == 50:
        error_numbers = '9-12/14,15,18'
    elif error_rating == 53:
        error_numbers = '6,8-11/13,16'
    elif error_rating == 56:
        error_numbers = '8-10,12,14,17/3,11,18'
    elif error_rating == 59:
        error_numbers = '4,7,9-12/13,15'
    elif error_rating == 62:
        error_numbers = '7-11,14/12,16,18'
    elif error_rating == 65:
        error_numbers = '7-10,12,13/11,16,18'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_ss (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-'
    elif error_rating == 1:
        error_numbers = '18/-'
    elif error_rating == 2:
        error_numbers = '3,18/-'
    elif error_rating == 3:
        error_numbers = '17/-'
    elif error_rating == 4:
        error_numbers = '17/18'
    elif error_rating == 5:
        error_numbers = '3,17/18'
    elif error_rating == 7:
        error_numbers = '3,16/18'
    elif error_rating == 8:
        error_numbers = '16,17/18'
    elif error_rating == 10:
        error_numbers = '16,17/3,18'
    elif error_rating == 12:
        error_numbers = '15/3,18'
    elif error_rating == 14:
        error_numbers = '4,15/17'
    elif error_rating == 16:
        error_numbers = '14/17'
    elif error_rating == 17:
        error_numbers = '15,16/17'
    elif error_rating == 18:
        error_numbers = '15,16,18/17'
    elif error_rating == 19:
        error_numbers = '4,14/17'
    elif error_rating == 20:
        error_numbers = '4,15,16/17'
    elif error_rating == 21:
        error_numbers = '6,15/17'
    elif error_rating == 22:
        error_numbers = '6,15/17,18'
    elif error_rating == 23:
        error_numbers = '3,13/17,18'
    elif error_rating == 24:
        error_numbers = '4,6,15/17,18'
    elif error_rating == 25:
        error_numbers = '4,13/17,18'
    elif error_rating == 26:
        error_numbers = '12/17,18'
    elif error_rating == 27:
        error_numbers = '3,12/17,18'
    elif error_rating == 28:
        error_numbers = '6,5,16/3,17,18'
    elif error_rating == 29:
        error_numbers = '11/3,17,18'
    elif error_rating == 30:
        error_numbers = '4,12/3,17,18'
    elif error_rating == 31:
        error_numbers = '4,6,15,16/3,17,18'
    elif error_rating == 32:
        error_numbers = '13,15/3,17,18'
    elif error_rating == 33:
        error_numbers = '13,15/16'
    elif error_rating == 34:
        error_numbers = '13,15,18/16'
    elif error_rating == 36:
        error_numbers = '13,15,17/16'
    elif error_rating == 38:
        error_numbers = '13,14/16'
    elif error_rating == 40:
        error_numbers = '11,15/16,18'
    elif error_rating == 42:
        error_numbers = '12,14/16,18'
    elif error_rating == 44:
        error_numbers = '8,12/16,18'
    elif error_rating == 48:
        error_numbers = '6,12,15/3,16,18'
    elif error_rating == 52:
        error_numbers = '11,13,18/16,17'
    elif error_rating == 56:
        error_numbers = '11,12,18/16,17'
    elif error_rating == 60:
        error_numbers = '7,11,14/15'
    elif error_rating == 64:
        error_numbers = '6,9,12/15,18'
    elif error_rating == 68:
        error_numbers = '9,12,14/15,18'
    elif error_rating == 72:
        error_numbers = '6,11,13,15/4,16,17'
    elif error_rating == 76:
        error_numbers = '9,12,13/15,17'
    elif error_rating == 80:
        error_numbers = '4,11-13/15,17'
    elif error_rating == 84:
        error_numbers = '10-12/3,15,17'
    elif error_rating == 88:
        error_numbers = '9,11,12,16/14'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_lf (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-/-'
    elif error_rating == 1:
        error_numbers = '3/17/-'
    elif error_rating == 2:
        error_numbers = '3,18/16/-'
    elif error_rating == 3:
        error_numbers = '3,18/15/-'
    elif error_rating == 4:
        error_numbers = '4/3,15/18'
    elif error_rating == 5:
        error_numbers = '4/14/18'
    elif error_rating == 6:
        error_numbers = '3,4/14,17/18'
    elif error_rating == 7:
        error_numbers = '16/6,15/18'
    elif error_rating == 8:
        error_numbers = '16/6,15,17/3,18'
    elif error_rating == 9:
        error_numbers = '6/11/3,18'
    elif error_rating == 10:
        error_numbers = '4,16/14,15,17/3,18'
    elif error_rating == 11:
        error_numbers = '16/13,15/3,18'
    elif error_rating == 12:
        error_numbers = '4,16/13,14/3,18'
    elif error_rating == 13:
        error_numbers = '6/4,12,15/17'
    elif error_rating == 14:
        error_numbers = '3,6/12,14/17'
    elif error_rating == 15:
        error_numbers = '3,6,18/4,12,14/17'
    elif error_rating == 16:
        error_numbers = '4,6/12,13/17'
    elif error_rating == 17:
        error_numbers = '4,6/9,12/17'
    elif error_rating == 18:
        error_numbers = '3,4,6/11,12,18/17'
    elif error_rating == 19:
        error_numbers = '7/3,10,11/17,18'
    elif error_rating == 20:
        error_numbers = '3,7/11,13,15/17,18'
    elif error_rating == 21:
        error_numbers = '3,7/11,12,15/17,18'
    elif error_rating == 22:
        error_numbers = '3,6,16/9,12,14/17,18'
    elif error_rating == 23:
        error_numbers = '4,7/11,12,14/17,18'
    elif error_rating == 24:
        error_numbers = '4,6,16/8,11,13/3,17,18'
    elif error_rating == 25:
        error_numbers = '4,6,16/11-13/3,17,18'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_cf (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-/-'
    elif error_rating == 1:
        error_numbers = '-/17/-'
    elif error_rating == 2:
        error_numbers = '3/17,18/-'
    elif error_rating == 3:
        error_numbers = '3,18/16/-'
    elif error_rating == 4:
        error_numbers = '4/16/18'
    elif error_rating == 5:
        error_numbers = '4/16,17/18'
    elif error_rating == 6:
        error_numbers = '4/3,15/18'
    elif error_rating == 7:
        error_numbers = '3,4/15,17/18'
    elif error_rating == 8:
        error_numbers = '3,4/15,16/18'
    elif error_rating == 9:
        error_numbers = '3,4/14,17/18'
    elif error_rating == 10:
        error_numbers = '16/3,4,14/18'
    elif error_rating == 11:
        error_numbers = '16/3,13/18'
    elif error_rating == 12:
        error_numbers = '16/4,6,15/3,18'
    elif error_rating == 13:
        error_numbers = '16/4,6,15,17/3,18'
    elif error_rating == 14:
        error_numbers = '16/12,17/3,18'
    elif error_rating == 15:
        error_numbers = '4,16/12,17/3,18'
    elif error_rating == 16:
        error_numbers = '4,16/7,14/3,18'
    elif error_rating == 17:
        error_numbers = '4,16/7,14,17/3,18'
    elif error_rating == 18:
        error_numbers = '4,16/13,14/3,18'
    elif error_rating == 19:
        error_numbers = '6/11,15/3,18'
    elif error_rating == 20:
        error_numbers = '6/4,13,14/17'
    elif error_rating == 21:
        error_numbers = '3,6/12,14/17'
    elif error_rating == 22:
        error_numbers = '3,6/4,12,14/17'
    elif error_rating == 23:
        error_numbers = '3,6,18/4,13,14,16/17'
    elif error_rating == 24:
        error_numbers = '4,6/12,13/17'
    elif error_rating == 25:
        error_numbers = '4,6/11,13,18/17'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def errors_rf (error_rating):
    error_numbers = ''
    if error_rating == 0:
        error_numbers = '-/-/-'
    elif error_rating == 1:
        error_numbers = '3/17/-'
    elif error_rating == 2:
        error_numbers = '3,18/16/-'
    elif error_rating == 3:
        error_numbers = '3,18/15/-'
    elif error_rating == 4:
        error_numbers = '4/3,15/18'
    elif error_rating == 5:
        error_numbers = '4/14/18'
    elif error_rating == 6:
        error_numbers = '3,4/14,17/18'
    elif error_rating == 7:
        error_numbers = '16/6,15/18'
    elif error_rating == 8:
        error_numbers = '16/6,15,17/3,18'
    elif error_rating == 9:
        error_numbers = '6/11/3,18'
    elif error_rating == 10:
        error_numbers = '4,16/14,15,17/3,18'
    elif error_rating == 11:
        error_numbers = '16/13,15/3,18'
    elif error_rating == 12:
        error_numbers = '4,16/13,14/3,18'
    elif error_rating == 13:
        error_numbers = '6/4,12,15/17'
    elif error_rating == 14:
        error_numbers = '3,6/12,14/17'
    elif error_rating == 15:
        error_numbers = '3,6,18/4,12,14/17'
    elif error_rating == 16:
        error_numbers = '4,6/12,13/17'
    elif error_rating == 17:
        error_numbers = '4,6/9,12/17'
    elif error_rating == 18:
        error_numbers = '3,4,6/11,12,18/17'
    elif error_rating == 19:
        error_numbers = '7/3,10,11/17,18'
    elif error_rating == 20:
        error_numbers = '3,7/11,13,15/17,18'
    elif error_rating == 21:
        error_numbers = '3,7/11,12,15/17,18'
    elif error_rating == 22:
        error_numbers = '3,6,16/9,12,14/17,18'
    elif error_rating == 23:
        error_numbers = '4,7/11,12,14/17,18'
    elif error_rating == 24:
        error_numbers = '4,6,16/8,11,13/3,17,18'
    elif error_rating == 25:
        error_numbers = '4,6,16/11-13/3,17,18'
    else:
        error_numbers = 'ERROR'
    return error_numbers


def long_results(result):
    reading = ''
    if result == 1:
        reading = 'lineout(p)'
    elif result == 2:
        reading = 'lineout(c)'
    elif result == 3:
        reading = 'lineout(1b)'
    elif result == 4:
        reading = 'lineout(2b)'
    elif result == 5:
        reading = 'lineout(3b)'
    elif result == 6:
        reading = 'lineout(ss)'
    elif result == 11:
        reading = 'lomax(1b)'
    elif result == 12:
        reading = 'lomax(2b)'
    elif result == 13:
        reading = 'lomax(3b)'
    elif result == 14:
        reading = 'lomax(ss)'
    elif result == 18:
        reading = 'foulout(c)'
    elif result == 19:
        reading = 'foulout(1b)'
    elif result == 21:
        reading = 'foulout(3b)'
    elif result == 27:
        reading = 'popout(1b)'
    elif result == 28:
        reading = 'popout(2b)'
    elif result == 29:
        reading = 'popout(3b)'
    elif result == 30:
        reading = 'popout(ss)'
    elif result == 33:
        reading = 'gb(p)A'
    elif result == 34:
        reading = 'gb(c)A'
    elif result == 35:
        reading = 'gb(1b)A'
    elif result == 36:
        reading = 'gb(2b)A'
    elif result == 37:
        reading = 'gb(3b)A'
    elif result == 38:
        reading = 'gb(ss)A'
    elif result == 41:
        reading = 'gb(p)B'
    elif result == 42:
        reading = 'gb(c)B'
    elif result == 43:
        reading = 'gb(1b)B'
    elif result == 44:
        reading = 'gb(2b)B'
    elif result == 45:
        reading = 'gb(3b)B'
    elif result == 46:
        reading = 'gb(ss)B'
    elif result == 49:
        reading = 'gb(p)C'
    elif result == 50:
        reading = 'gb(c)C'
    elif result == 51:
        reading = 'gb(1b)C'
    elif result == 52:
        reading = 'gb(2b)C'
    elif result == 53:
        reading = 'gb(3b)C'
    elif result == 54:
        reading = 'gb(ss)C'
    elif result == 57:
        reading = 'GB(P)X'
    elif result == 59:
        reading = 'GB(1B)X'
    elif result == 60:
        reading = 'GB(2B)X'
    elif result == 61:
        reading = 'GB(3B)X'
    elif result == 62:
        reading = 'GB(SS)X'
    elif result == 66:
        reading = 'CATCH-X'
    elif result == 73:
        reading = 'FLY(LF)X'
    elif result == 74:
        reading = 'FLY(CF)X'
    elif result == 75:
        reading = 'FLY(RF)X'
    elif result == 81:
        reading = 'fly(lf)A'
    elif result == 82:
        reading = 'fly(cf)A'
    elif result == 83:
        reading = 'fly(rf)A'
    elif result == 89:
        reading = 'fly(lf)B'
    elif result == 90:
        reading = 'fly(cf)B'
    elif result == 91:
        reading = 'fly(rf)B'
    elif result == 97:
        reading = 'fly(lf)B?'
    elif result == 98:
        reading = 'fly(cf)B?'
    elif result == 99:
        reading = 'fly(rf)B?'
    elif result == 105:
        reading = 'fly(lf)C'
    elif result == 106:
        reading = 'fly(cf)C'
    elif result == 107:
        reading = 'fly(rf)C'
    elif result == 113:
        reading = 'SINGLE(LF)'
    elif result == 114:
        reading = 'SINGLE(CF)'
    elif result == 115:
        reading = 'SINGLE(RF)'
    elif result == 120:
        reading = 'SINGLE*'
    elif result == 128:
        reading = 'SINGLE**'
    elif result == 136:
        reading = 'DOUBLE'
    elif result == 137:
        reading = 'DOUBLE(LF)'
    elif result == 138:
        reading = 'DOUBLE(CF)'
    elif result == 139:
        reading = 'DOUBLE(RF)'
    elif result == 144:
        reading = 'DOUBLE**'
    elif result == 152:
        reading = 'TRIPLE'
    elif result == 160:
        reading = 'HOMERUN'
    elif result == 161:
        reading = 'N-HOMERUN'
    elif result == 168:
        reading = 'WALK'
    elif result == 176:
        reading = 'HBP'
    elif result == 184:
        reading = 'strikeout'
    elif result == 195:
        reading = 'gb(1b)A+'
    elif result == 196:
        reading = 'gb(2b)A+'
    elif result == 197:
        reading = 'gb(3b)A+'
    elif result == 198:
        reading = 'gb(ss)A+'
    elif result ==203:
        reading = 'gb(1b)B+'
    elif result == 204:
        reading = 'gb(2b)B+'
    elif result == 205:
        reading = 'gb(3b)B+'
    elif result == 206:
        reading = 'gb(ss)B+'
    elif result == 210:
        reading = ' \u25c6\u2004'
    elif result == 211:
        reading = ' \u25bc\u2009'
    else:
        pass
    return reading


def short_results(result):
    reading = ''
    if result == 1:
        reading = 'lo(p)'
    elif result == 2:
        reading = 'lo(c)'
    elif result == 3:
        reading = 'lo(1b)'
    elif result == 4:
        reading = 'lo(2b)'
    elif result == 5:
        reading = 'lo(3b)'
    elif result == 6:
        reading = 'lo(ss)'
    elif result == 33:
        reading = 'gb(p)A'
    elif result == 34:
        reading = 'gb(c)A'
    elif result == 35:
        reading = 'gb(1b)A'
    elif result == 36:
        reading = 'gb(2b)A'
    elif result == 37:
        reading = 'gb(3b)A'
    elif result == 38:
        reading = 'gb(ss)A'
    elif result == 41:
        reading = 'gb(p)B'
    elif result == 42:
        reading = 'gb(c)B'
    elif result == 43:
        reading = 'gb(1b)B'
    elif result == 44:
        reading = 'gb(2b)B'
    elif result == 45:
        reading = 'gb(3b)B'
    elif result == 46:
        reading = 'gb(ss)B'
    elif result == 49:
        reading = 'gb(p)C'
    elif result == 50:
        reading = 'gb(c)C'
    elif result == 51:
        reading = 'gb(1b)C'
    elif result == 52:
        reading = 'gb(2b)C'
    elif result == 53:
        reading = 'gb(3b)C'
    elif result == 54:
        reading = 'gb(ss)C'
    elif result == 81:
        reading = 'fb(lf)A'
    elif result == 82:
        reading = 'fb(cf)A'
    elif result == 83:
        reading = 'fb(rf)A'
    elif result == 89:
        reading = 'fb(lf)B'
    elif result == 90:
        reading = 'fb(cf)B'
    elif result == 91:
        reading = 'fb(rf)B'
    elif result == 105:
        reading = 'fb(lf)C'
    elif result == 106:
        reading = 'fb(cf)C'
    elif result == 107:
        reading = 'fb(rf)C'
    elif result == 120:
        reading = 'SI*'
    elif result == 128:
        reading = 'SI**'
    elif result == 136:
        reading = 'DO'
    elif result == 144:
        reading = 'DO**'
    elif result == 152:
        reading = 'TR'
    elif result == 160:
        reading = 'HR'
    elif result == 161:
        reading = 'N-HR'
    else:
        pass
    return reading


def front_split(split):
    reading = ''
    if split == 1:
        reading = '1'
    elif split == 2:
        reading = '1-2'
    elif split == 3:
        reading = '1-3'
    elif split == 4:
        reading = '1-4'
    elif split == 5:
        reading = '1-5'
    elif split == 6:
        reading = '1-6'
    elif split == 7:
        reading = '1-7'
    elif split == 8:
        reading = '1-8'
    elif split == 9:
        reading = '1-9'
    elif split == 10:
        reading = '1-10'
    elif split == 11:
        reading = '1-11'
    elif split == 12:
        reading = '1-12'
    elif split == 13:
        reading = '1-13'
    elif split == 14:
        reading = '1-14'
    elif split == 15:
        reading = '1-15'
    elif split == 16:
        reading = '1-16'
    elif split == 17:
        reading = '1-17'
    elif split == 18:
        reading = '1-18'
    elif split == 19:
        reading = '1-19'
    return reading


def back_split(split):
    reading = ''
    if split == 1:
        reading = '2-20'
    elif split == 2:
        reading = '3-20'
    elif split == 3:
        reading = '4-20'
    elif split == 4:
        reading = '5-20'
    elif split == 5:
        reading = '6-20'
    elif split == 6:
        reading = '7-20'
    elif split == 7:
        reading = '8-20'
    elif split == 8:
        reading = '9-20'
    elif split == 9:
        reading = '10-20'
    elif split == 10:
        reading = '11-20'
    elif split == 11:
        reading = '12-20'
    elif split == 12:
        reading = '13-20'
    elif split == 13:
        reading = '14-20'
    elif split == 14:
        reading = '15-20'
    elif split == 15:
        reading = '16-20'
    elif split == 16:
        reading = '17-20'
    elif split == 17:
        reading = '18-20'
    elif split == 18:
        reading = '19-20'
    elif split == 19:
        reading = '20'
    return reading


def get_result_list(result):
    result_list = []
    if result in [1, 2, 3, 4, 5, 6,  # lineout
                  11, 12, 13, 14,  # lomax
                  18, 19, 21,  # foulout
                  27, 28, 29, 30,  # popout
                  105, 106, 107,  # flyC
                  184,  # strikeout
                  ]:
        result_list.append('pure_out')
    if result in [11, 12, 13, 14]:
        result_list.append('lomax')
    if result in [33, 35, 36, 37, 38, 195, 196, 197, 198]:
        result_list.append('gbA')
    if result in [36, 38, 196, 198]:
        result_list.append('gbA_middle')
    if result in [35, 37, 195, 197]:
        result_list.append('gbA_corner')
    if result in [41, 43, 44, 45, 46, 203, 204, 205, 206]:
        result_list.append('gbB')
    if result in [44, 46, 204, 206]:
        result_list.append('gbB_middle')
    if result in [43, 45, 203, 205]:
        result_list.append('gbB_corner')
    if result in [51, 52, 53, 54]:
        result_list.append('gbC')
    if result in [52, 54]:
        result_list.append('gbC_middle')
    if result in [51, 53]:
        result_list.append('gbC_corner')
    if result in [57, 59, 60, 61, 62, 66, 73, 74, 75]:
        result_list.append('x_chart')
    if result in [81, 82, 83, 89, 90, 91]:
        result_list.append('fly_B')
    if result in [97, 98, 99]:
        result_list.append('fly_Bx')
    if result in [120]:
        result_list.append('single_1')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
    if result in [128]:
        result_list.append('single_2')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
    if result in [113, 114, 115]:
        result_list.append('single_open')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
    if result in [144]:
        result_list.append('double_2')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
        result_list.append('total_bases')
    if result in [136, 137, 138, 139]:
        result_list.append('double_open')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
        result_list.append('total_bases')
    if result in [152]:
        result_list.append('triple')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
        result_list.append('total_bases')
        result_list.append('total_bases')
    if result in [160, 161]:
        result_list.append('homerun')
        result_list.append('hits')
        result_list.append('on_base')
        result_list.append('total_bases')
        result_list.append('total_bases')
        result_list.append('total_bases')
        result_list.append('total_bases')
    if result in [168, 176]:
        result_list.append('walk')
        result_list.append('on_base')
    if result in [210]:
        result_list.append('ballpark_homerun')
    if result in [211]:
        result_list.append('ballpark_single')
    return result_list


def clutch_lookup(result):
    clutch = 0
    if result.clutch:
        if result.primary_result == 1:
            clutch = 1
        elif result.primary_result == 2:
            clutch = 1
        elif result.primary_result == 3:
            clutch = 1
        elif result.primary_result == 4:
            clutch = 1
        elif result.primary_result == 5:
            clutch = 1
        elif result.primary_result == 6:
            clutch = 1
        elif result.primary_result == 11:
            clutch = 1
        elif result.primary_result == 12:
            clutch = 1
        elif result.primary_result == 13:
            clutch = 1
        elif result.primary_result == 14:
            clutch = 1
        elif result.primary_result == 18:
            clutch = 1
        elif result.primary_result == 19:
            clutch = 1
        elif result.primary_result == 21:
            clutch = 1
        elif result.primary_result == 27:
            clutch = 1
        elif result.primary_result == 28:
            clutch = 1
        elif result.primary_result == 29:
            clutch = 1
        elif result.primary_result == 30:
            clutch = 1
        elif result.primary_result == 33:
            clutch = 1
        elif result.primary_result == 34:
            clutch = 1
        elif result.primary_result == 35:
            clutch = 1
        elif result.primary_result == 36:
            clutch = 1
        elif result.primary_result == 37:
            clutch = 1
        elif result.primary_result == 38:
            clutch = 1
        elif result.primary_result == 41:
            clutch = 1
        elif result.primary_result == 42:
            clutch = 1
        elif result.primary_result == 43:
            clutch = 1
        elif result.primary_result == 44:
            clutch = 1
        elif result.primary_result == 45:
            clutch = 1
        elif result.primary_result == 46:
            clutch = 1
        elif result.primary_result == 51:
            clutch = 1
        elif result.primary_result == 52:
            clutch = 1
        elif result.primary_result == 53:
            clutch = 1
        elif result.primary_result == 54:
            clutch = 1
        elif result.primary_result == 81:
            clutch = 1
        elif result.primary_result == 82:
            clutch = 1
        elif result.primary_result == 83:
            clutch = 1
        elif result.primary_result == 89:
            clutch = 1
        elif result.primary_result == 90:
            clutch = 1
        elif result.primary_result == 91:
            clutch = 1
        elif result.primary_result == 97:
            clutch = 1
        elif result.primary_result == 98:
            clutch = 1
        elif result.primary_result == 99:
            clutch = 1
        elif result.primary_result == 184:
            clutch = 1
        elif result.primary_result == 113:
            clutch = -1
        elif result.primary_result == 114:
            clutch = -1
        elif result.primary_result == 115:
            clutch = -1
        elif result.primary_result == 120:
            clutch = -1
        elif result.primary_result == 128:
            clutch = -1
        else:
            pass
    return clutch


def get_position_from_int(position):
    pos_string = ''
    if position == 2:
        pos_string = 'c'
    elif position == 3:
        pos_string = '1b'
    elif position == 4:
        pos_string = '2b'
    elif position == 5:
        pos_string = '3b'
    elif position == 6:
        pos_string = 'ss'
    elif position == 7:
        pos_string = 'lf'
    elif position == 8:
        pos_string = 'cf'
    elif position == 9:
        pos_string = 'rf'
    return pos_string


def get_full_position_name_from_int(position):
    pos_string = ''
    if position == 2:
        pos_string = 'Catchers'
    elif position == 3:
        pos_string = 'First Basemen'
    elif position == 4:
        pos_string = 'Second Basemen'
    elif position == 5:
        pos_string = 'Third Basemen'
    elif position == 6:
        pos_string = 'Shortstops'
    elif position == 7:
        pos_string = 'Left Fielders'
    elif position == 8:
        pos_string = 'Center Fielders'
    elif position == 9:
        pos_string = 'Right Fielders'
    return pos_string


def get_position_int_from_string(position):
    if position == 'c':
        pos = 2
    elif position == '1b':
        pos = 3
    elif position == '2b':
        pos = 4
    elif position == '3b':
        pos = 5
    elif position == 'ss':
        pos = 6
    elif position == 'lf':
        pos = 7
    elif position == 'cf':
        pos = 8
    elif position == 'rf':
        pos = 9
    return pos


def leading_plus(rating):
    if rating > 0:
        result = "+" + str(rating)
    else:
        result = str(rating)
    return result


def create_defense_string(defense_data):
    defense_string = ''
    of_arm_done = False
    for i in range(1, 9):
        if defense_data[i] != '--':
            position_defense = defense_data[i]
            position_defense = position_defense.split('-')
            position_defense = [int(position_defense[0]), int(position_defense[1]),
                                int(position_defense[2])]
            defense_string += get_position_from_int(position_defense[0]) + '- '
            defense_string += str(position_defense[1])
            if position_defense[0] > 6:
                if not of_arm_done:
                    of_arm_done = True
                    defense_string += '(' + leading_plus(defense_data[9]) + ')'
            if position_defense[0] == 2:
                defense_string += '(' + leading_plus(defense_data[10]) + ')'
            defense_string += 'e' + str(position_defense[2])
            if position_defense[0] == 2:
                defense_string += ",T-{}(pb-{})".format(defense_data[11], defense_data[12])
            defense_string += ' / '
    defense_string = defense_string[:-3]
    return defense_string


def create_error_string(defense_data):
    error_string = ''
    corner_of_done = False
    for i in range(1, 9):
        if defense_data[i] != '--':
            position_defense = defense_data[i]
            position_defense = position_defense.split('-')
            position_defense = [int(position_defense[0]), int(position_defense[1]),
                                int(position_defense[2])]
            if position_defense[0] == 7 or position_defense[0] == 9:
                if corner_of_done:
                    if position_defense[0] == 7:
                        error_string = error_string.replace('rf', 'rf/lf')
                    if position_defense[0] == 9:
                        error_string = error_string.replace('lf', 'lf/rf')
                else:
                    corner_of_done = True
                    error_string += get_position_from_int(position_defense[0]) + '- '
                    error_string += get_error_numbers(position_defense[0], position_defense[2])
            else:
                error_string += get_position_from_int(position_defense[0]) + '- '
                error_string += get_error_numbers(position_defense[0], position_defense[2])
        error_string += "  "
    error_string = error_string[:-2]
    return error_string


def create_defense_ratings(defense_data):
    from defensive_values import defensive_value as dv
    defense = {
        'c': 0, '1b': 0, '2b': 0, '3b': 0,
        'ss': 0, 'lf': 0, 'cf': 0, 'rf': 0
    }
    for i in range(1, 9):
        if defense_data[i] != '--':
            position_defense = defense_data[i]
            position_defense = position_defense.split('-')
            position = get_position_from_int(int(position_defense[0]))
            error_rtg = int(position_defense[2])
            range_ = int(position_defense[1])
            defensive_value = dv[position][error_rtg][range_ - 1]
            if position == 'c':
                defensive_value += (defense_data[10] + 5) * 25.0 / 9.0
                defensive_value += defense_data[11] * 5.0 / 36.0
                defensive_value += defense_data[12] * 5.0 / 108.0
            elif position == 'lf':
                defensive_value += (defense_data[9] + 5) * 5.0 / 24.0
            elif position == 'cf':
                defensive_value += (defense_data[9] + 5) * 7.0 / 12.0
            elif position == 'rf':
                defensive_value += (defense_data[9] + 5) * 0.25
            defense[position] = defensive_value
    return defense


def build_numbers_string(input_str, test, first_number):
    input_str += '-'
    numbers = ''
    test_holding = [0, 0]
    for i in range(len(input_str)):
        if input_str[i] == test:
            if test_holding[0] == 0:
                test_holding[0] = i + first_number
            else:
                test_holding[1] = i + first_number
        else:
            if test_holding[0] == 0:
                pass
            elif test_holding[1] == 0:
                numbers += '{},'.format(test_holding[0])
            elif test_holding[1] - test_holding[0] == 1:
                numbers += '{},{},'.format(test_holding[0], test_holding[1])
            else:
                numbers += '{}-{},'.format(test_holding[0], test_holding[1])
            test_holding = [0, 0]
    if len(numbers) > 0:
        numbers = numbers[:-1]
    if numbers == '':
        numbers = '-'
    return numbers


def build_stealing_string(asterisk, front_number, back_number, lead_str):
    stealing_string = ''
    if asterisk:
        stealing_string += "*"
    if front_number == 0:
        stealing_string = "-/- (---)"
    else:
        stealing_string += build_numbers_string(lead_str, "L", 2) + "/"
        stealing_string += build_numbers_string(lead_str, "O", 2)
        stealing_string += " ({}-{})".format(front_number, back_number)
    return stealing_string


def pitcher_positions(position):
    pos_string = ''
    position = position.lower()
    if position == 'sp':
        pos_string = 'Starting Pitchers'
    elif position == 'lsp':
        pos_string = 'Left Handed Starting Pitchers'
    elif position == 'rsp':
        pos_string = 'Right Handed Starting Pitchers'
    elif position == 'rp':
        pos_string = 'Relief Pitchers'
    elif position == 'rlp':
        pos_string = 'Left Handed Relief Pitchers'
    elif position == 'rrp':
        pos_string = 'Right Handed Relief Pitchers'
    return pos_string
