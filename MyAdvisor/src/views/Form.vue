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
                            <v-select
                              v-model="type"
                              :items="types"
                              menu-props="auto"
                              label="Semester"
                              hide-details
                              single-line
                            ></v-select>
                          </v-flex>
                          </v-layout>
                        </v-form>

                        <v-form ref="form1" v-model="valid" lazy-validation>
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
                    <v-btn
                        color="primary"
                        @click="submit"
                        data-cy="joinSubmitBtn"
                        >Submit</v-btn
                    >
                    <center>
                        <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions0.png?alt=media&token=09ffc1ce-efb7-4893-91bf-14260ffedf80" align="middle" v-if='showImage'> 
                    </center> 
                    <center>
                        <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions1.png?alt=media&token=7c018506-ba5b-41b3-b07b-ed5d5568ab91" align="middle" v-if='showImage'>
                    </center>       
                    <center>
                        <img class="images" src="https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions2.png?alt=media&token=c26390e1-634d-40a3-9983-fca1c5ff3b8c" align="middle" v-if='showImage'>
                    </center>       
                    <v-btn
                        color="primary"
                        to="/schedules"
                        data-cy="formBtn"
                        >See YOUR SCHEDULE</v-btn
                    >             
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
            types: ['Fall', 'Spring'],
            url : '',
            showImage: false,
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
                classNumber5: '',
                type: null
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
            this.classes.type = this.type;
            this.$refs.form.reset();
            this.$refs.form1.reset();
            this.$refs.form2.reset();
            this.$refs.form3.reset();
            this.$refs.form4.reset();
            this.$refs.form5.reset();
            window.alert("Done");
            firebase
                .database()
                .ref('Classes')
                .child('classargs')
                .set(this.classes);
       },
       recieve() {
       /*
            var storage = firebase.storage();
            var storageRef =  storage.ref();
            storageRef.child('Schedules/').listAll().then(function(result){
                result.items.forEach(function(imageRef){
                    imageRef.getDownloadURL().then(function(url){
                    });
                });
            });
        */
            //window.alert(this.imageURL); 
            this.showImage = !this.showImage;
       },
       showPhoto() {
            const imgUrl = 'https://firebasestorage.googleapis.com/v0/b/advisor-c0b7d.appspot.com/o/Schedules%2Fsolutions0.png?alt=media&token=09ffc1ce-efb7-4893-91bf-14260ffedf80';
            return imgUrl;
       }
    }
};
</script>

<style scoped>
.images {
    width: 100%;
}
</style>