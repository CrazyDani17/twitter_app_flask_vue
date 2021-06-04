<script>
export default{    
    data(){ 
        return {
            fields: ['tweet', 'puntaje', 'calificacion', 'twitter_username', 'twitter_user_location', 'hashtags', 'user_id',{ key: 'actions', label: 'Acciones' }],
            tweets:[],
            newTweet:{}
        }
    },
    methods:{
        addTweet(e){
            e.preventDefault();
            this.tweets.push(this.newTweet);
            this.newTweet = {};
        },
        deleteTweet(tweet){
            this.tweets.splice(this.tweets.indexOf(tweet),1);
            this.$http.post ("http://127.0.0.1:5000/delete_tweet/"+ tweet["tweet_id"])
                .then(res => {
                console.log(res.body);
            });
        }
    },
    created(){ // call when component is created
		this.$http.get ('http://127.0.0.1:5000/tweets')
		.then(res => this.tweets = res.body);
	}
}
</script>

<template>
<div class='tweets'>
<b-button pill variant="outline-primary" style="position: absolute;left:91%;top: 35%;" href="historial"> Historial </b-button>
<ul>
<b-table striped hover :items="tweets" :fields="fields">
    <template #cell(actions)="tweet">
        <div>
        <b-dropdown variant="primary">
        <template #button-content>
            <b-icon icon="gear-fill" aria-hidden="true"></b-icon> Ajustes
        </template>
        <b-dropdown-item-button>
            <b-icon icon="pencil-square" aria-hidden="true"></b-icon>
            Editar
        </b-dropdown-item-button>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item-button variant="danger">
            <b-icon icon="trash-fill" aria-hidden="true" @click="deleteTweet(tweet.item)"></b-icon>
            Eliminar
        </b-dropdown-item-button>
        </b-dropdown>
    </div>
    </template>
</b-table>
</ul>
</div>
</template>