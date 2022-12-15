<template>
  <main class="profile section">
    <div class="container friends__container">
      <div class="friends__wrapper">
        <router-link to="/friends">
          <button class="friends__button">
            Смотреть другие анкеты
          </button>
        </router-link>
        </div>

      <form class="profile__form">
        <fieldset class="profile__fieldset">
          <label class="profile__label">
            имя:
            <input class="profile__input" type="text" v-model="user.name">
          </label>
          <label class="profile__label">
            пароль:
            <input class="profile__input" type="text" v-model="user.password">
          </label>
          <label class="profile__label">
            возраст:
            <input class="profile__input" type="number" v-model="user.age">
          </label>
          <label class="profile__label">
            цвет волос:
            <input class="profile__input" type="text" v-model="user.hair_color">
          </label>
          <label class="profile__label">
            цвет глаз:
            <input class="profile__input" type="text" v-model="user.eye_color">
          </label>
          <label class="profile__label">
            любимая книга:
            <input class="profile__input" type="text" v-model="user.favorite_book">
          </label>
          <label class="profile__label">
            любимая музыка:
            <input class="profile__input" type="text" v-model="user.favorite_music">
          </label>
          <label class="profile__label">
            любимая еда:
            <input class="profile__input" type="text" v-model="user.favorite_food">
          </label>
          <label class="profile__label">
            хобби:
            <input class="profile__input" type="text" v-model="user.hobby">
          </label>
          <label class="profile__label">
            знак зодиака:
            <input class="profile__input" type="text" v-model="user.zodiac_sign">
          </label>
          <label class="profile__label">
            любимое время года:
            <input class="profile__input" type="text" v-model="user.favorite_season">
          </label>
          <label class="profile__label">
            любимый актер:
            <input class="profile__input" type="text" v-model="user.favorite_actor">
          </label>
          <label class="profile__label">
            любимый напиток:
            <input class="profile__input" type="text" v-model="user.favorite_drink">
          </label>
          <label class="profile__label">
            имя любимого-или любимой:
            <input class="profile__input" type="text" v-model="user.loved_on">
          </label>
          <label class="profile__label">
            любимый питомец:
            <input class="profile__input" type="text" v-model="user.pet">
          </label>
          <label class="profile__label">
            любимый цвет:
            <input class="profile__input" type="text" v-model="user.favorite_color">
          </label>
          <label class="profile__label">
            любимые цветы:
            <input class="profile__input" type="text" v-model="user.favorite_flower">
          </label>
          <label class="profile__label">
            любимая цитата:
            <textarea class="profile__textarea" v-model="user.favorite_quote"></textarea>
          </label>
          <label class="profile__label">
            мое лучшее свидание:
            <textarea class="profile__textarea" v-model="user.perfect_date"></textarea>
          </label>
        </fieldset>
        <!-- кнопка редактирования -->
          <button class="button button_submit profile__button" type="button" @click="editingUser()"></button>
        <!-- кнопка удаления -->
          <button class="button button_submit profile__button" type="button" @click="deleteThisProfile()"></button>
      </form>
    </div>
  </main>
</template>

<script>
/* eslint-disable */
//import { editProfile, deleteProfile } from '../../api/vue/api'
import router from '../router'

export default {
  name: 'ProfileView',
  data () {
    return {
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

  /*methods: {

    editingUser() {
      editProfile(
      this.user.id, this.user.age, this.user.hair_color, this.user.eye_color,
      this.user.favorite_book, this.user.favorite_music, this.user.favorite_quote,
      this.user.favorite_food, this.user.favorite_color, this.user.hobby, this.user.pets,
      this.user.favorite_flowers,this.user.zodiac_sign, this.user.dream, this.user.favorite_season,
      this.user.perfect_date, this.user.favorite_actor, this.user.favorite_drink, this.user.loved_one,
      this.user.contacts, this.user.password,
        (data) => {
          this.user = data;
        },
        (error) => {
          this.error = error.message;
        }
      );
    },

  deleteThisProfile() {
      deleteProfile(
        this.user.id,
        () => {
        this.user = "";
        router.push({ name: 'profile' })
        },
        (error) => {
          this.error = error.message;
        }
      );
    },
  },*/

}
</script>
