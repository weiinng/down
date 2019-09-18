ES6 简单语法

let 和 const
模板字符串
箭头函数
对象单体模式
es6面向对象
模块化



let 和 const
// 之前一直用 var 来声明变量
// ES6  新增 let 和 const
// let 
script type="text/javascript">

    // let声明变量块级作用域,不能重复声明
    // let声明的变量 是块级作用域,不能重复声明
    // {
    //     // let a = 12;
    //     let a  = 12;
    //     let a  = 13;
    // }
   
    // console.log(a);
	
	// var 的坑 ，循环的时候会按照最后一次的赋值
    // var a = [];
    // for (var i = 0; i < 10; i++) {	//这里的 var i 换成 let i 即可解决
    //  a[i] = function () {
    //     console.log(i);
    // };
    // }
    // a[6](); // var 10 ，let 6
    
    // var 会发生变量提升
    console.log(foo); // 输出undefined
    var foo = 2;
	// let  不发生变量提升 
	console.log(foo); // 报错 ReferenceError
    let foo = 2;

    // const 声明常量，一旦声明，立即初始化，不能重复声明。
	const foo; // 没立即赋值，会报错
	// const 声明是只读常量，不可更改
	const P = 1
	P = 2 // 报错无法更改
</script>


模板字符串
// 更加的简单的拼接字符串 用 ${} 来填入
<script>
	var a = 1;
	var b = 2;

	// var str = "哈哈哈哈" + a + "嘿嘿嘿" + b;
	// ` xxx${}xxxx${}xxx`  注意反引号 
	var str = `哈哈哈哈${a}嘿嘿嘿${b}`; 	
	console.log(str);
</script>



箭头函数
// 操作更加简单了，但是改变了特性造成了不便
<script>
	// function(){} --等同于--- ()=>{}

	// 1.this的指向发生改变，指向了定义对象时的对象
			// function(){} 的时候相当于 self 
			// ()=>{} 的时候相当于 windows
	// 2.arguments不能使用，无法再通过 arguments 拿所有的参数 
	
</script>


对象单体模式
// 为了解决箭头函数的问题 
// (){} 完全等同于 function(){} 不再有上面的困扰了
<script>
	var person = {
		name:'张三',
		age: 18,
	   
		fav(){
			console.log(this);
			console.log(arguments);
		}
	}
	person.fav();
</script>



es6面向对象
<script>
    // 构造函数的方式创建对象
    //  function Animal(name,age){
    //      this.name = name;
    //      this.age = age;
        
    //  }
    //  Animal.prototype.showName = function(){
    //      console.log(this.name);
    //  }
    //  Animal.prototype.showName2 = function(){
    //      console.log(this.name);
    //  }
    //  Animal.prototype.showName3 = function(){
    //      console.log(this.name);
    //  }
    //  Animal.prototype.showName4 = function(){
    //      console.log(this.name);
    //  }
    //  var dog = new Animal('日天',18)



    class Animal{
        constructor(name,age){ //  必须要 constructor 初始化属性 类似于 init 
            this.name = name;
            this.age = age;
        }  // 这一行一定不要加逗号
        showName(){
            console.log(this.name)
        }
    }
    var d = new Animal('张三',19);
    d.showName();
</script>






