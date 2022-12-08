<template>
  <article class="login section">
    <div class="container">
      <form class="login__form">
        <fieldset class="login__fieldset">
          <label class="login__label">
            login
            <input class="login__input" type="text" required v-model="login">
          </label>
          <label class="login__label">
            password
            <input class="login__input" type="password" required v-model="password">
          </label>
        </fieldset>
        <router-link to="/profile">
          <button class="button button_submit login__button" type="button"></button>
        </router-link>
      </form>
    </div>
  </article>
</template>

<script>
export default {
  name: 'LoginView',
  data () {
    return {
      login: 'test',
      password: 'test'
    }
  }
}
</script>
