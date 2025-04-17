import { Button, Drawer } from "@mui/material"
import { Helmet } from "react-helmet"
import { Nav } from "./nav"
import { useState } from "react"
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
          <div className="bg-[#3C3D37] h-screen w-screen">
               <header className="w-screen h-[8rem] flex justify-between text-[2rem] bg-[#8C3061] p-[1rem]">
                    <Button onClick={handleToggleDrawer(true)} ><h1 className="text-[#000]">Menu</h1></Button>
                    <Drawer open={open} onClose={handleToggleDrawer(false)}>
                         {drawerList}
                    </Drawer>
                    <h1>Hubvent</h1>
                    <div></div>
               </header>
          </div>
          </>
     )
}