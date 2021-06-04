<script>
export default{    
    data(){ 
        return {
            fields: ['user_name', 'nombre_completo', 'email', 'tipo_de_usuario',{ key: 'actions', label: 'Acciones' }],
            users:[],
            newUser:{}
        }
    },
    methods:{
        addUser(e){
            e.preventDefault();
            this.users.push(this.newUser);
            this.newUser = {};
        },
        deleteUser(user){
            this.users.splice(this.users.indexOf(user),1);
            this.$http.post ("http://127.0.0.1:5000/delete_user/"+ user["user_id"])
                .then(res => {
                console.log(res.body);
            });
        }
    },
    created(){ // call when component is created
		this.$http.get ('http://127.0.0.1:5000/users')
		.then(res => this.users = res.body);
	}
}
</script>

<template>
<div class='users'>
<b-button pill variant="outline-primary" style="position: absolute;left:87%;top: 35%;" href="crear_usuario">Añadir Usuario</b-button>    
<ul>
<b-table striped hover :items="users" :fields="fields">
    <template #cell(actions)="user">
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
            <b-icon icon="trash-fill" aria-hidden="true" @click="deleteUser(user.item)"></b-icon>
            Eliminar
        </b-dropdown-item-button>
        </b-dropdown>
    </div>
    </template>
</b-table>

</ul>
</div>
</template>