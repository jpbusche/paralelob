<template>
  <div>
    <img src="https://i.ibb.co/QY5PrFH/Logo.png" alt="Logo">
    <input class="login-input" placeholder="Usuário" type="text" v-model="username">
    <input class="login-input" placeholder="Senha" type="password" v-model="password">
    <button class="login-button" type="submit" v-on:click="login">Logar</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      var self = this
      var payload = {
        username: self.username,
        password: self.password
      }
      axios.post(`http://localhost:5000/login`, payload)
      .then(response => {
        var data = response.data;
        self.$store.state.is_admin = data['admin']
        self.$store.state.user = data['username']
        self.$store.state.config = {
          headers: {
            Authorization: `Bearer ${data['access_token']}`
          }
        }
        self.flashMessage.success({
          message: 'Login realizado!'
        })
      })
      .catch(error => {
        var response = error.response;
        if (response.status == 401) {
          self.flashMessage.error({
            message: 'Usuário ou senha incorretos!'
          })
        }
      })
    }
  }
}
</script>

<style>
  img {
    margin: 50px 35% 10px;
    width: 500px;
  }
  .login-input {
    font-family: 'AncientModernTales';
    border-radius: 5px;
    border-color: #ebedeb;
    background-color: #d9dbd9;
    height: 35px;
    width: 200px;
    font-size: 30px;
    margin: 10px auto;
    display: block;
  }
  ::placeholder {
    font-style: italic;
    opacity: 0.5;
  }
  .login-button {
    border-radius: 5px;
    border-color: #ebedeb;
    background-color: #d9dbd9;
    display: block;
    margin: 10px auto;
    height: 40px;
    width: 100px;
    font-size: 30px;
    font-family: 'AncientModernTales';
  }
</style>