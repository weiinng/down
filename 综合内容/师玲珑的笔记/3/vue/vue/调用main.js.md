import main from "../../static/main"
	alert(main.person.name)
这个在script 里
export default的上面

static里main.js
var person={
	name:"张三",
	age:20,
	getname:function(){
		return this.name
	},
	getage:function(){
		return this.age
	}
}
export default{person}