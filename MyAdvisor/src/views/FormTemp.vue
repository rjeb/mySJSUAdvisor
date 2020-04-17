<template>

    <v-container fill-height grid-list-md text-xs-center>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 >
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Classes Form</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form ref="form" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name1" label="Name" v-model="name1" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number1" label="Number" v-model="number1" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="primary"
                            @click="submit"
                            data-cy="joinSubmitBtn"
                            >Submit</v-btn
                        >
                    </v-card-actions>
                    
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>

</template>

<script>
import axios from 'axios';

export default {
    name: 'Form',
    data() {
        return {
            valid: false,
            email: '',
            password: ''

        };
    },
    methods: {
        submit() {
        	//const data = JSON.stringify({name: this.name1, number: this.number1});
            //localStorage.setItem('todos', data);
            //console.log(data);
	        //this.$refs.form.reset();
            //window.alert(data);

            
        }
    }
};
</script>

<style scoped></style>
