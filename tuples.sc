//Write a function cycle: (Int,Int,Int) => (Int,Int,Int) that takes a triple of integers and “cycles through them”, 
//moving the first component to the end and the other two forward, e.g. cycle((1,2,3)) = (2,3,1).
def cycle(t: (Int,Int,Int)): (Int,Int,Int) = {
  (t._2, t._3, t._1)
}
