package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {

	b, err := ioutil.ReadFile(".env")
	if err != nil {
		fmt.Print(err)
	}

	f, err := os.Create("env.example")
	if err != nil {
		fmt.Println(err)
		return
	}

	str := string(b)
	lines := strings.Split(str, "\n")
	for _, line := range lines {
		if strings.Contains(line, "=") {
			splitedLine := strings.Split(line, "=")
			fmt.Fprint(f, splitedLine[0], "=", "\n")
			if err != nil {
				fmt.Println(err)
				return
			}
		} else {
			fmt.Fprintln(f, line)
			if err != nil {
				fmt.Println(err)
				return
			}
		}
	}
}
