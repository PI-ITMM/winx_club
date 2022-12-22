/* eslint-disable */ 
import axios from 'axios'
import './axios'


export const doLogin = async (username, password, okCallback, errorCallback) => {
  try {
    const response = await axios.post(`/login/?username=${username}&password=${password}`);
    okCallback(response.data)
  } catch (e) {
    return errorCallback(e);
  }
};

export const getProfiles = async (field, value, okCallback, errorCallback) => {
  try {
    const response = await axios.get(`/profiles/?field=${field}&value=${value}`);
    okCallback(response.data)
  } catch (e) {
    return errorCallback(e)
  }
};

export const getProfile = async (id, okCallback, errorCallback) => {
  try {
    const response = await axios.get(`/profiles/${id}`);
    okCallback(response.data)
  } catch (e) {
    return errorCallback(e)
  }
};


export const createProfile = async (name, age, hair_color, eye_color,
  favorite_book, favorite_music, favorite_quote, favorite_food,favorite_color, hobby,pets,
  favorite_flowers,zodiac_sign, dream, favorite_season,
  perfect_date, favorite_actor, favorite_drink, loved_one,
  contacts, password, okCallback, errorCallback) => {
  try {
    const response = await axios.post(`/profile/`, { name, age, hair_color, eye_color,
      favorite_book, favorite_music, favorite_quote, favorite_food,favorite_color, hobby,pets,
      favorite_flowers,zodiac_sign, dream, favorite_season,
      perfect_date, favorite_actor, favorite_drink, loved_one,
      contacts, password })
    okCallback(response.data)
  } catch (e) {
    return errorCallback(e)
  }
};

export const editProfile = async (id, age, hair_color, eye_color,
  favorite_book, favorite_music, favorite_quote, favorite_food,favorite_color, hobby,pets,
  favorite_flowers,zodiac_sign, dream, favorite_season,
  perfect_date, favorite_actor, favorite_drink, loved_one,
  contacts, password, okCallback, errorCallback) => {
  try {
    const response = await axios.put(`/profile/${id}`,{ age, hair_color, eye_color,
      favorite_book, favorite_music, favorite_quote, favorite_food,favorite_color, hobby,pets,
      favorite_flowers,zodiac_sign, dream, favorite_season,
      perfect_date, favorite_actor, favorite_drink, loved_one,
      contacts, password })
    okCallback(response.data)
  } catch (e) {
    return errorCallback(e)
  }
};

export const deleteProfile = async (id, okCallback, errorCallback) => {
  try {
    await axios.delete(`/profile/${id}`)
    okCallback()
  } catch (e) {
    return errorCallback(e)
  }
};
