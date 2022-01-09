<template>
  <div>
    <FlashMessage :position="'left top'"/>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@font-face {
  font-family: "AncientModernTales";
  src: url('/fonts/AncientModernTales.otf') format('truetype');
}
</style>
