<template>
  <div class="hello">
    <img alt="Adivisor logo" src="./logoLatest.png">
    <h2>WELCOME TO MY ADVISOR</h2>
    <p> My advisor is an application which will make the process of selecting classes easier for you......</p>
    <p>ADD MORE HERE ABOUT THE APP</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h3 {
  margin: 40px 0 0;
}
img {
  padding: 0 7em 2em 0;
  margin: 40px 0 0;
  align: center;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#hello {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 30px;
    background-color: #dcd6f7;
  }
</style>
