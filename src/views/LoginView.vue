<template>
  <article class="login section">
    <div class="container">
      <form class="login__form">
        <fieldset class="login__fieldset">
          <label class="login__label">
            username
            <input class="login__input" type="text" required v-model="username">
          </label>
          <label class="login__label">
            password
            <input class="login__input" type="password" required v-model="password">
          </label>
        </fieldset>
        <button class="button button_submit login__button" type="button" @click="login()"></button>
      </form>
      <div class="login__registration">
        <p class="login__none">Нет анкеты?</p>
        <button class="button_registration" @click="signUp()">Зарегистрируйтесь здесь</button>
      </div>
    </div>
  </article>
</template>

<script>
/* eslint-disable */
import { doLogin } from '../../api/vue/api'
import router from '../router'

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      user: {
        id: 0,
        name: 'Алена',
        password: 'test',
        age: 16,
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
      },
    }
  },

  methods: {
    signUp() {
      router.push({ name: "profile" })
    },
    login() {
      doLogin(this.username, this.password,
        (data) => {
          this.user = data;
          this.$emit('getId', this.user.id)
          router.push({ name: 'friends' })
        },
        (e) => {
          alert("Неверное имя пользователя или пароль");
        }
      )
    }
  }

}
</script>
