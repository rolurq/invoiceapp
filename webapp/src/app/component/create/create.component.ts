import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { ClientService } from 'src/app/invoice/client.service';
import { Client } from 'src/app/model/client';
import { Subscription } from 'rxjs';
import { SelectionModel } from '@angular/cdk/collections';
import { ProductService } from 'src/app/invoice/product.service';
import { Product } from 'src/app/model/product';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit, OnDestroy {
  createForm: FormGroup;
  clients: Client[];
  products: Product[];
  selection = new SelectionModel(true);
  columnsToDisplay = ['select', 'name', 'price', 'amount'];
  private subClients: Subscription;
  private subProducts: Subscription;

  constructor(private formBuilder: FormBuilder, private clientService: ClientService, private productService: ProductService) {
    this.createForm = formBuilder.group({
      client: new FormControl('', [Validators.required]),
      terms: new FormControl('', [Validators.required]),
      tax: new FormControl('', [Validators.required]),
    });
  }

  ngOnInit(): void {
    this.subClients = this.clientService.getClients().subscribe(clients => { this.clients = clients; });
    this.subProducts = this.productService.getProducts().subscribe(products => { this.products = products; });
  }

  ngOnDestroy(): void {
    this.subClients.unsubscribe();
    this.subProducts.unsubscribe();
  }

  get terms() { return this.createForm.get('terms'); }

  get tax() { return this.createForm.get('tax'); }

  get client() { return this.createForm.get('client'); }

  onSubmit(data) {}

  /** Whether the number of selected elements matches the total number of rows. */
  isAllSelected() {
    const numSelected = this.selection.selected.length;
    const numRows = this.products.length;
    return numSelected === numRows;
  }

  /** Selects all rows if they are not all selected; otherwise clear selection. */
  masterToggle() {
    this.isAllSelected() ?
        this.selection.clear() :
        this.products.forEach(row => this.selection.select(row));
  }

}
