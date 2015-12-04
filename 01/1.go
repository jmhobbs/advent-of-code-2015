package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {

	fi, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := fi.Close(); err != nil {
			panic(err)
		}
	}()

	s := santa{}
	r := bufio.NewReader(fi)
	for {
		if c, _, err := r.ReadRune(); err != nil {
			if err == io.EOF {
				break
			} else {
				panic(err)
			}
		} else {
			s.move(c)
		}
	}

	fmt.Printf("Floor: %d\n", s.floor)

}
