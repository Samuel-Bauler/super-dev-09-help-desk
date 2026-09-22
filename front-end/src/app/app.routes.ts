import { Routes } from '@angular/router';

export const routes: Routes = [
    {path: "tickets", loadComponent: () => import("./pages/tickets/listar/listar").then(m => m.Listar)}
];
