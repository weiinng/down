JavaScript对象有两种属性：数据属性和访问器属性 

## 1.数据属性

数据属性包含一个数据值的位置，在这个位置可以读取和写入值。即数据属性限制使用者对对象属性数据值的读取和写入权限，有四种特性 
（1）[[Configurable]]：表示能否通过 delete 删除属性从而重新定义属性，能否修改属性的特性，或者能否把属性修改为访问器属性。像前面例子中那样直接在对象上定义的属性，它们的这个特性默认值为 true。 
（2）[[Enumerable]]：表示能否通过 for-in 循环返回属性。像前面例子中那样直接在对象上定义的属性，它们的这个特性默认值为 true。 
（3）[[Writable]]：表示能否修改属性的值。像前面例子中那样直接在对象上定义的属性，它们的这个特性默认值为 true。 
（4）[[Value]]：包含这个属性的数据值。读取属性值的时候，从这个位置读；写入属性值的时候，把新值保存在这个位置。这个特性的默认值为 undefined。 

### 例1：

```javascript
var person={
    name:"Nacy",
    age:11
}
```



像上面这种直接在对象上定义的属性，它们的[[Configurable]]、 [[Enumerable]] 
和[[Writable]]特性都被设置为 true，而[[Value]]特性被设置为指定的值。 

ECMAScript 5提供了Object.defineProperty()方法可以修改属性的默认特性，这个方法接收三个参数：一个描述符对象属性所在的对象，属性的名字和一个描述符对象，其中，描述符对象的属性必须是： configurable、 enumerable、 writable 和 value。 

### 例2：

```javascript
var person = {};
Object.defineProperty(person, "name", {
writable: false,
value: "Nicholas"
});
alert(person.name); //"Nicholas"
person.name = "Greg";
alert(person.name); //"Nicholas"
```

### 例3：

```javascript
var person = {};
Object.defineProperty(person, "name", {
configurable: false,
value: "Nicholas"
});
alert(person.name); //"Nicholas"
delete person.name;
alert(person.name); //"Nicholas"

```

注：像例3中，将那么属性设置为不可配置的，则无法再次使用Object.defineProperty()方法将其设置为可配置的。

## 2.访问器属性

访问器属性包含一对getter和setter函数，有四个特性 
（1）[[Configurable]]：表示能否通过 delete 删除属性从而重新定义属性，能否修改属性的特性，或者能否把属性修改为数据属性。对于直接在对象上定义的属性，这个特性的默认值为true。 
（2）[[Enumerable]]：表示能否通过 for-in 循环返回属性。对于直接在对象上定义的属性，这个特性的默认值为 true。 
（3）[[Get]]：在读取属性时调用的函数。默认值为 undefined。 
（4） [[Set]]：在写入属性时调用的函数。默认值为 undefined。 
同样，可以通过Object.defineProperty()方法设置访问器的属性。 

### 例4:

```javascript
var book = {
_year: 2018,
edition: 1
};

//将year设置为person的访问器属性，并规定它的getter和setter方法
Object.defineProperty(book, "year", {
get: function(){
return this._year;
},
set: function(newValue){
if (newValue > 2018) {
this._year = newValue;
this.edition += newValue - 2018;
}
}
});
book.year = 2019;
alert(book.edition); //2
```

## 3.定义多个属性

ECMAScript 5 提供了 **Object.defineProperties()方法**用来一次定义多个属性。这个方法接收两个对象参数：第一个参数是要添加和修改其属性的对象，第二个参数是一个对象，和要修改的对象的属性对应。 

### 例5:

```javascript
var book = {};
Object.defineProperties(book, {
_year: {
value: 2004
},
edition: {
value: 1
},
year: {
get: function(){
return this._year;
},
set: function(newValue){
if (newValue > 2004) {
this._year = newValue;
this.edition += newValue - 2004;
}
}
}
});
```

使用 ECMAScript 5 的 Object.getOwnPropertyDescriptor()方法，可以取得给定属性的描述符。这个方法接收两个参数：属性所在的对象和要读取其描述符的属性名称。返回值是一个对象，如果是访问器属性，这个对象的属性有 configurable、 enumerable、 get 和 set；如果是数据属性，这个对象的属性有 configurable、 enumerable、 writable 和 value。