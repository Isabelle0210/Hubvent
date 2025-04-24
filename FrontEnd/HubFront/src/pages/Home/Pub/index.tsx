import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from "@mui/material";

type PublicarProps = {
  open: boolean;
  onClose: () => void;
};

export const Publicar = ({ open, onClose }: PublicarProps) => {
  return (
    <Dialog open={open}>
      <DialogTitle>Publicar</DialogTitle>
      <DialogContent>
        <DialogContentText>
          Publicar eventos, notícias e muito mais.
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancelar</Button>
        <Button onClick={() => {}}>Publicar</Button>
      </DialogActions>
    </Dialog>
  );
};
