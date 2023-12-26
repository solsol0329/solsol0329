<template>
  <div class="album">
    <div>
      <div class="album-title">앨범제목</div>
      <ul class="song-list">
        <li class="song">노래제목1</li>
        <li class="song">노래제목2</li>
        <li class="song">노래제목3</li>
      </ul> 
    </div>
  </div>
</template>

<script setup>

</script>

<style  scoped>
  .album{
    display: inline-block;
    text-align: center;
    border: 1px solid rgb(185, 177, 177);
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    background-color: #f0e6e6;
    box-shadow: 4px 4px 4px rgb(185, 177, 177);
  }
  .song-list {
    list-style: none;
    padding: 0px;
  }
  .album-title {
    font-weight: bold;
  }

  .song {
    color: orangered
  }
</style>