package main

import "fmt"

type santa struct {
	floor int
}

func (s *santa) move(c rune) {
	if c == '(' {
		s.floor++
	} else if c == ')' {
		s.floor--
	} else {
		panic(fmt.Sprintf("Invalid Rune: %c", c))
	}
}
