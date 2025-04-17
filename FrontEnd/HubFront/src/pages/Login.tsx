import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Button, TextField } from "@mui/material";
import api from "../utils/api";
import { Helmet } from "react-helmet";

const Login = () => {

const [email, setEmail] = useState("");
const [password, setPassword] = useState("");


const navigate = useNavigate();

const handleLogin = async (e) => {
     e.preventDefault();

     try{
          const response = await api.post("/user/signin/",{ 
               email,
               password
          })

          const token = response.data.access;

          localStorage.setItem("token", token);
          navigate ("/home");

          console.log("Login bem-sucedido:", response.data);
          console.log("Token:", token);
     }catch (error) {
          alert("Erro ao fazer login, verifique suas credenciais.");
          console.error("Erro ao fazer login:", error);
     }
}
     return(
          <>
          <Helmet>
               <title>Login</title>
          </Helmet>
               <div className=" 
               flex 
               flex-col 
               items-center 
               justify-center 
               bg-[#A6D6D6] 
               h-screen 
               w-full
               ">
                    <h1 className="flex flex-col items-center text-[3.75rem] font-knewave mb-[6.25rem]" >HUBVENT</h1>
                    <Box className="flex flex-col items-center justify-center h-[25rem] w-[25rem] bg-[#6DE1D2] rounded-[1rem] p-4">
                         <form onSubmit={handleLogin}
                         className="flex flex-col items-center justify-center gap-[1rem]"
                         >
                              <TextField
                                   type="email"
                                   variant="outlined"
                                   placeholder="Email"
                                   value={email}
                                   onChange={(e) => setEmail(e.target.value)}
                                   required
                              />
                              <TextField
                                   variant="outlined"
                                   type="password"
                                   placeholder="Senha"
                                   value={password}
                                   onChange={(e) => setPassword(e.target.value)}
                                   required
                              />
                              <Button type="submit" variant="contained">Entrar</Button>
                         </form>
                         <p>Não tem uma conta? <a href="/register">Registrar</a></p>
                    </Box>
               </div>
          </>
     );
}

export default Login;