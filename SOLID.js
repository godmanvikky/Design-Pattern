


//Single Responsibility Principle
var fs = require('fs');
class Journal{
    constructor(){
        this.enteries={}
    }
    addEntery(text){
        let c=++Journal.count
        this.enteries[c]=text
        return c
    }
    deleteEntry(index){
        delete this.enteries[index]
    }
    toString(){
        return Object.values(this.enteries).join('\n')
    }
}
class Presistence{
   saveTofile(journal,filename){
       fs.writeFileSync(filename,journal.toString())
   }
}
// Journal.count=0
// let j=new Journal()
// j.addEntery("Hello Vikky")
// j.addEntery("Hello World")
// j.addEntery("Hello Vaish")
// let p =new Presistence()
// p.saveTofile(j,"e:/form/vikky.txt")
//Single Responsibility Principle 2nd Example
class Book{
    constructor(){
        this.book={}
    }
    addEntry(name,author,year){
        let count=++Book.count
        this.book[count]={
            'name':name,
            'author':author,
            'year':year
        }
        return count
    }
    removEntry(index){
        var temp=this.book[index]
        delete this.book[index]
        return temp
    }
    toString(){
        var a=Object.values(this.book)
        return a
    }
}
class Filter{
    filterByname(item,Bname){
        return item.filter(({name})=>
            name==Bname
        )
    }
}
// Book.count=0
// let b=new Book()
// b.addEntry('Lost in Space','JackSparrow',2013)
// b.addEntry('Flash','Paul Walker',2014)
// var f=new Filter()
// console.log(f.filterByname(b.toString(),'Flash')[0].name="Dark")
let Color=Object.freeze({
    red:'red',
    blue:'blue',
    green:'green',
    black:'black'
})
let Size=Object.freeze({
    small:'small',
    large:'large',
    medium:'medium'
})
class Amazon{
    constructor(name,color,size){
        this.name=name
        this.color=color
        this.size=size
    }
    addProduct(){
        Amazon.cart.push(this)
    }
}
class SpecByColor{
    constructor(color){
        this.color=color;
    }
    isOk(item){
        return this.color==item.color
    }
}
class SpecBySize{
    constructor(size){
        this.size=size;
    }
    isOk(item){
        return this.size==item.size;
    }
}
class BaseFilter{
    advFilter(arrObj,className){
        return arrObj.filter((x)=>className.isOk(x))
    }
}
class AndFilter{
    constructor(...spec){
        this.spec=spec
    }
    andfilter(){
        
    }
}
var and=new AndFilter(new SpecByColor(Color.green),new SpecBySize(Size.large))
console.log(and)
Amazon.cart=[]
var a=new Amazon('Dog',Color.black,Size.large)
var b=new Amazon('Donkey',Color.black,Size.medium)
var c=new Amazon('Snake',Color.blue,Size.small)
a.addProduct()
b.addProduct()
c.addProduct()
Amazon.cart.map(({name,color})=>{
    console.log(name,color)
})
var base=new BaseFilter()
for(var p of base.advFilter([a,b,c],new SpecByColor(Color.black))){
    console.log(p)
}
for(var p of base.advFilter([a,b,c],new SpecBySize(Size.small))){
    console.log(p)
}

// Call

function Product(){
    this.name="vikky"
    this.age=23
    this.disp=function() {
        console.log(this.name)
    }
}

function Donkey() {

    Product.call(this)
    
}
var d=new Donkey()
d.disp()