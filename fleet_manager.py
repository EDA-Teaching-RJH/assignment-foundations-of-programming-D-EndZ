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

def add_member(names, ranks, div, id):
    names = input("Name: ")
    ranks = input("Rank: ")
    div = input("Division: ")
    new_id = int(input("ID: "))

    if new_id in id:
        print("ID already exists")
        return

    if ranks in ["Captain", "Commander", "Lt.Commander", "Ensign", "Lieutenant"]:
        valid = True
    else:
        valid = False

    if valid == False:
        print("Rank unrecognised")
        return
    
    names.append(names)
    ranks.append(ranks)
    div.append(div)
    ids.append(new_id)
    print("Crew Memeber Added")


def remove_member(names, ranks, div, id):
    remove_id = int(input("Enter ID: "))
    if remove_id in id:
        i = id.index(remove_id)
        names.pop(i)
        ranks.pop(i)
        div.pop(i)
        id.pop(i)
        print("Member removed")
    else:
        print("Member not found")



def update_rank(names, ranks, id):
    target = int(input("ID: "))

    if target in id:
        i = id.index(target)
        new_rank = input("New rank: ")
        ranks[i] = new_rank
        print("Rank updated")
    else:
        print("Rank not found")



def display_roster(names, ranks, div, id):
    print("\nRoster:")
    for i in range(len(names)):
        print(id[i], names[i], ranks[i], div[i])


def search_crew(names, ranks, div, id):
    term = input("Search for crew member:")
    for i in range(len(names)):
        if term.lower() in names[i].lower():
            print("Found")
            print(names[i], ranks[i], div[i], id[i])
        else:
            print("Crew member not found")




def filter_by_div(names, divs):
    input = input("Enter the division you require: ")
    for i in range(len(names)):
        if divs[i] == input:
            print("List of members in " + input)
            print(names[i])



def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt. Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200

    return total



count_officers(ranks)