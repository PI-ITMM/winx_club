<template>
  <header class="section header">
    <div class="container header__container">
      <img class="logo" src="./assets/img/logo.png" alt="Логотип сайта">
    </div>
  </header>

  <router-view @getId="getId" v-bind:id="editId"/>

  <footer class="section footer">
    <div class="container">
      by winx club 2022
    </div>
  </footer>
</template>

<script>
export default {
  data () {
    return {
      editId: 0
    }
  },

  methods: {
    getId (id) {
      this.editId = id
    }
  }
}
</script>
