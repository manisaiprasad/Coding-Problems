// The Scala ListMap class provides a method contains, testing whether a map m contains a key k which can be written a same thod call m.contains(k)
//  or infix as m contains k. Using contains,write a function election that takes a list of Strings and constructs a ListMap[String,Int] 
// such that for each k, the value of m(k) is the number of occurrences of k in the initial list.

def election(l:List[String]):ListMap[String,Int] = {
  var m = ListMap[String,Int]()
	for(i <- l) {
		if(m.contains(i)) {
			m = m + (i -> (m(i)+1))
		} else {
			m = m + (i -> 1)v
		}
	}
	return m
}

val l = List("a","a","b","c","c","c","d")
election(l)
