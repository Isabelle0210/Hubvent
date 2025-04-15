import { User } from "./Auth";
import { Event } from "./Event";

export type Subscription = {
     id: number
     event: Event
     user: User
}

// ✅ Resposta ao se inscrever
export type ApiCreateSubscription = {
     subscription: Subscription
     qr_code: string
}

// ✅ Resposta ao listar inscrições de um evento
export type ApiGetSubscriptions = {
     subscriptions: Subscription[]
}

// ✅ Resposta ao deletar inscrição
export type ApiDeleteSubscription = {
     message: string
}

