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
            <input class="profile__input" type="text" v-model="name">
          </label>
          <label class="profile__label">
            возраст:
            <input class="profile__input" type="number" v-model="age">
          </label>
          <label class="profile__label">
            цвет волос:
            <input class="profile__input" type="text" v-model="hair_color">
          </label>
          <label class="profile__label">
            цвет глаз:
            <input class="profile__input" type="text" v-model="eye_color">
          </label>
          <label class="profile__label">
            любимая книга:
            <input class="profile__input" type="text" v-model="favorite_book">
          </label>
          <label class="profile__label">
            любимая музыка:
            <input class="profile__input" type="text" v-model="favorite_music">
          </label>
          <label class="profile__label">
            любимая еда:
            <input class="profile__input" type="text" v-model="favorite_food">
          </label>
          <label class="profile__label">
            хобби:
            <input class="profile__input" type="text" v-model="hobby">
          </label>
          <label class="profile__label">
            знак зодиака:
            <input class="profile__input" type="text" v-model="zodiac_sign">
          </label>
          <label class="profile__label">
            любимое время года:
            <input class="profile__input" type="text" v-model="favorite_season">
          </label>
          <label class="profile__label">
            любимый актер:
            <input class="profile__input" type="text" v-model="favorite_actor">
          </label>
          <label class="profile__label">
            любимый напиток:
            <input class="profile__input" type="text" v-model="favorite_drink">
          </label>
          <label class="profile__label">
            имя любимого-или любимой:
            <input class="profile__input" type="text" v-model="loved_on">
          </label>
          <label class="profile__label">
            любимый питомец:
            <input class="profile__input" type="text" v-model="pet">
          </label>
          <label class="profile__label">
            любимый цвет:
            <input class="profile__input" type="text" v-model="favorite_color">
          </label>
          <label class="profile__label">
            любимые цветы:
            <input class="profile__input" type="text" v-model="favorite_flower">
          </label>
          <label class="profile__label">
            любимая цитата:
            <textarea class="profile__textarea" v-model="favorite_quote"></textarea>
          </label>
          <label class="profile__label">
            мое лучшее свидание:
            <textarea class="profile__textarea" v-model="perfect_date"></textarea>
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
  data () {
    return {
      name: 'Алена',
      age: '16',
      hair_color: 'Блонд',
      eye_color: 'Зеленый',
      favorite_book: 'Гарри Поттер',
      favorite_music: 'Техно',
      favorite_food: 'Суши',
      hobby: 'Чтение',
      zodiac_sign: 'Стрелец',
      favorite_season: 'Весна',
      favorite_actor: 'Майкл Мэдсен',
      favorite_drink: 'Зеленый чай',
      loved_on: 'Не скажу!!',
      pet: 'Кошка Китти',
      favorite_color: 'Желтый',
      favorite_flower: 'Ромашка',
      favorite_quote: 'Волк не тот, кто волк, а тот, кто волк...',
      perfect_date: 'В небольшом кафе вечером, с цветами и маленькими подарками'
    }
  }
}
</script>
