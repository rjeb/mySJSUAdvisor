import Vue from 'vue'
import courses from '@components/courses'

<template>
  <component :is="dynamicComponent"></component> 
</template>
<template>
  <div id="employee-form">
    <div>
      <h3>Department name(example: CS)</h3>
      <input type="text" v-model="name">
      <h3>Course Number(example: 161)</h3>
      <input type="text" v-model="number">
      <h2> </h2>
      <button v-on:click="say('Hang on..Working on schedule')">Submit</button>
      <h2> </h2>
      <h2 style="color:DodgerBlue" v-if="error && submitting">
          ERROR
      </h2>
      <h2 style="color:DodgerBlue" v-if="success">
          HANG ON! FINDING THE PERFECT SCHEDULE FOR YOU :)
      </h2>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'employee-form',
    data: () => ({
      name: '',
      number: '',
      success: false,
      submitting: false,
      error: false,
    }),
    methods :{
      say: function(message){
        alert(message)
      },
      dynamicComponent(){
        return 'courses';
      },
      clearStatus(){
        this.success = false
        this.error = false
      }
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>