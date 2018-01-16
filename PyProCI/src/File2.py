import twitter

# Create an Api instance.
api = twitter.Api('ACZL1iLsSDBHR7htZiLQO2QDp',"sJjPc6qUfqwnwj0R8Ac1Ca8X6SzjeowXEIUsNXSVeAsMqp6HHp","858764635-ebJ9SyoUZ4ZEr9SZ1mofcqJq3rDUwTus1PCQ40r7",
"zPx5EqpQOTK9zJyJc9rhBJynfWrwJju71pv6dyCEq0rku")

users = api.GetFriends()

print(users)
