<script>
export default{    
    data(){ 
        return {
            fields: ['auditoria_id', 'accion', 'fecha', 'tweet_id','user_id'],
            auditorias:[],
            newAuditoria:{}
        }
    },
    created(){ // call when component is created
		this.$http.get ('http://127.0.0.1:5000/auditorias')
		.then(res => this.auditorias = res.body);
	}
}
</script>

<template>
<div class='auditorias'>    
<ul>
<b-table striped hover :items="auditorias" :fields="fields">
</b-table>
</ul>
</div>
</template>