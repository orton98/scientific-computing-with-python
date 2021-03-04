if __name__ == '__main__':
    line = input("Write something: ")
    character_counter = {}
    for character in line:
        character_counter[character] = character_counter.get(character,0)+1
    print(character_counter)