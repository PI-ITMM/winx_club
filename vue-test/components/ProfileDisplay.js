app.component('profile-display', {
  template: 
  /*html*/
  `<div class="profile-display">
    <div class="profile-container">
      <div class="profile-image">
        <img v-bind:src="image">
      </div>
      <div class="profile-info">
        <h1>Привет! Меня зовут {{ name }}</h1>
        <p class="status-text">&laquo;{{ status }}&raquo;</p>
        <h3>Люблю:</h3>
        <ul class="likes-list">
          <li v-for="like in likes">{{ like }}</li>
        </ul>
        <h3>Не люблю:</h3>
        <ul class="dislikes-list">
          <li v-for="dislike in dislikes">{{ dislike }}</li>
        </ul>
      </div>
      <div class="like-area">
        <span class="hearts">{{ hearts }}</span>
        <button class="button" @click="addLike">&#x1F9E1;</button>
      </div>
    </div>
  </div>`,
  data() {
    return {
        name: 'Алена',
        image: './assets/images/profile-image_kitten.jpg',
        status: 'Добро пожаловать в мою анкету :))) Поставь сердечко, раз уж зашел в гости!',
        likes: ['Музыка', 'Цветы', 'Мама'],
        dislikes: ['Математика', 'Дождь'],
        hearts: 3
    }
  },
  methods: {
    addLike() {
      this.hearts++;
    }
  }
})