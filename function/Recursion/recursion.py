# jab koi fu

def hello(n):
    if n==0:
        return
    
    print("Hello")
    hello(n-1)


hello(2)


# hello(2)
#    │
#    └── hello(1)
#           │
#           └── hello(0)
#                  │
#               return
#                  │
#                  ▼
#           hello(1)  ← yahan wapas
#                  │
#               finish
#                  ▼
#           hello(2)  ← fir yahan wapas



# Golden Rule

# Recursion mein:

# Call hamesha neeche jaata hai.
# Return hamesha upar aata hai.
# Call

# hello(2)
#    ↓
# hello(1)
#    ↓
# hello(0)

# Return

# hello(0)
#    ↑
# hello(1)
#    ↑
# hello(2)