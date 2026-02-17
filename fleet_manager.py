def init_database():
    names = ["Philip Boyce", "Joesph Carey", "Worf", "Jadzia Dax", "Nog"]
    ranks = ["Lt.Commander", "Lieutenant", "Lieutenant", "Lt.Commander", "Ensign"]
    div = ["Medical", "Engineering", "Security", "Sciences", "Operations"]
    id = [101, 102, 103, 104, 105]
    return names, ranks, div, id


def display_menu():
    print("\nSigned in as:", user)
    print("1: Add\n2: Remove\n3: Update Rank\n4: Display\n5: Search\n6: Division\n7: Payroll\n8: Count Officers\n9: Exit")
    choice = input("Choose a function ")
    return choice

remove_member(name, ranks, divs, ids)


update_rank()


display_roster()


search_crew()


filter_by_div()


calculate_payroll(ranks)


count_officers(ranks)