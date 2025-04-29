describe('Pruebas API con Cypress', () => {
    it('Obtiene una lista de usuarios', () => {
      cy.request('GET', 'https://reqres.in/api/users?page=2').then((response) => {
        expect(response.status).to.eq(200); // Verifica que la respuesta es 200 OK
        expect(response.body).to.have.property('data'); // Verifica que la respuesta tiene datos
        expect(response.body.data).to.be.an('array'); // Verifica que los datos son un array
      });
    });
  
    it('Crea un nuevo usuario', () => {
      cy.request('POST', 'https://reqres.in/api/users', {
        name: 'Luciano',
        job: 'Tester',
      }).then((response) => {
        expect(response.status).to.eq(201); // Código de estado 201 (creado)
        expect(response.body).to.have.property('name', 'Luciano');
        expect(response.body).to.have.property('job', 'Tester');
      });
    });
  });
  