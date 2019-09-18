# 常量

常量声明可以使用iota常量生成器初始化，它用于生成一组以相似规则初始化的常量，但是不用每行都写一遍初始化表达式。

注意：在一个const声明语句中，在第一个声明的常量所在的行，iota将会被置为0，然后在每一个有常量声明的行加一。

```go
package main

func main() {

	//iota 枚举
	//iota 枚举格式如果卸载一行中值相等如果换行值+1

	const (
		a = iota
		b = iota
		c,d = iota,iota
	)
}

```

