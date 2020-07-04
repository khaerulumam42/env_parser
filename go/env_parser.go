package main

import (
    "fmt"
    "os"
    "log"
)

func main() {
    file, err := os.Open(".env")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Print(file)
}