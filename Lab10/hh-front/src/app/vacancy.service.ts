
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = 'http://127.0.0.1:8000/api/vacancies/';

  constructor(private http: HttpClient) { }

  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.apiUrl);
  }

  // Add other methods as needed
}

// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { Observable } from 'rxjs';
// import { Company } from './company';

// @Injectable({
//   providedIn: 'root'
// })
// export class DataService {

//   constructor(private http: HttpClient) { }

//   getCompanies(): Observable<Company[]> {
//     return this.http.get<Company[]>('api/companies');
//   }

//   getVacancies(companyId: number): Observable<Vacancy[]> {
//     return this.http.get<Vacancy[]>(`api/companies/${companyId}/vacancies`);
//   }
// }
