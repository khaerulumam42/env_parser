package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func fileExists(filename string) bool {
	info, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}

func parserDotEnv(inputFile string, outputFile string, force bool) {
	b, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Print(err)
		return
	}

	if fileExists(outputFile) && !force {
		fmt.Printf("path %s exists, use --force to overwrite\n", outputFile)
	} else {
		f, err := os.Create(outputFile)
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
}

func main() {
	args := os.Args
	force := false
	if len(args) > 1 {
		arg := args[1]
		if arg == "--force" {
			force = true
		}
	}
	parserDotEnv(".env", "env.example", force)
}
