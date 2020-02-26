<template>
  <div id="employee-form">
    <div>
      <h3>Department name(example: CS)</h3>
      <input type="text" v-model="name">
      <h3>Course Number(example: 161)</h3>
      <input type="text" v-model="number">
      <h2>Submit</h2>
      <input type="submit" value="Submit" v-on:click="submit"/>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'employee-form',
    data: () => ({
      name: '',
      number: ''
    }),
    methods :{
      submit: function(){
        console.log(this.name, this.number);
        this.name = '';
        this.number = '';
      }
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>