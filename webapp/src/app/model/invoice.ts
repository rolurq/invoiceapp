import { Client } from './client';

export class Invoice {
  id: number;
  name: string;
  issueDate: Date;
  client: Client;
}
