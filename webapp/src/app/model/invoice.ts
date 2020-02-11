export class Invoice {
  constructor(public id: number, public issueDate: Date, public client: string) {}

  static fromJson(data): Invoice {
    return new Invoice(data.id, data.issue_date, data.client);
  }
}
