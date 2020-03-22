<template>
  <div>
    <form v-if="!isSubmitted" @submit.prevent="submit" novalidate>
    <div class="alert alert-danger" v-if="isError">
      <p class="mb-0">
        <strong>{{ $t(errorHeader) }}</strong>
      </p>
      <ul class="mb-0 pl-3" v-if="errors.length > 0">
        <li v-for="error in errors" v-bind:key="error.field">
          <span v-if="error.field">{{ $t('form.'+error.field) }}<span v-if="error.message">: {{ $t(error.message) }}</span></span>
          <span v-else-if="error.message">{{ $t(error.message) }}</span>
        </li>
      </ul>
    </div>
    <div class="form-group">
      <button type="submit" class="btn btn-primary" :disabled="submitting">
        <span v-if="submitting">{{ $t('form.submitting' ) }} <img src="../../assets/loader.svg" /></span>
        <span v-else>{{ $t('form.submit' ) }}</span>
      </button>
    </div>
      <div class="form-group">
        <label for="type">{{ $t('form.type') }} *</label>
        <select id="type" class="form-control" v-model="form.type" @blur="onFieldBlur('type')" v-bind:class="getFieldClasses('type')">
            <option v-for="type in types" v-bind:key="type.value" v-bind:value="type.value">{{ $t(type.label) }}</option>
        </select>
        <div v-if="isErrorField('type')" class="invalid-feedback">{{ $t('form.type') }}</div>
      </div>
      <div class="form-group">
        <label for="className1">{{ $t('form.className1') }} *</label>
        <input type="text" class="form-control" id="className1" v-model.lazy.trim="form.className1" @blur="onFieldBlur('className1')" v-bind:class="getFieldClasses('className1')">
        <div v-if="isErrorField('className1')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className1') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className2">{{ $t('form.className2') }} </label>
        <input type="text" class="form-control" id="className2" v-model.lazy.trim="form.className2" @blur="onFieldBlur('v')" v-bind:class="getFieldClasses('className2')">
        <div v-if="isErrorField('className2')" class="invalid-feedback"></div>
      </div>
      <div class="form-group">
        <label for="className3">{{ $t('form.className3') }} </label>
        <input type="text" class="form-control" id="className3" v-model.lazy.trim="form.className3" @blur="onFieldBlur('className3')" v-bind:class="getFieldClasses('className3')">
        <div v-if="isErrorField('className3')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className3') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className4">{{ $t('form.className4') }} </label>
        <input type="text" class="form-control" id="className4" v-model.lazy.trim="form.className4" @blur="onFieldBlur('className4')" v-bind:class="getFieldClasses('className4')">
        <div v-if="isErrorField('className4')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className4') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className5">{{ $t('form.className5') }} </label>
        <input type="text" class="form-control" id="className5" v-model.lazy.trim="form.className5" @blur="onFieldBlur('className5')" v-bind:class="getFieldClasses('className5')">
        <div v-if="isErrorField('className5')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className5') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className6">{{ $t('form.className6') }} </label>
        <input type="text" class="form-control" id="className6" v-model.lazy.trim="form.className6" @blur="onFieldBlur('className6')" v-bind:class="getFieldClasses('className6')">
        <div v-if="isErrorField('className6')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className6') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className7">{{ $t('form.className7') }} </label>
        <input type="text" class="form-control" id="className7" v-model.lazy.trim="form.className7" @blur="onFieldBlur('className7')" v-bind:class="getFieldClasses('className7')">
        <div v-if="isErrorField('className7')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className7') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className8">{{ $t('form.className8') }} </label>
        <input type="text" class="form-control" id="className8" v-model.lazy.trim="form.className8" @blur="onFieldBlur('className8')" v-bind:class="getFieldClasses('className8')">
        <div v-if="isErrorField('className8')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className8') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className9">{{ $t('form.className9') }} </label>
        <input type="text" class="form-control" id="className" v-model.lazy.trim="form.className9" @blur="onFieldBlur('className9')" v-bind:class="getFieldClasses('className9')">
        <div v-if="isErrorField('className9')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className9') }) }}</div>
      </div>
      <div class="form-group">
        <label for="className10">{{ $t('form.className10') }} </label>
        <input type="text" class="form-control" id="className" v-model.lazy.trim="form.className10" @blur="onFieldBlur('className10')" v-bind:class="getFieldClasses('className10')">
        <div v-if="isErrorField('className10')" class="invalid-feedback">{{ $t('error.fieldRequired', { field: $t('form.className10') }) }}</div>
      </div>
    </form>
    <div v-else>
      <div class="alert alert-success">
        <strong>{{ $t('form.submitted' ) }}</strong>
      </div>
      <div class="alert alert-info">
        <p><strong>{{ $t('form.sentInfo' ) }}</strong></p>
        <pre>
            {{form}}
        </pre>
      </div>
      </div>
      <p class="text-center">
        <a href="#" class="btn btn-secondary" @click.prevent="reload()">{{ $t('form.return' ) }}</a>
      </p>
    </div>
  </div>
</template>

<script src="./Form.js"></script>
<style src="./Form.scss" lang="scss" scoped></style>
