<template>
    <v-container fluid fill-height class="home-hero" style="max-height: 100vh;">
        <v-layout justify-center align-center column pa-5>
            <div class="display-4 font-weight-black white--text text-xs-center">
                CUSTOMIZING SCHEDULES
            </div>
            <div
                class="display-4 font-weight-black white--text text-xs-center mb-3"
            >
                FOR YOUR CLASSES
            </div>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'HomeHero'
};
</script>

<style scoped>
.home-hero {
    background: url('https://cpb-us-w2.wpmucdn.com/blogs.sjsu.edu/dist/f/94/files/2015/09/Schmitz_GeneralCampus_7631_1_02-rprer4.jpg');
    background-size: cover;
    width: 100%;
    height: 100%;

    font-family: "Roboto", sans-serif;
}
</style>
