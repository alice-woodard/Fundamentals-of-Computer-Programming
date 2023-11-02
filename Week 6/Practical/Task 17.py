""": Examine the above code and work out which user names will be placed in the
some_users list. What is the condition that has to be met for inclusion?"""
some_users = [u for u in all_users if len(u) < 8]
# a user will be placed in some_users if their username is less than 8 charactors in length