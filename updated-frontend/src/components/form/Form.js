import { required, email, maxLength } from 'vuelidate/lib/validators';
import axios from 'axios';
import Vue from 'vue';

export default {
  name: 'app-form',
  data() {
    return {
      isSubmitted: false,
      isError: false,
      errorHeader: 'error.invalidFields',
      errors: [],
      types: this.getTypes(),
      depts: this.getDepts(),
      submitting: false,
      form: {
        className1: null,
        classNumber1: '',
        className2: null,
        classNumber2: '',
        className3: null,
        classNumber3: '',
        className4: null,
        classNumber4: '',
        className5: null,
        classNumber5: '',
        className6: null,
        classNumber6: '',
        className7: null,
        classNumber7: '',
        className8: null,
        classNumber8: '',
        className9: null,
        classNumber9: '',
        className10: null,
        classNumber10: '',
        type: null
      }
    }
  },
  methods: {
    getDepts() {
      return [
        {
          value: 'CS',
          label: 'form.types.CS'
        }, {
          value: 'MATH',
          label: 'form.types.MATH'
        }];
    },
    submit() {
      this.$v.$touch();
      if (!this.$v.$error) {
        this.sendFormData();
      } else {
        this.validationError();
      }
    },
    enableSubmitLoader() {
      this.submitting = true;
    },
    disableSubmitLoader() {
      this.submitting = false;
    },
    sendFormData() {
      this.enableSubmitLoader();
      axios.post(Vue.config.formApiUrl, this.form).then(response => {
        this.submitSuccess(response);
        this.disableSubmitLoader();
      }).catch(error => {
        this.submitError(error);
        this.disableSubmitLoader();
      });
    },
    submitSuccess(response) {
      if (response.data.success) {
        this.isSubmitted = true;
        this.isError = false;
      } else {
        this.errorHeader = 'error.invalidFields';
        this.errors = response.data.errors;
        this.isError = true;
      }
    },
    submitError(error) {
      this.errorHeader = 'error.general';
      this.errors = [{'field': null, 'message': 'error.generalMessage'}];
      this.isError = true;
    },
    validationError() {
      this.errorHeader = 'error.invalidFields';
      this.errors = this.getErrors();
      this.isError = true;
    },
    isErrorField(field) {
      try {
        if (this.getValidationField(field).$error) {
          return true;
        }
      } catch (error) {}

      return this.errors.some(el => el.field === field);
    },
    getErrors() {
      let errors = [];
      for (const field of Object.keys(this.form)) {
        try {
          if (this.getValidationField(field).$error) {
            errors.push({'field': field, 'message': null});
          }
        } catch (error) {}
      }
      return errors;
    },
    getFieldClasses(field) {
      return { 'is-invalid': this.isErrorField(field) }
    },
    getCharactersLeft(field) {
      try {
        return this.getValidationField(field).$params.maxLength.max - this.form[field].length;
      } catch (error) {
        return 0;
      }
    },
    getTypes() {
      return [
        {
          value: 'fall',
          label: 'form.types.fall'
        }, {
          value: 'spring',
          label: 'form.types.spring'
        }];
    },
    getValidationField(field) {
      if (this.$v.form[field]) {
        return this.$v.form[field];
      }
      throw Error('No validation for field ' + field);
    },
    onFieldBlur(field) {
      try {
        this.getValidationField(field).$touch();
        if (this.getValidationField(field).$error) {
          if (!this.errors.some(el => el.field === field)) {
            this.errors.push({'field': field, 'message': null});
          }
        } else {
          this.errors = this.errors.filter(el => el.field !== field);
        }
      } catch (error) {}
    },
    reload() {
      window.location = '';
    }
  },
  validations: {
    form: {
      classNumber1: { required},
      className1: { required },
      type: { required },
    }
  },
  watch: {
    errors() {
      this.isError = this.errors.length > 0 ? true : false;
    }
  }
}
