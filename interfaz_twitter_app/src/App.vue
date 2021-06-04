<template>
  <div id="app">
    <img src="./assets/Twitter-Logo.png" width="400" height="210">
    <SideBar/>
    <router-view></router-view>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import SideBar from './components/SideBar'

export default {
  name: 'App',
  components: {
    HelloWorld,
    SideBar,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
