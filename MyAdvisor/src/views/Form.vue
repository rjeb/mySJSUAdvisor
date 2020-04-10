<template>
    <v-container fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Join Form</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form ref="form" v-model="valid" lazy-validation>
                            <v-text-field name="email" label="Email" type="email" v-model="email" required>
                            </v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="primary"
                            @click="submit"
                            data-cy="joinSubmitBtn"
                            >Join</v-btn
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
        };
    },
    methods: {
        submit() {
        	let formData = { name: this.email}
            console.log(formData);
	        console.log(this.email);
	        axios.post('http://localhost:8081/form', formData)
			    .then(function (response) {
			       console.log(response);
			    })
			    .catch(function (error) {
			       console.log(error);
			});
	        this.$refs.form.reset();
        }        
    }
};
</script>

<style scoped></style>
