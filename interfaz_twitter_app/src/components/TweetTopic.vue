<script>
export default{    
    data(){ 
        return {
            fields: ['topic', 'user_id'],
            fields_tweets: ['tweet', 'puntaje', 'calificacion', 'twitter_username', 'twitter_user_location', 'hashtags', 'user_id'],
            tweets:[],
            newTopic:{},
            show: true,
            dismissSecs: 12,
            dismissCountDown: 0,
            mostrar_data: false,
            showDismissibleAlert: false
        }
    },
    methods:{
        search(e){
            e.preventDefault();
            this.$http.post ("http://127.0.0.1:5000/search_by_topic", this.newTopic)
                .then(res => {
                console.log(res.body);
                if(res.body){
                    this.showAlert();
                    this.mostrar_tweets(res.body);
                }
            });
        },
        onReset(event) {
            event.preventDefault()
            // Reset our form values
            this.newTopic.topic = ''
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        },
        mostrar_tweets(rbody){
            this.tweets = rbody
            this.mostrar_data = true
        },
        countDownChanged(dismissCountDown) {
            this.dismissCountDown = dismissCountDown
        },
        showAlert() {
            this.dismissCountDown = this.dismissSecs
        }
    },
}
</script>

<template>
<div class='topics'>
    <h2>Buscar tweets por tema:</h2>

    <b-alert
      :show="dismissCountDown"
      dismissible
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
    >
      Felicidades 😊 encontraste los siguientes tweets. Este mensaje se autodestruirá en {{ dismissCountDown }} ...
    </b-alert>

    <ul>
        <b-table v-if="mostrar_data" striped hover :items="tweets" :fields="fields_tweets"></b-table>
    </ul>



    

    <b-form @submit='search' @reset="onReset" v-if="show">
        <b-form-input
            type='text' 
            v-model='newTopic.topic'
            placeholder='Tema'
            required
        ></b-form-input><br>

        <b-form-input
          type='text' 
          v-model='newTopic.user_id' 
          placeholder='Usuario'
          required
        ></b-form-input><br>

      <b-button type="submit" variant="primary"><b-icon icon="search" aria-hidden="true"></b-icon> Buscar</b-button>
      <b-button type="reset" variant="danger">Limpiar</b-button>
    </b-form>
  </div>
</template>