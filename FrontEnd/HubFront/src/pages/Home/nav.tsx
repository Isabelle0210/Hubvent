import { useState } from "react";
import {
  Box,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from "@mui/material";
import AutoAwesomeMotionIcon from "@mui/icons-material/AutoAwesomeMotion";
import AutoStoriesIcon from "@mui/icons-material/AutoStories";
import { Publicar } from "./Pub";

type NavProps = {
  handleToggleDrawer: (open: boolean) => () => void;
};

export const Nav = ({ handleToggleDrawer }: NavProps) => {
  const [openDialog, setOpenDialog] = useState(false);

  const handleClickOpen = () => {
    setOpenDialog(true);
  };

  const handleClose = () => {
    setOpenDialog(false);
    handleToggleDrawer(false)();
  };

  return (
    <>
      <Box sx={{ width: 250 }} role="presentation">
        <List>
          <ListItem disablePadding>
            <ListItemButton onClick={handleClickOpen}>
              <ListItemIcon>
                <AutoAwesomeMotionIcon />
              </ListItemIcon>
              <ListItemText primary="Publicar" />
            </ListItemButton>
          </ListItem>

          <ListItem disablePadding>
            <ListItemButton>
              <ListItemIcon>
                <AutoStoriesIcon />
              </ListItemIcon>
              <ListItemText primary="Inscrições" />
            </ListItemButton>
          </ListItem>
        </List>
      </Box>

      <Publicar open={openDialog} onClose={handleClose} />
    </>
  );
};
