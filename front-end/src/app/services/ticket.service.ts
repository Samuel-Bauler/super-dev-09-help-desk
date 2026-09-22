import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { TicketResposta } from '../models/tickets.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TicketService {
  private http = inject(HttpClient);

  private baseUrl = `http://localhost:8001/tickets`

  listar(): Observable<TicketResposta[]>{
    return this.http.get<TicketResposta[]>(this.baseUrl);
  }
}
