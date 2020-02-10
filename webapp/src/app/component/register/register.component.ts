import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthService } from 'src/app/auth/auth.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;
  returnUrl: string;

  constructor(private authService: AuthService, private formBuilder: FormBuilder, private router: Router, private route: ActivatedRoute) {
    this.registerForm = this.formBuilder.group({
      username: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required, Validators.email]),
      firstName: new FormControl(''),
      lastName: new FormControl(''),
      password1: new FormControl('', [Validators.required]),
      password2: new FormControl('', [Validators.required]),
      phone: new FormControl('', [Validators.required, Validators.pattern('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$')]),
      website: new FormControl('', [Validators.required]),
      address: new FormControl('', [Validators.required]),
      city: new FormControl('', [Validators.required]),
      state: new FormControl('', [Validators.required]),
      country: new FormControl('', [Validators.required]),
      zipCode: new FormControl('', [Validators.required]),
    }, {
      validator: (group) => {
        return (group.get('password1').value === group.get('password2').value) ? null : { passwordMismatch: true };
      }
    });
  }

  get username() { return this.registerForm.get('username'); }

  get email() { return this.registerForm.get('email'); }

  get firstName() { return this.registerForm.get('firstName'); }

  get lastName() { return this.registerForm.get('lastName'); }

  get password1() { return this.registerForm.get('password1'); }

  get password2() { return this.registerForm.get('password2'); }

  get phone() { return this.registerForm.get('phone'); }

  get website() { return this.registerForm.get('website'); }

  get address() { return this.registerForm.get('address'); }

  get city() { return this.registerForm.get('city'); }

  get state() { return this.registerForm.get('state'); }

  get country() { return this.registerForm.get('country'); }

  get zipCode() { return this.registerForm.get('zipCode'); }

  ngOnInit(): void {
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  onSubmit(registerData) {
    this.authService.register(registerData).subscribe(
      () => this.router.navigate([this.returnUrl]),
    );
  }

}
