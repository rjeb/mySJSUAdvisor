<template>
  <div id="app">
    <img alt="Adivisor logo" src="./assets/logoNew.png">
    <h1>Welcome to MY ADVISOR</h1>
    <p> My advisor is an application which will make the process of selecting classes easier for you......</p>
    <p>ADD MORE HERE ABOUT THE APP</p>
    <employee-form />
  </div>
</template>

<script>
import EmployeeForm from './components/EmployeeForm.vue'

export default {
  name: 'App',
  components: {
      EmployeeForm, 
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background-color: #dcd6f7;
}
</style>
