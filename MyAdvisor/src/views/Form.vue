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
                            <v-text-field name="dept1" label="Department" v-model="dept1" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number1" label="Number" v-model="number1" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form2" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="dept2" label="Department" v-model="dept2" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number2" label="Number" v-model="number2" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form3" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="dept3" label="Department" v-model="dept3" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number3" label="Number" v-model="number3" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form4" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="dept4" label="Department" v-model="dept4" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number4" label="Number" v-model="number4" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form5" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="dept5" label="Department" v-model="dept5" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number5" label="Number" v-model="number5" required>
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
import firebase from 'firebase';

export default {
    name: 'Form',
    data() {
        return {
            valid: false,
            dept1: '',
            number1: '',
            dept2: '',
            number2: '',
            dept3: '',
            number3: '',
            dept4: '',
            number4: '',
            dept5: '',
            number5: ''
        };
    },
    methods: {
        submit() {
            const data = JSON.stringify({dept1:this.dept1,number1:this.number1,dept2:this.dept2,number2:this.number2,dept3:this.dept3,number3:this.number3,dept4:this.dept4,number4:this.number4,dept5:this.dept5,number5:this.number5});
            localStorage.setItem('news', data);
            this.$refs.form.reset();
            this.$refs.form2.reset();
            this.$refs.form3.reset();
            this.$refs.form4.reset();
            this.$refs.form5.reset();
            window.alert(data);
            firebase
                .database()
                .ref('Classes')
                .push(data);
            
            console.log("Uploaded to FB");
        }
    }
};
</script>

<style scoped></style>
