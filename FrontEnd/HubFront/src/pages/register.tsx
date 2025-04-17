import {Box, Button, Snackbar, TextField } from "@mui/material";
import { JSX, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../utils/api";
import CheckIcon from '@mui/icons-material/Check';
import { Helmet } from "react-helmet";

export const Register = () => {

     const [nome, setNome] = useState("");
     const [email, setEmail] = useState("");
     const [password, setPassword] = useState("");
     const [alert, setAlert] = useState<JSX.Element | null>(null);
     const navigate = useNavigate();

     const handleRegister = async (e: React.FormEvent) => {
          e.preventDefault();

          try{
               await api.post("/user/signup/",{
                    nome,
                    email,
                    password
               })
               setAlert(
                    
                    <Snackbar
                    message="Cadastro realizado com sucesso!"
                    open={true}
                    autoHideDuration={3000}
                    action={
                         <CheckIcon className="text-green-500" />
                    }
                    />
               );

               setTimeout(() => navigate("/"), 5000);

          }catch (error) {
               console.error("Erro ao cadastrar:", error);
               setAlert(
                    <Snackbar
                    message="Erro ao cadastrar, verifique suas credenciais."
                    open={true}
                    autoHideDuration={3000}
                    />
               )
          }

     }

     return(
          <>
               {alert && <div className="">{alert}</div>}
               <Helmet>
                    <title>Cadastro</title>
               </Helmet>
               <div className ="flex flex-col items-center justify-center bg-[#A6D6D6] h-screen w-full">
                    <h1 className="flex flex-col items-center text-[3.75rem] font-knewave pt-[6.25rem] mb-[6.25rem]" >HUBVENT CADASTRO</h1>
                    <Box className=" bg-[#6DE1D2] rounded-[1rem] p-4 h-[25rem] w-[30rem] flex items-center justify-center">
                         
                         <form onSubmit={handleRegister}
                         className="flex flex-col items-center justify-center gap-[1rem]">
                              <TextField
                                   label="Nome"
                                   variant="outlined"
                                   placeholder="Nome"
                                   value={nome}
                                   onChange={(e) => setNome(e.target.value)}
                                   className="w-[25rem]"
                              />
                              <TextField
                              label="Email"
                              variant="outlined"
                              placeholder="Email"
                              value={email}
                              onChange={(e) => setEmail(e.target.value)}
                              className="w-[25rem]"
                              />
                              <TextField
                              label="Senha"
                              variant="outlined"
                              type="password"
                              placeholder="Senha"
                              value={password}
                              onChange={(e) => setPassword(e.target.value)}
                              className="w-[25rem]"
                              />
                              <Button type="submit" variant="contained">Cadastrar</Button>
                         </form>

                    </Box>
               </div>
          </>
     )
}