import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './component/login/login.component';
import { RegisterComponent } from './component/register/register.component';
import { AuthGuard } from './auth/auth.guard';
import { InvoicesComponent } from './component/invoices/invoices.component';
import { AccessGuard } from './auth/access.guard';


const routes: Routes = [
  { path: '', component: InvoicesComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent, canActivate: [AccessGuard] },
  { path: 'register', component: RegisterComponent, canActivate: [AccessGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
