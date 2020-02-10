import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';

import { User } from '../model/user';
import { Token } from '../model/token';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authenticated = false;
  private userProfile: User;
  private accessToken: string;

  constructor(private http: HttpClient) {
    const key = localStorage.getItem('auth_token');
    if (key) {
      this.loadKey(key);
    }
  }

  login(username: string, password: string) {
    return this.http.post<Token>(`${environment.apiHost}/api/v1/auth/login/`, {
      username,
      password
    }).pipe( tap(token => { this.loadKey(token.key); }) );
  }

  register(data: User) {
    const { firstName, lastName, zipCode, ...otherFields } = data;

    return this.http.post<Token>(`${environment.apiHost}/api/v1/auth/registration/`, {
      ...otherFields,
      first_name: firstName,
      last_name: lastName,
      zip_code: zipCode,
    }).pipe( tap(token => { this.loadKey(token.key); this.userProfile = data; })
    );
  }

  logout() {
    return this.http.post(`${environment.apiHost}/api/v1/auth/logout/`, {}).pipe(
      tap(() => {
        this.accessToken = null;
        this.authenticated = false;
        localStorage.removeItem('auth-token');
      })
    );
  }

  get isAuthenticated(): boolean {
    return this.authenticated;
  }

  get token(): string {
    return this.accessToken;
  }

  get user(): User {
    return this.userProfile;
  }

  private loadKey(key: string) {
    this.accessToken = key;
    this.authenticated = true;
    localStorage.setItem('auth_token', key);
  }
}
