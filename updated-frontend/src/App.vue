<template>
  <div id="app" class="container">
    <HelloWorld msg="Welcome to My Advisor"/>
    <div class="row justify-content-center">
      <div class="col-xs-12 col-sm-10 col-md-6">
        <h1 class="text-center">{{title}}</h1>
        <app-form></app-form>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import Form from './components/form/Form.vue';
import HelloWorld from './components/form/HelloWorld.vue';

export default {
  name: 'app',
  data () {
    return {
      title: 'Input your classes here'
    }
  },
  components: {
    HelloWorld,
    appForm: Form
  }
}
</script>

<style lang="scss">
  h1 {
    margin-bottom: 5px;
  }

  #app {
    padding: 20px;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    background-color: #dcd6f7;
    margin-top: 60px;
    color: #2c3e50;
  }
  
</style>

