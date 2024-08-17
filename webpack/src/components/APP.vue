<!-- 这是一个vue单文件组件 -->

<template>
	<div>
		<h1>这是APP根组件</h1>
	</div>
</template>

<script>
	export default{
		data(){
			return{}
		},
		methods:{}
	}
</script>

<!-- 加上scoped之后，这里的样式就是这个组件私有的，就不会产生冲突了 -->
<style scoped>
	h1{
		color: red;
	}
</style>
