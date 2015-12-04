package main

import (
	"io"
	"strings"
	"testing"
)

func CheckBasementForString(t *testing.T, s string, expected int) {
	t.Logf("Expecting %s to enter basement on move %d.", s, expected)
	r := strings.NewReader(s)
	snta := santa{}
	for {
		if c, _, err := r.ReadRune(); err != nil {
			if err == io.EOF {
				break
			} else {
				panic(err)
			}
		} else {
			snta.move(c)
			if snta.floor < 0 {
				break
			}
		}
	}

	if snta.moves != expected {
		t.Errorf("!!!  Expected move %d, but got %d", expected, snta.moves)
	}

}

func TestCaseFloorOne(t *testing.T) {
	// ) causes him to enter the basement at character position 1.
	CheckBasementForString(t, ")", 1)
}

func TestCaseFloorFive(t *testing.T) {
	// ()()) causes him to enter the basement at character position 5.
	CheckBasementForString(t, "()())", 5)
}
