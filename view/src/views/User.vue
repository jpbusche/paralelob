<template>
  <div>
    <header-component />
    <div>
      <h2 class="add-header">Cadastrar Usuário:</h2>
      <div class='form-field'>
        <span class='span-text'><b>Nome: </b></span>
        <input class='add-input' type='text' v-model='username'>
      </div>
      <div class='form-field'>
        <span class='span-text'><b>Senha: </b></span>
        <input class='add-input' type='password' v-model='password'>
      </div>
      <button class='add-button' type='submit' v-on:click='addUser'>Cadastrar</button>
      <button class='cancel-button' type='submit' v-on:click='cancel'>Cancelar</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import HeaderComponent from '@/components/Header.vue'

export default {
  name: 'User',
  components: {HeaderComponent},
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    cancel() {
      this.$router.push(`/index`);
    },
    addUser() {
      var self = this
      axios.post('http://localhost:5000/create_user', this.mountPayload(), self.$store.state.config)
      .then(response => {
        self.flashMessage.success({
          message:  'Usuário criado com sucesso'
        })
        self.$router.push(`/index`)
      })
      .catch(error => {
        var data = error.response.data
        if (self.containsKey(data, 'message')) {
          self.flashMessage.error({
            message: data['message']
          })
        }
        else {
          self.flashMessage.error({
            message: 'Campo nome e senha não podem ser vazios!'
          })
        }
      })
    },
    mountPayload() {
      var payload = {}
      if (this.username) {
        payload['username'] = this.username
      }
      if (this.password) {
        payload['password'] = this.password
      }
      return payload
    },
    containsKey(obj, key ) {
      return Object.keys(obj).includes(key);
    }
  }
}
</script>