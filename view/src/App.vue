<template>
  <div>
    <FlashMessage :position="'left bottom'"/>
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
.add-button {
  margin: 10px 17px;
  font-family: 'AncientModernTales';
  border-radius: 5px;
  height: 40px;
  width: 120px;
  font-size: 30px;
  border-color: #00ff00;
  background-color: #6dff6d;
  display: inline;
}
.cancel-button {
  margin: 10px 17px;
  font-family: 'AncientModernTales';
  border-radius: 5px;
  height: 40px;
  width: 120px;
  font-size: 30px;
  border-color: #cc0000;
  background-color: #f65757;
  display: inline;
}
.add-header {
  font-family: 'AncientModernTales';
  color: #474747;
  margin: 20px;
  font-size: 40px
}
.form-field {
  margin: 10px 20px;
  display: block;
}
.add-input {
  border-radius: 5px;
  border-color: #ebedeb;
  background-color: #d9dbd9;
  color: #474747;
  height: 35px;
  font-size: 30px;
  width: 200px;
  font-family: 'AncientModernTales';
  display: inline;
}
.span-text {
  margin-top: 20px;
  color: #474747;
  font-family: 'AncientModernTales';
  font-size: 30px;
}
</style>
