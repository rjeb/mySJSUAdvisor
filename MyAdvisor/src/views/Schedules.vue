<template>
    <v-container fluid class="#f6eedf">
      <center>
          <h1>Schedules in order of rating from top to bottom</h1>
      </center>
    	<center>
         	<img class="zoom" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions0.png?alt=media&token=09ffc1ce-efb7-4893-91bf-14260ffedf80" align="left" v-if='showImage'> 
         </center>
         <center>
            <img class="zoom" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions1.png?alt=media&token=7c018506-ba5b-41b3-b07b-ed5d5568ab91" align="left" v-if='showImage'>
         </center>       
         <center>
            <img class="zoom" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions2.png?alt=media&token=c26390e1-634d-40a3-9983-fca1c5ff3b8c" align="middle" v-if='showImage'>
         </center> 
         <center>      
         <v-btn
            color="primary"
            to="/"
            data-cy="formBtn"
            >BACK TO HOME PAGE</v-btn> 
          </center>
    </v-container>
</template>

<script>

export default {
    name: 'Schedules',
    data(){
    	return {
    		showImage: true,
    	}
    }
};
</script>

<style scoped>
.box{
	width: 100%;
  	height: 200px;
}
img {
 	width: 100%;
  	height: 100%;

}
.zoom {
  padding: 50px;
  transition: transform .2s;
}

.zoom:hover {
  -ms-transform: scale(1.3); /* IE 9 */
  -webkit-transform: scale(1.3); /* Safari 3-8 */
  transform: scale(1.3); 
}
</style>