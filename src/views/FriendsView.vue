<template>
  <main class="friends section">
    <div class="container friends__container">
      <div class="friends__wrapper">
        <router-link to="/profile">
          <button class="friends__button">
            имя фамилия
          </button>
        </router-link>
      </div>

      <form class="friends__form">
        <fieldset class="friends__fieldset">
          <select class="friends__select" name="field">
            <option value="field1">поле 1</option>
            <option value="field2">поле 2</option>
          </select>

          <input class="friends__input" type="text">
        </fieldset>
      </form>

      <div class="friends__cards">
        <div class="friends__card">анкета 1</div>
        <div class="friends__card">анкета 11</div>
        <div class="friends__card">анкета 111</div>
        <div class="friends__card">анкета 1111</div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'FriendsView',
  components: {}
}
</script>
