<script>
export default{    
    data(){ 
        return {
            fields: ['user_name', 'nombre_completo', 'email', 'tipo_de_usuario'],
            users:[],
            newUser:{},
            show: true,
            dismissSecs: 12,
            dismissCountDown: 0,
            showDismissibleAlert: false
        }
    },
    methods:{
        addUser(e){
            e.preventDefault();
            this.$http.post ("http://127.0.0.1:5000/create_user", this.newUser)
                .then(res => {
                console.log(res.body);
                if(res.body){
                    this.showAlert();
                }
            });
        },
        onReset(event) {
            event.preventDefault()
            // Reset our form values
            this.newUser.user_name = ''
            this.newUser.password = ''
            this.newUser.nombre_completo= ''
            this.newUser.email = ''
            this.newUser.tipo_de_usuario = ''
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        },
        countDownChanged(dismissCountDown) {
            this.dismissCountDown = dismissCountDown
        },
        showAlert() {
            this.dismissCountDown = this.dismissSecs
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
    <h2>Crear Usuario</h2>

    <b-alert
      :show="dismissCountDown"
      dismissible
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
    >
      Felicidades 😊 creaste un nuevo usuario. Este mensaje se autodestruirá en {{ dismissCountDown }} ...
    </b-alert>

    <b-form @submit='addUser' @reset="onReset" v-if="show">
        <b-form-input
            type='text' 
            v-model='newUser.user_name'
            placeholder='Username'
            required
        ></b-form-input><br>

        <b-form-input
          type='password' 
          v-model='newUser.password' 
          placeholder='Password'
          required
        ></b-form-input><br>

        <b-form-input
          type='text'
          v-model='newUser.nombre_completo' 
          placeholder='Nombre Completo'
          required
        ></b-form-input><br>

        <b-form-input
          type='email'
          v-model='newUser.email' 
          placeholder='Email'
          required
        ></b-form-input><br>

        <b-form-input
          type='text'
          v-model='newUser.tipo_de_usuario' 
          placeholder='Tipo de Usuario'
          required
        ></b-form-input><br>

      <b-button type="submit" variant="primary">Crear</b-button>
      <b-button type="reset" variant="danger">Limpiar</b-button>
    </b-form>
  </div>
</template>