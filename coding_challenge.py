

#
# Print out each element of the following array on a separate line:
# ['Joe', '2', 'Ted', '4.98', '14', 'Sam', 'void *', '42', 'float', 'pointers', '5006']
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


# maybe use f string and /n line method?


contents = ['Joe', '2', 'Ted', '4.98', '14', 'Sam', 'void *', '42', 'float', 'pointers', '5006']


# for i in contents:
#     print(i)


contents2 = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def iterater(x):
    for i in x:
        print(i)
        for i in x:
            print(i)

print(iterater(contents2))