<template>
    <span>
         <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions0.png?alt=media&token=09ffc1ce-efb7-4893-91bf-14260ffedf80" align="left" v-if='showImage'> 
         <center>
            <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions1.png?alt=media&token=7c018506-ba5b-41b3-b07b-ed5d5568ab91" align="left" v-if='showImage'>
         </center>       
         <center>
            <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions2.png?alt=media&token=c26390e1-634d-40a3-9983-fca1c5ff3b8c" align="middle" v-if='showImage'>
         </center>       
    </span>
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
.images {
 	width: 1440px;
 	height: 375px;
 	overflow: hidden;
}
</style>