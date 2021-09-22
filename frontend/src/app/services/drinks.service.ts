import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

export interface Drink {
  id: number;
  title: string;
  recipe: Array<{
          name: string,
          color: string,
          parts: number
        }>;
}

@Injectable({
  providedIn: 'root'
})
export class DrinksService {

  url = environment.apiServerUrl;

  public items: {[key: number]: Drink} = {};


  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getDrinks() {
    if (this.auth.can('get:groups-details')) {
      this.http.get(this.url + '/Groups-Details', this.getHeaders())
      .subscribe((res: any) => {
        this.drinksToItems(res.drinks);
        console.log(res);
      });
    } else {
      this.http.get(this.url + '/Groups', this.getHeaders())
      .subscribe((res: any) => {
        this.drinksToItems(res.drinks);
        console.log(res);
      });
    }

  }

  saveDrink(drink: Drink) {
    if (drink.id >= 0) { // patch
      this.http.patch(this.url + '/Edit-Group/' + drink.id, drink, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.drinksToItems(res.drinks);
        }
      });
    } else { // insert
      this.http.post(this.url + '/Post-Group', drink, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.drinksToItems(res.drinks);
        }
      });
    }

  }

  deleteDrink(drink: Drink) {
    delete this.items[drink.id];
    this.http.delete(this.url + '/Delete-Group/' + drink.id, this.getHeaders())
    .subscribe( (res: any) => {

    });
  }

  drinksToItems( drinks: Array<Drink>) {
    for (const drink of drinks) {
      this.items[drink.id] = drink;
    }
  }
}
