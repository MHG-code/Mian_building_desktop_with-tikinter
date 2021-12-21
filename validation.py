def validate_number_of_items(number_of_require_item,total_number_of_item):
    if int(number_of_require_item) > int(total_number_of_item):
        return False
    else:
        return True