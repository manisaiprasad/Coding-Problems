package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"

)

var TempN int
var TempArr []int

func main() {
	var inputloop int

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	
	inputloop, err := strconv.Atoi(scanner.Text())
    if err != nil{
    	fmt.Println("inputloop error")
    }
	
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "input error:", err)
	}
    TempN = inputloop
	outerrec(inputloop)
}

func printans(n int, c int) int{
	if n ==0{
		return 0
	}
    fmt.Println(TempArr[c])
    return printans(n-1, c+1)
}
func outerrec(n int) int{
	if n== 0{
        printans(TempN, 0)
    	return 0
    }
    var innerloop int
    var iArr []int
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	innerloop, err := strconv.Atoi(scanner.Text())
    if err != nil{
    	fmt.Println("innerloop error")
    }
    innerrec(innerloop, iArr)    
    return outerrec(n-1)

}
func innerrec(n int, arr []int) int{
	if n == 0{
		sumofs(arr, (len(arr)-1), 0)
		return 0
	}
	var i int
	_, err := fmt.Scanf("%d", &i)
	if err != nil{
		return 0
	}
	
	arr = append(arr, i)
	return innerrec(n-1, arr)

}

func sumofs(arr []int, n int, sum int) int{

	if n == -1{
		TempArr = append(TempArr, sum)
		return -1
	}
    if((arr[n] <= 0)&& n>=0){
    	return sumofs(arr, n-1, sum)
    }else{
    	sum+= (arr[n]*arr[n])
    }

    return sumofs(arr, n-1, sum)
     
}