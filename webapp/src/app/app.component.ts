import { Component } from '@angular/core';
import { AuthService } from './auth/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'invoiceapp';

  constructor(private authService: AuthService, private router: Router) {}

  get isAuthenticated(): boolean { return this.authService.isAuthenticated; }

  logout() {
    this.authService.logout().subscribe(() => {
      this.router.navigate(['/login'], { queryParams: { returnUrl: '/' } });
    });
  }
}
