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
                            <v-text-field name="className1" label="Department" v-model="className1" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="classNumber1" label="Number" v-model="classNumber1" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                    <v-card-text>
                        <v-form ref="form2" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="className2" label="Department" v-model="className2" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="classNumber2" label="Number" v-model="classNumber2" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form3" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="className3" label="Department" v-model="className3" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="classNumber3" label="Number" v-model="classNumber3" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form4" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="className4" label="Department" v-model="className4" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="classNumber4" label="Number" v-model="classNumber4" required>
                            </v-text-field>
                            </v-flex>
                          </v-layout>
                        </v-form>

                    </v-card-text>
                      <v-card-text>
                        <v-form ref="form5" v-model="valid" lazy-validation>
                          <v-layout row wrap>
                            <v-flex xs6>
                            <v-text-field name="className5" label="Department" v-model="className5" required>
                            </v-text-field>
                            </v-flex>
                            <v-flex xs6>
                            <v-text-field name="classNumber5" label="Number" v-model="classNumber5" required>
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
import firebase from 'firebase';

export default {
    name: 'Form',
    data() {
        return {
            classes: {
                valid: false,
                className1: '',
                classNumber1: '',
                className2: '',
                classNumber2: '',
                className3: '',
                classNumber3: '',
                className4: '',
                classNumber4: '',
                className5: '',
                classNumber5: ''
            }
        };
    },
    methods: {
        submit() {
            this.classes.className1 = this.className1;
            this.classes.classNumber1 = this.classNumber1;
            this.classes.className2 = this.className2;
            this.classes.classNumber2 = this.classNumber2;
            this.classes.className3 = this.className3;
            this.classes.classNumber3 = this.classNumber3;
            this.classes.className4 = this.className4;
            this.classes.classNumber4 = this.classNumber4;
            this.classes.className5 = this.className5;
            this.classes.classNumber5 = this.classNumber5;
            this.$refs.form.reset();
            this.$refs.form2.reset();
            this.$refs.form3.reset();
            this.$refs.form4.reset();
            this.$refs.form5.reset();
            window.alert("Done");
            firebase
                .database()
                .ref('Classes')
                .push(this.classes);
       }
    }
};
</script>

<style scoped></style>
