<template>
  <header class="header section">
    <div class="container header__container">
      <img class="logo" src="../public/img/logo.png" alt="Логотип сайта">
    </div>
  </header>

  <router-view />

  <footer class="footer section">
    <div class="container">
      by winx club 2022
    </div>
  </footer>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>
