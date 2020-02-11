import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Invoice } from '../model/invoice';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class InvoiceService {

  constructor(private http: HttpClient) { }

  getInvoices() {
    return this.http.get<Invoice[]>(`${environment.apiHost}/api/v1/invoice/`);
  }
}
