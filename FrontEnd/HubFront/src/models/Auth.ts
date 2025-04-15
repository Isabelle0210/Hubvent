
//os types eu faço com base com o que a api me retorna e o que eu envio para a api, posso olhar os serializer e as views da api para ver o que eu envio e o que eu recebo

export type User = {
     name: string;
     email: string;
     password: string;
}

export type ApiGetUser = {
     user: User;
}

export type SignInRequest = { // esse é o que eu envio para a api
     email: string;
     password: string;
}

export type SignUpRequest = { // esse é o que eu envio para a api
     name: string;
     email: string;
     password: string;
}


export type ApiSignIn = { // esse é o que eu recebo da api
     user: User;
     refresh: string;
     access: string;
}

