<template>
  <div>
    <b-button pill variant="outline-primary" style="position: absolute;left:3%;top: 5%;" v-b-toggle.sidebar-variant>Menú</b-button>
    <b-sidebar id="sidebar-variant" title="Menú" bg-variant="light" text-variant="blue" backdrop shadow>
      <template #default="{ hide }">
      <div class="px-3 py-2">
        <nav class="mb-3">
            <b-nav vertical>
              <b-nav-item href="/" @click="hide">
                <b-icon icon="house" aria-hidden="true"></b-icon> Inicio
              </b-nav-item>
              <b-nav-item href="administrar_usuarios" @click="hide">
                <b-icon icon="file-person" aria-hidden="true"></b-icon> Administrar Usuarios
              </b-nav-item>
              <b-nav-item href="tweets" @click="hide">
                <b-icon icon="twitter" aria-hidden="true"></b-icon> Tweets
              </b-nav-item>
              <b-nav-item href="buscar_tweets" @click="hide">
                <b-icon icon="search" aria-hidden="true"></b-icon> Búsqueda de tweets
              </b-nav-item>
              <b-nav-item href="estadisticas" @click="hide">
                <b-icon icon="graph-up" aria-hidden="true"></b-icon> Revisar estadísticas
              </b-nav-item>
            </b-nav>
          </nav>
        <b-img src="https://cdn.discordapp.com/attachments/823595523097100348/850257330041257984/laptweet.png" fluid thumbnail></b-img>
      </div>
      </template>
    </b-sidebar>
  </div>
</template>