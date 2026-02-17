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

def add_member(names, ranks, divs, ids):
    name = input("Name: ")
    rank = input("Rank: ")
    div = input("Division: ")
    new_id = int(input("ID: "))

    if new_id in id:
        print("ID already exists")
        return

    if rank in ["Captain", "Commander", "Lt.Commander", "Ensign", "Lieutenant"]:
        valid = True
    else:
        valid = False

    if valid == False:
        print("Rank unrecognised")
        return
    
    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(new_id)
    print("Crew Memeber Added")


def remove_member(name, ranks, divs, ids):
    remove_id = int(input("Enter ID: "))
    if remove_id in id:
        i = id.index(remove_id)
        name.pop(i)
        ranks.pop(i)
        divs.pop(i)
        ids.pop(i)
        print("Member removed")
    else:
        print("Member not found")



update_rank()


display_roster()


search_crew()


filter_by_div()


calculate_payroll(ranks)


count_officers(ranks)