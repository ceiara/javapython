# quiz 1
st = "The Espresso Spirit"
ucp = st.upper()
lcp = st.lower()
print(ucp)
print(lcp)
print(st)

print()
# quiz 2
def birth_only(p1):
    plist = p1.split("-")
    return plist("-")[0]

p1 = "070609-2011xx"
p1 = birth_only(p1)
print(p1)
