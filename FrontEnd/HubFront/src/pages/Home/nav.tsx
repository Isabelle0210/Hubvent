import { Box, List, ListItem, ListItemButton, ListItemIcon, ListItemText } from "@mui/material";
import AutoAwesomeMotionIcon from '@mui/icons-material/AutoAwesomeMotion';
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
type NavProps = {
     handleToggleDrawer: (open: boolean) => () => void;
}

export const Nav = ({handleToggleDrawer}: NavProps) => {


     return(
          <Box sx={{ width: 250 }} role="presentation" onClick={handleToggleDrawer(false)}>
               <List>
                    {['Publicar', 'Inscrições',].map((text, index) => (
                         <ListItem key={text} disablePadding>
                         <ListItemButton>
                              <ListItemIcon>
                              {index % 2 === 0 ? <AutoAwesomeMotionIcon /> : <AutoStoriesIcon />}
                              </ListItemIcon>
                         <ListItemText primary={text} />
                         </ListItemButton>
                         </ListItem>
                    ))}
               </List>
          </Box>
     );
}