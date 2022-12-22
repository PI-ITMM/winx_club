<!-- eslint-disable vue/no-mutating-props -->
<template>
  <main class="profile section" @getId="getId">
    <div class="container friends__container">
      <div class="friends__wrapper">
        <router-link to="/friends">
          <button class="friends__button friends__button_top">
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
            <input class="profile__input" type="text" v-model="user.age">
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
            <input class="profile__input" type="text" v-model="user.loved_one">
          </label>
          <label class="profile__label">
            любимый питомец:
            <input class="profile__input" type="text" v-model="user.pets">
          </label>
          <label class="profile__label">
            любимый цвет:
            <input class="profile__input" type="text" v-model="user.favorite_color">
          </label>
          <label class="profile__label">
            любимые цветы:
            <input class="profile__input" type="text" v-model="user.favorite_flowers">
          </label>
          <label class="profile__label">
            любимая цитата:
            <textarea class="profile__textarea" v-model="user.favorite_quote"></textarea>
          </label>
          <label class="profile__label">
            мое лучшее свидание:
            <textarea class="profile__textarea" v-model="user.perfect_date"></textarea>
          </label>
          <label class="profile__label">
            моя мечта:
            <textarea class="profile__textarea" v-model="user.dream"></textarea>
          </label>
          <label class="profile__label">
            мои контакты:
            <textarea class="profile__textarea" v-model="user.contacts"></textarea>
          </label>
        </fieldset>
        <div class="profile__button-group">
          <button class="button button_delete" type="button" @click="deleteThisProfile()"></button>
          <button class="button button_edit" type="button" @click="editingUser()"></button>
        </div>
      </form>
    </div>
  </main>
</template>

<script>
/* eslint-disable */
import { editProfile, deleteProfile, getProfile } from '../../api/vue/api'
import router from '../router'

export default {
  props: {
    id: Number
  },
  name: 'ProfileView',
  data() {
    return {
      user: {
        id: 0,
        name: '',
        age: '',
        hair_color: '',
        eye_color: '',
        favorite_book: '',
        favorite_music: '',
        favorite_quote: '',
        favorite_food: '',
        favorite_color: '',
        hobby: '',
        pets: '',
        favorite_flowers: '',
        zodiac_sign: '',
        dream: '',
        favorite_season: '',
        perfect_date: '',
        favorite_actor: '',
        favorite_drink: '',
        loved_one: '',
        contacts: '',
        password: ''
      },
      editId: '',
      editName: '',
      editAge: '',
      editHairColor: ''
    }
  },

  mounted() {
    getProfile(this.id,
      (data) => {
        this.user = data;
      },
      (error) => {
        this.error = error.message;
      }
    );
  },

  methods: {

    editingUser() {
      editProfile(
        this.user.id, this.user.age, this.user.hair_color, this.user.eye_color,
        this.user.favorite_book, this.user.favorite_music, this.user.favorite_quote,
        this.user.favorite_food, this.user.favorite_color, this.user.hobby, this.user.pets,
        this.user.favorite_flowers, this.user.zodiac_sign, this.user.dream, this.user.favorite_season,
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
  },

}
</script>
