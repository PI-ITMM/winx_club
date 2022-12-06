<template>
  <main class="friends section">
    <div class="container friends__container">
      <div class="friends__wrapper">
        <router-link to="/profile">
          <button class="friends__button">
            {{ name }}
          </button>
        </router-link>
      </div>

      <form class="friends__form">
        <fieldset class="friends__fieldset">
          <select class="friends__select" v-model="field">
            <option disabled value="">Выбери фильтр</option>
            <option v-for="option in options" :value="option.value" :key="option">{{ option.text }}</option>
          </select>

          <input class="friends__input" type="text" v-model="parameter">
        </fieldset>
      </form>

      <ul class="friends__cards">
        <li class="friends__card" v-for="friend in friends" :key="friend.login">
          <p class="friends__name">{{ friend.name }}</p>
          <ul class="friends__friend-profile">
            <li class="friends__friend-item" v-for="item in friend" :key="item.value">
              {{ item }}
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </main>
</template>

<script>
import users from './users.json'
export default {
  name: 'FriendsView',
  data () {
    return {
      name: 'тут будет имя',
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
          value: 'favorite_food',
          text: 'любимая еда'
        },
        {
          value: 'hobby',
          text: 'хобби'
        },
        {
          value: 'zodiac_sign',
          text: 'знак зодиака'
        },
        {
          value: 'favorite_season',
          text: 'любимое время года'
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
          value: 'loved_on',
          text: 'имя любимого-или любимой'
        },
        {
          value: 'pet',
          text: 'любимый питомец'
        },
        {
          value: 'favorite_color',
          text: 'любимый цвет'
        },
        {
          value: 'favorite_flower',
          text: 'любимые цветы'
        },
        {
          value: 'favorite_quote',
          text: 'любимая цитата'
        },
        {
          value: 'perfect_date',
          text: 'мое лучшее свидание'
        }
      ],
      parameter: '',
      friends: users
      // .find(user => user.name === 'Алена11111')
    }
  }
}
</script>
