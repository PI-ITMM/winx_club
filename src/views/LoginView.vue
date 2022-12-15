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
          <button class="button button_submit login__button" type="button" @click="signUp()"></button>
      </form>
    </div>
    <p class="text-sm mt-4 font-medium leading-none text-gray-500">
              У вас ещё нет анкеты?
              <button
              class="hover:text-indigo-700 text-sm font-medium leading-none underline text-gray-800 cursor-pointer"
              type="button"
              @click="signUp()"
              >
              Зарегистрируйтесь здесь
            </button>
            </p>
  </article>
</template>

<script>
/* eslint-disable */
//import { doLogin } from '../../api/vue/api'
import router from '../router'

export default {
  name: 'LoginView',
  data () {
    return {
      username: 'test',
      password: 'test',
      user: {
        id: 0,
        name: 'Алена',
        password:'test',
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
    signUp(){
    router.push({ name: "profile"})
    },
    /*login () {
      doLogin(this.username, this.password,
        () => {
          this.user = data;
          router.push({ name: 'friends' })
        },
        (e) => {
          this.error = e.response.data.errorMessage
        }
      )
    }*/
  }
  
}
</script>
