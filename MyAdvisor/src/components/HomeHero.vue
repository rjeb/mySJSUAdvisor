<template>
    <v-container fluid fill-height class="home-hero" style="max-height: 100vh;">
        <v-layout justify-center align-center column pa-5>
            <div class="display-4 font-weight-black pink--text text-xs-center">
                CUSTOMIZING SCHEDULES
            </div>
            <div
                class="display-4 font-weight-black pink--text text-xs-center mb-3"
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
    background: url('https://images.unsplash.com/photo-1502570149819-b2260483d302?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60');
    background-size: cover;
    width: 100%;
    height: 100%;
}
</style>
