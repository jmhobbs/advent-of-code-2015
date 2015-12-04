package main

import (
	"io"
	"strings"
	"testing"
)

func CheckFloorForString(t *testing.T, s string, expected int) {
	t.Logf("Expecting %s to result in floor %d.", s, expected)
	r := strings.NewReader(s)
	snta := santa{floor: 0}
	for {
		if c, _, err := r.ReadRune(); err != nil {
			if err == io.EOF {
				break
			} else {
				panic(err)
			}
		} else {
			snta.move(c)
		}
	}

	if snta.floor != expected {
		t.Errorf("!!!  Expected floor %d, but got %d", expected, snta.floor)
	}

}

func TestCaseFloorZero(t *testing.T) {
	// (()) and ()() both result in floor 0.
	CheckFloorForString(t, "(())", 0)
	CheckFloorForString(t, "()()", 0)
}

func TestCaseFloorThree(t *testing.T) {
	// ((( and (()(()( both result in floor 3.
	// ))((((( also results in floor 3.
	CheckFloorForString(t, "(((", 3)
	CheckFloorForString(t, "(()(()(", 3)
	CheckFloorForString(t, "))(((((", 3)
}

func TestCaseNegativeOne(t *testing.T) {
	// ()) and ))( both result in floor -1 (the first basement level).
	CheckFloorForString(t, "())", -1)
	CheckFloorForString(t, "))(", -1)
}

func TestCaseNegativeThree(t *testing.T) {
	// ))) and )())()) both result in floor -3.
	CheckFloorForString(t, ")))", -3)
	CheckFloorForString(t, ")())())", -3)
}
