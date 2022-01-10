<template>
  <header>
    <img @click="index" :style="logoStyles" src="https://i.ibb.co/R2GjTqR/Logo.png" alt="Logo">
    <span @click="user" v-if="admin" class="header-text">Criar Usuário</span>
    <span v-if="admin" class="header-text">Criar Aventura</span>
    <span class="header-text">Criar Personagem</span>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {
      admin: this.$store.state.is_admin,
    }
  },
  methods: {
    index() {
      this.$router.push(`/index`);
    },
    user() {
      this.$router.push(`/user`);
    }
  },
  computed: {
    logoStyles() {
      if (this.admin) {
        return {
          "margin": "5px 10px",
          "margin-right": "60%"
        }
      }
      return {
        "margin": "5px 10px",
        "margin-right": "80%"
      }
    }
  }
}
</script>

<style>
header {
  background-color: #8c6635;
  height: 60px;
  margin: -10px -10px 10px;
  position: relative;
  display: flex;
}
.header-text {
  font-family: 'AncientModernTales';
  font-size: 30px;
  margin: 20px;
  color: #bfbbbb;
}
.header-text:hover {
  font-size: 32px;
  color: black;
  margin: 18px;
}
</style>