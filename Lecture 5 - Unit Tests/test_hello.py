from hello import hello 


def test_hello():
   assert hello("Kanishk") == "hello, Kanishk"
   
   
def test_argument():
   assert hello() == "hello, world"