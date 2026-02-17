def init_database():
    names = ["Philip Boyce", "Joesph Carey", "Worf", "Jadzia Dax", "Nog"]
    ranks = ["Lt.Commander", "Lieutenant", "Lieutenant", "Lt.Commander", "Ensign"]
    div = ["Medical", "Engineering", "Security", "Sciences", "Operations"]
    id = [101, 102, 103, 104, 105]
    return names, ranks, div, id


display_menu()


remove_member(name, ranks, divs, ids)


update_rank()


display_roster()


search_crew()


filter_by_div()


calculate_payroll(ranks)


count_officers(ranks)