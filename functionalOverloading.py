# python doesn't allow traditional functional overloading , it allows Using Default Arguments
# operator overloading built in operator redefine kore user define data types er jonno

def function(arg=None):
    print(arg)
    print(str(type(arg)))

function()
function([1, 2, 3, 4])
