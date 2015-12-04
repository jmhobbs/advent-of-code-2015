package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {

	floor := 0

	fi, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := fi.Close(); err != nil {
			panic(err)
		}
	}()

	r := bufio.NewReader(fi)
	for {
		if c, _, err := r.ReadRune(); err != nil {
			if err == io.EOF {
				break
			} else {
				log.Fatal(err)
			}
		} else {
			if c == '(' {
				floor++
			} else if c == ')' {
				floor--
			}
		}
	}

	fmt.Printf("Floor: %d\n", floor)

}
