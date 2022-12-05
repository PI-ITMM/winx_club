<template>
  <main class="profile section">
    <div class="container">
      <div class="profile__greeting">
        привет, новый друг!<br>
        благодаря нашему ресурсу
        ты сможешь отыскать себе
        собеседников по интересам.
        но вначале заполни
        небольшую анкету
      </div>

      <form class="profile__form">
        <fieldset class="profile__fieldset">
          <label class="profile__label">
            имя:
            <input class="profile__input" type="text" name="name">
          </label>
          <label class="profile__label">
            возраст:
            <input class="profile__input" type="number" name="age">
          </label>
          <label class="profile__label">
            цвет волос:
            <input class="profile__input" type="text" name="hair_color">
          </label>
          <label class="profile__label">
            цвет глаз:
            <input class="profile__input" type="text" name="eye_color">
          </label>
          <label class="profile__label">
            любимая книга:
            <input class="profile__input" type="text" name="favorite_book">
          </label>
          <label class="profile__label">
            любимая музыка:
            <input class="profile__input" type="text" name="favorite_music">
          </label>
          <label class="profile__label">
            любимая еда:
            <input class="profile__input" type="text" name="favorite_food">
          </label>
          <label class="profile__label">
            хобби:
            <input class="profile__input" type="text" name="hobby">
          </label>
          <label class="profile__label">
            знак зодиака:
            <input class="profile__input" type="text" name="zodiac_sign">
          </label>
          <label class="profile__label">
            любимое время года:
            <input class="profile__input" type="text" name="favorite_season">
          </label>
          <label class="profile__label">
            любимый актер:
            <input class="profile__input" type="text" name="favorite_actor">
          </label>
          <label class="profile__label">
            любимый напиток:
            <input class="profile__input" type="text" name="favorite_drink">
          </label>
          <label class="profile__label">
            имя любимого-или любимой:
            <input class="profile__input" type="text" name="loved_on">
          </label>
          <label class="profile__label">
            любимый питомец:
            <input class="profile__input" type="text" name="pet">
          </label>
          <label class="profile__label">
            любимый цвет:
            <input class="profile__input" type="text" name="favorite_color">
          </label>
          <label class="profile__label">
            любимые цветы:
            <input class="profile__input" type="text" name="favorite_flower">
          </label>
          <label class="profile__label">
            любимая цитата:
            <textarea class="profile__textarea" name="favorite_quote"></textarea>
          </label>
          <label class="profile__label">
            мое лучшее свидание:
            <textarea class="profile__textarea" name="perfect_date"></textarea>
          </label>
        </fieldset>
        <router-link to="/friends">
          <button class="button button_submit profile__button" type="button"></button>
        </router-link>
      </form>
    </div>
  </main>
</template>

<script>
export default {
  name: 'ProfileView',
  components: {}
}
</script>
