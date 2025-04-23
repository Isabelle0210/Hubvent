import { Button, Drawer } from "@mui/material"
import { Helmet } from "react-helmet"
import { Nav } from "./nav"
import { useState } from "react"
import { Feed } from "./Feed"
import AddToPhotosIcon from '@mui/icons-material/AddToPhotos';

export const Home = () => {
     const [open, setOpen] = useState(false)
     
     const handleToggleDrawer = (open: boolean) => () => {
          setOpen(open)
     }

     const drawerList = (
          <Nav handleToggleDrawer={handleToggleDrawer} />
     )

     return (
     

          <>
          <Helmet>Home</Helmet>
          <div className="bg-[#F6F8D5] h-full w-screen">
               <header className="w-screen h-[4rem] flex justify-between text-4xl bg-[#98D2C0] ">
                    <Button onClick={handleToggleDrawer(true)} >
                         <AddToPhotosIcon fontSize="large" className="bg-black"/>
                    </Button>
                    <Drawer open={open} onClose={handleToggleDrawer(false)}>
                         {drawerList}
                    </Drawer>
                    <h1 className="mt-2">Hubvent</h1>
                    <div></div>
               </header>
               <section className="flex flex-col items-center justify-center list-style-none">
                    <Feed />
               </section>
               <footer className="w-screen h-20 bg-[#98D2C0] flex justify-center items-center mt-4">
                    <p className="text-2xl">Direitos Reservados</p>
               </footer>
          </div>
          </>
     )
}