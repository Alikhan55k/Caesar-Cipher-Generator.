li1="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
list1=li1.split(",")
message=input("Enter your message:\n")
message=message.lower()
case=input("Enter 'encode' for Encryption and 'decode'for Decription\n")
shift=int(input("Enter Shift No:"))

def encoding(message,shift):
    cypher=""
    for letter in message:
        if letter in list1:
            place=list1.index(letter)
            new_place=place+shift
            new_letter=list1[new_place]
            cypher+=new_letter
        else:
            cypher+=letter
    print(cypher)
    return cypher
def decoding(message,shift):
    cypher=""
    for letter in message:
        if letter in list1:
            place=list1.index(letter)
            new_place=place-shift
            new_letter=list1[new_place]
            cypher+=new_letter
        else:
            cypher+=letter
    print(cypher)
    return cypher

if case=="encode":
    cypher=encoding(message,shift)
    rep=input("\ndo you want to decode yes or no:")
    if rep=="yes":
        decoding(cypher,shift)
else:
    cypher=decoding(message,shift)
    rep=input("\ndo you want to encode  yes or no:")
    if rep=="yes":
        encoding(cypher,shift)