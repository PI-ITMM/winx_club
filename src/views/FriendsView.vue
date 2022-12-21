<template>
  <main class="friends section">
    <div class="container friends__container">
      <div class="friends__wrapper">
        <router-link to="/user">
          <button class="friends__button">
            Моя анкета
          </button>
        </router-link>
      </div>

      <form class="friends__form">
        <fieldset class="friends__fieldset">
          <select class="friends__select" v-model="field" @change="(e) => (choiceField = e.target.value)">
            <option disabled value="">Выбери фильтр</option>
            <option v-for="option in options" :value="option.value" :key="option">{{ option.text }}</option>
          </select>

          <input class="friends__input" type="text" v-model="parameter"
          @input="(e) => (choiceValue = e.target.value)"
          >
        </fieldset>
      </form>

      <button class="friends__button" @click="searchingProfiles()">
            Искать
      </button>

      <ul class>
        <li v-for="friend in friends" :key="friend.id">
          <ul class="friends__cards">
          <li class="friends__card" v-for="f in friend" :key="f.value">
            <p class="friends__name">{{ f.name }}</p>
            <ul class="friends__friend-profile">
              <li class="friends__friend-item">
                Возраст : {{ f.age }}
              </li>
              <li class="friends__friend-item">
                Цвет волос : {{ f.hair_color }}
              </li>
              <li class="friends__friend-item">
                Цвет глаз : {{ f.eye_color }}
              </li>
              <li class="friends__friend-item">
                Любимая книга : {{ f.favorite_book }}
              </li>
              <li class="friends__friend-item">
                Любимая музыка : {{ f.favorite_music }}
              </li>
              <li class="friends__friend-item">
                Любимая цитата : {{ f.favorite_quote }}
              </li>
              <li class="friends__friend-item">
                Любимая еда : {{ f.favorite_food }}
              </li>
              <li class="friends__friend-item">
                Любимый цвет : {{ f.favorite_color }}
              </li>
              <li class="friends__friend-item">
                Хобби : {{ f.hobby }}
              </li>
              <li class="friends__friend-item">
                Животные : {{ f.pets }}
              </li>
              <li class="friends__friend-item">
                Любимые цветы : {{ f.favorite_flowers }}
              </li>
              <li class="friends__friend-item">
                Знак зодиака : {{ f.zodiac_sign }}
              </li>
              <li class="friends__friend-item">
                Моя мечта : {{ f.dream }}
              </li>
              <li class="friends__friend-item">
                Любимое время года : {{ f.favorite_season }}
              </li>
              <li class="friends__friend-item">
                Любимое время года : {{ f.favorite_season }}
              </li>
              <li class="friends__friend-item">
                Мое лучшее свидание : {{ f.perfect_date }}
              </li>
              <li class="friends__friend-item">
                Любимый актер : {{ f.favorite_actor }}
              </li>
              <li class="friends__friend-item">
                Любимый напиток : {{ f.favorite_drink }}
              </li>
              <li class="friends__friend-item">
                Имя любимого-или любимой : {{ f.loved_one }}
              </li>
              <li class="friends__friend-item">
                Мои контакты : {{ f.contacts }}
              </li>
            </ul>
          </li>
        </ul>
        </li>
      </ul>
    </div>
  </main>
</template>

<script>
// import users from './users.json'
import { getProfiles } from '../../api/vue/api'

export default {
  /* eslint-disable */
  name: 'FriendsView',
  data () {
    return {
      choiceValue: '',
      choiceField: 'age',
      field: '',
      
      options: [
        {
          value: 'name',
          text: 'имя'
        },
        {
          value: 'age',
          text: 'возраст'
        },
        {
          value: 'hair_color',
          text: 'цвет волос'
        },
        {
          value: 'eye_color',
          text: 'цвет глаз'
        },
        {
          value: 'favorite_book',
          text: 'любимая книга'
        },
        {
          value: 'favorite_music',
          text: 'любимая музыка'
        },
        {
          value: 'favorite_quote',
          text: 'любимая цитата'
        },
        {
          value: 'favorite_food',
          text: 'любимая еда'
        },
        {
          value: 'favorite_color',
          text: 'любимый цвет'
        },
        {
          value: 'hobby',
          text: 'хобби'
        },
        {
          value: 'pets',
          text: 'любимый питомец'
        },
        {
          value: 'favorite_flowers',
          text: 'любимые цветы'
        },
        {
          value: 'zodiac_sign',
          text: 'знак зодиака'
        },
        {
          value: 'dream',
          text: 'моя мечта'
        },
        {
          value: 'favorite_season',
          text: 'любимое время года'
        },
        {
          value: 'perfect_date',
          text: 'мое лучшее свидание'
        },
        {
          value: 'favorite_actor',
          text: 'любимый актер'
        },
        {
          value: 'favorite_drink',
          text: 'любимый напиток'
        },
        {
          value: 'loved_one',
          text: 'имя любимого-или любимой'
        },
        {
          value: 'contacts',
          text: 'мои контакты'
        }
      ],
      parameter: '',
      friends: []
    }
  },

  mounted() {
    getProfiles(
        '',
        '',
        (data) => {
          this.friends = data
        },
        (error) => {
          this.error = error.response.data.errorMessage
        }
      )
  },

  methods: {
    searchingProfiles() {
      getProfiles(
        this.choiceField,
        this.choiceValue,
        (data) => {
          this.friends = data
        },
        (error) => {
          this.error = error.response.data.errorMessage
        }
      )
    }
  }
}
</script>
