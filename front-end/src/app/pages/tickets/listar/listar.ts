import { Component, inject, signal } from '@angular/core';
import { TicketService } from '../../../services/ticket.service';
import { TicketResposta } from '../../../models/tickets.model';

@Component({
  selector: 'app-listar',
  imports: [],
  templateUrl: './listar.html',
  styleUrl: './listar.scss',
})
export class Listar {
  ticketService = inject(TicketService);

  tickets = signal<TicketResposta[]>([]);

  ngOnInit(){
    this.carregarTickets();
  }

  carregarTickets(){
    this.ticketService.listar().subscribe({
      next: (tickets) => this.tickets.set(tickets),
      error: (erro) => {
        console.error(erro)
        alert("Não foi possivel carregar os tickets");
      }
    })
  }
}