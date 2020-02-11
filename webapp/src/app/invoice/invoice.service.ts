import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Invoice } from '../model/invoice';
import { environment } from 'src/environments/environment';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class InvoiceService {

  constructor(private http: HttpClient) { }

  getInvoices() {
    return this.http.get<any[]>(`${environment.apiHost}/api/v1/invoice/`).pipe(
      map(dataArr => dataArr.map(Invoice.fromJson))
    );
  }
}
