import { User } from "./Auth";

export type Event = { // esse é o que eu envio para a api
     id : string;
     title: string;
     description: string;
     date: string;
     created_at: string;
     created_by: User; //quem criou o evento
}

export type ApiGetEvent = { // esse é o que eu recebo da api
     event: Event[];
}

export type CreateEventRequest = { // esse é o que eu envio para a api
     title: string;
     description: string;
     date: string;
}
export type UpdateEventRequest = { // esse é o que eu envio para a api
     title?: string;
     description?: string;
     date?: string;
}






