<template>
  <div id="employee-form">
    <div>
      <h3>Department name(example: CS)</h3>
      <input type="text" v-model="name">
      <h3>Course Number(example: 161)</h3>
      <input type="text" v-model="number">
      <h2>Submit</h2>
      <input type="submit" value="Submit" v-on:click="submit"/>
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
      submit(){
        this.submitting = true
        this.clearStatus()
        console.log(this.name, this.number);
        this.name = '';
        this.number = '';
        this.success = true
        this.error = false
        this.submitting = false
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