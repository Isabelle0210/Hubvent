import axios from "axios";
import { useEffect, useState } from "react";
import { ApiGetEvent, Event } from "../../../models/Event";
import { Button, Container } from "@mui/material";

export const Feed = () => {
     const [events, setEvents] = useState<Event[]>([]);
     const [subscriptions, setSubscriptions] = useState<number[]>([]);

          const subscribeToEvent = async (eventId: number) => {
               try{
                    const response = await axios.post(`http://127.0.0.1:8000/events/${eventId}/subscription/`, {
                         event_id: eventId
                    }, {
                         headers: {
                              Authorization: `Bearer ${localStorage.getItem("token")}`
                         }
                    })
                    console.log("Inscrição realizada com sucesso:", response.data);
                    setSubscriptions((prev) => [...prev, eventId]);
               
               }catch(error){
                    console.error("Erro ao se inscrever no evento:", error);
               }
          }
     useEffect(() => {
          const fetchEvents = async () => {
               try{
                    const response = await axios.get<ApiGetEvent>("http://127.0.0.1:8000/events/", {
                         headers: {
                              Authorization: `Bearer ${localStorage.getItem("token")}`
                         }
                    })
                    console.log("Pre-setEvent:", response.data);
                    setEvents(response.data.events || []);
                    
               }catch(error){
                    console.error("Erro ao buscar eventos:", error);
               }
          }
          fetchEvents();
     },[])
     return(
          <>
               <Container className="flex flex-col gap-7">
                    <h1 className="text-4xl m-5 text-cyan-900">Eventos</h1>
                         {
                              events.length === 0 ? (
                                   <p>Nenhum evento encontrado</p>
                              ) : (
                                   <ul className="flex flex-col gap-4">
                                        {events.map((event) => (
                                        <li key={event.id} className="flex flex-col gap-2 bg-[#98D2C0] p-4 rounded-lg shadow-lg">
                                             <h2 className="text-3xl text-center font-bold">{event.title}</h2>
                                             <p className="font-normal text-lg">{event.description}</p>
                                             <p className="text-sm">{event.date}</p>
                                             <p className="text-sm">{event.created_at}</p>
                                             <p>{event.created_by?.name}</p>
                                             <Button variant="contained" onClick={() => subscribeToEvent(Number(event.id))}
                                                  disabled={subscriptions.includes(Number(event.id))}

                                                  >{subscriptions.includes(Number(event.id)) ? "Inscrito" : "Inscrever-se"}</Button>
                                        </li>
                                        ))}
                                   </ul>
                              )
                         }
               </Container>
          </>
     );
}