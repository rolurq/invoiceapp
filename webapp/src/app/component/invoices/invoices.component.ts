import { Component, OnInit, OnDestroy } from '@angular/core';
import { InvoiceService } from 'src/app/invoice/invoice.service';
import { Invoice } from 'src/app/model/invoice';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-invoices',
  templateUrl: './invoices.component.html',
  styleUrls: ['./invoices.component.scss']
})
export class InvoicesComponent implements OnInit, OnDestroy {
  displayedColumns: string[] = ['id', 'issueDate', 'client', 'pdf'];
  invoices: Invoice[];
  private subscription: Subscription;

  constructor(private invoiceService: InvoiceService, private authService: AuthService) { }

  ngOnInit(): void {
    this.subscription = this.invoiceService.getInvoices().subscribe(invoices => {
      this.invoices = invoices;
    });
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  getPdfUrl(invoice: Invoice): string {
    return `${environment.apiHost}/invoice_pdf/${this.authService.token}/${invoice.id}`;
  }

}
