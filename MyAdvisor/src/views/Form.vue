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
                            <v-select v-model="dept" :items="depts" label="Department" @input="$v.dept.$touch()" @blur="$v.dept.$touch()">
                            </v-select>
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
                            <v-text-field name="name2" label="Name" v-model="name2" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number2" label="Number" v-model="number2" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form3" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name3" label="Name" v-model="name3" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number3" label="Number" v-model="number3" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form4" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name4" label="Name" v-model="name4" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number4" label="Number" v-model="number4" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form5" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name5" label="Name" v-model="name5" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number5" label="Number" v-model="number5" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form6" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name6" label="Name" v-model="name6" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number6" label="Number" v-model="number6" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form7" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name7" label="Name" v-model="name7" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number7" label="Number" v-model="number7" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form8" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name8" label="Name" v-model="name8" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number8" label="Number" v-model="number8" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form9" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name9" label="Name" v-model="name9" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number9" label="Number" v-model="number9" >
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form10" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="name10" label="Name" v-model="name10" >
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="number10" label="Number" v-model="number10" required>
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
            dept: null,
            number1: '',
            name2: '',
            number2: '',
            name3: '',
            number3: '',
            name4: '',
            number4: '',
            name5: '',
            number5: '',
            name6: '',
            number6: '',
            name7: '',
            number7: '',
            name8: '',
            number8: '',
            name9: '',
            number9: '',
            name10: '',
            number10: '',
            depts: [
                'CS',
                'MATH',
                'ENGLISH',
                'CHEM',
              ],

        };
    },
    methods: {
        submit() {
        	let formData = { dept: this.dept, number1: this.number1, name2: this.name2, number2: this.number2, name3: this.name3, number3: this.number3, name4: this.name4, number4: this.number4, name5: this.name5, number5: this.number5, name6: this.name6, number6: this.number6, name7: this.name7, number7: this.number7, name8: this.name8, number8: this.number8, name9: this.name9, number9: this.number9, name10: this.name10, number10: this.number10};
            let data = {this. dept, this.number1};
	        this.$refs.form.reset();
            this.$refs.form2.reset();
            this.$refs.form3.reset();
            this.$refs.form4.reset();
            this.$refs.form5.reset();
            this.$refs.form6.reset();
            this.$refs.form7.reset();
            this.$refs.form8.reset();
            this.$refs.form9.reset();
            this.$refs.form10.reset();
            //this.$localStorage.set('todos',formdata);
            window.alert("done");
        }
    }
};
</script>

<style scoped></style>
