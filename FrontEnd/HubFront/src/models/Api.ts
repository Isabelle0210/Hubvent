
//Ele serve pra tipar erros vindos de uma API, ou seja, dizer qual é a estrutura esperada de um objeto de erro.
export type ApiError ={
     detail: string;
     code?: string;
}