// ./src/index.js

import $ from 'jquery'
import './css/index.css'
import Vue from 'vue'
import APP from './components/APP.vue'

$(function(){
    $('li:odd').css('backgroundColor','pink')
    $('li:even').css('backgroundColor','skyblue')
})

const vm = new Vue({
    el:'#app',  //  挂载点，挂载到id为app的div上
    render:h => h(APP)  // 渲染APP组件, 通过render方法将APP组件渲染到挂载点el上
})

class Person{
    static info = '我是静态属性'
    static say(){
        console.log('我是静态方法')
    }
}
console.log(Person.info)