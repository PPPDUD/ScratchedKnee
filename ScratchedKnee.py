import scratchattach as scratch3
session = scratch3.login("PPPDUD", "censored")
user = session.get_linked_user()





while True:
    logfile = open("usernames.txt", "a")
    user2 = scratch3.get_user(input("Please type in a username: "))
    try:
        for target in user2.followers(limit=40, offset=0):
            logfile.write(target.name + " Followers: " + str(target.follower_count()) + ", Messages: " + str(target.message_count()) + '''
''')
            print(target.name + " Followers: " + str(target.follower_count()) + ", Messages: " + str(target.message_count()))
    

            for target2 in target.followers(limit=40, offset=0):
                logfile.write(target2.name + " Followers: " + str(target2.follower_count()) + ", Messages: " + str(target2.message_count()) + '''
''')

                print(target2.name + " Followers: " + str(target2.follower_count()) + ", Messages: " + str(target2.message_count()))


        print('''
Process complete. See the data in usernames.txt.''')
        
    except Exception as e:
        print(e)

    logfile.close()

    
    






