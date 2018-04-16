package main

import "fmt"

func isAlNum(b byte) bool {
	if (b >= '0' && b <= '9') || (b >= 'A' && b <= 'Z') || (b >= 'a' && b <= 'z') {
		return true
	}
	return false
}

func toLower(b byte) byte {
	if b >= 'A' && b <= 'Z' {
		return b + 32
	}
	return b
}

func isPalindrome(s string) bool {
	l, r := 0, len(s)-1
	for l < r {
		for l < r && !isAlNum(s[l]) {
			l++
		}
		for l < r && !isAlNum(s[r]) {
			r--
		}
		if toLower(s[l]) != toLower(s[r]) {
			return false
		}
		l++
		r--
	}
	return true
}

func main() {
	s := "A man, a plan, a canal: Panama"
	fmt.Println(isPalindrome(s))
}
