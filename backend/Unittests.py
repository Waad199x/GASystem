from src.api import app
from src.database.models import setup_db, Group
import unittest
import json
from flask_sqlalchemy import SQLAlchemy


class GroupsTestCase(unittest.TestCase):
    """This class represents the groups test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "GROUPS_test"
        self.database_path = "postgresql://{}/{}".format('postgres:W3DoOoNHM@localhost:5432', self.database_name)
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    edited_group = {
            'id': 4,
            'title': "T. Waad",
            'recipe': [{"name": "Norah", "color": "Noni@gmail.com", "parts": 541545584}]
        }
    new_group = {
            'title': "T. Mei",
            'recipe': [{"name": "Sara", "color": "Sara@gmail.com", "parts": 541251258}]
        }    
    def tearDown(self):
        """Executed after each test"""
        pass


# Getting Short Groups Info Endpoint

    # Test for SUCCESSFUL request  
        
    def test_get_groups_names(self):
        res = self.client().get('/Groups')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['drinks'])
    
    # Test for FAILED request  

    def test_failed_get_groups_names(self):
        res = self.client().get('/drinkss')# wrong link
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)

# Getting Detailed Groups Info Endpoint

    # Test for SUCCESSFUL request 
        
    def test_get_groups_infos(self):
        res = self.client().get('/Groups-Details', headers =
        {'Authorization':"bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1IeVdzQktLX1R3X2pqWHFOZy1yRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXNob3AtcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwOTViNzIzNTgyYmMwMDY5NDdkOTlkIiwiYXVkIjoiQ2Fwc3RvbmUtV2Vic2l0ZSIsImlhdCI6MTYzMjMxOTMwNiwiZXhwIjoxNjMyNDA1NzA2LCJhenAiOiI5U0tvd20wR0g2V3d2d3dNRFcyVVBBT1JoRHB3ZnJWQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmdyb3VwIiwiZ2V0Omdyb3VwcyIsImdldDpncm91cHMtZGV0YWlscyIsInBhdGNoOmdyb3VwcyIsInBvc3Q6Z3JvdXAiXX0.oXvdJoSd9b-d8YR23J0nDDpj6Z56CJ7gH50krpxdDtJcUSmb25KfXjguTU-6KlYKlMPADNOVcYdOKH11n5w5AwiGAFSPkltYaEgkvkh6ihExBIcrxx7kT_pawQKUK2j15_l7Vn3fXXPELSNce56KLrhyG12j3XdtL7a2v-e0ftO0R2IHu2zzAjsPzl8JoHB9-zLVUVG_-UzcyvwN1vAjavF6R0ICsMVxc6nrM0vleKc5GZvjhQ9X40NaIKMGFPqHNln6vgCinD_v0R2kpXoWIIDc1nTiDD9cAYYy4k-INJWhGSN1-TOH0g2rtuaCid0zkgzwez3k2N2HB1lW_s2xdw"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['drinks'])

    # Test for FAILED request  

    def test_failed_get_groups_infos(self):
        res = self.client().get('/Groups-Details', headers =
        {'Authorization':"bearer Invalid.Token"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['description'], "Permissions is not found in the payload.")  


# Posting New Group Endpoint

    # Test for SUCCESSFUL posting request

    def test_create_new_Quuestion(self):
        res = self.client().post('/Post-Group', headers =
        {'Authorization':"bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1IeVdzQktLX1R3X2pqWHFOZy1yRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXNob3AtcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwOTViNzIzNTgyYmMwMDY5NDdkOTlkIiwiYXVkIjoiQ2Fwc3RvbmUtV2Vic2l0ZSIsImlhdCI6MTYzMjMxOTMwNiwiZXhwIjoxNjMyNDA1NzA2LCJhenAiOiI5U0tvd20wR0g2V3d2d3dNRFcyVVBBT1JoRHB3ZnJWQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmdyb3VwIiwiZ2V0Omdyb3VwcyIsImdldDpncm91cHMtZGV0YWlscyIsInBhdGNoOmdyb3VwcyIsInBvc3Q6Z3JvdXAiXX0.oXvdJoSd9b-d8YR23J0nDDpj6Z56CJ7gH50krpxdDtJcUSmb25KfXjguTU-6KlYKlMPADNOVcYdOKH11n5w5AwiGAFSPkltYaEgkvkh6ihExBIcrxx7kT_pawQKUK2j15_l7Vn3fXXPELSNce56KLrhyG12j3XdtL7a2v-e0ftO0R2IHu2zzAjsPzl8JoHB9-zLVUVG_-UzcyvwN1vAjavF6R0ICsMVxc6nrM0vleKc5GZvjhQ9X40NaIKMGFPqHNln6vgCinD_v0R2kpXoWIIDc1nTiDD9cAYYy4k-INJWhGSN1-TOH0g2rtuaCid0zkgzwez3k2N2HB1lW_s2xdw"},json=self.new_group)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['drinks'])

    # Test for failed posting request 

    def test_failed_create_new_Quuestion(self):
        res = self.client().post('/Post-Group', headers =
        {'Authorization':"bearer Invalid.Token"},json=self.new_group)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['description'], "Permissions is not found in the payload.")  


# Patch Group Infos Endpoint

    # Test for SUCCESSFUL patch request

    def test_update_groups_info(self):
        res = self.client().patch('/Edit-Group/2', headers =
        {'Authorization':"bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1IeVdzQktLX1R3X2pqWHFOZy1yRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXNob3AtcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwOTViNzIzNTgyYmMwMDY5NDdkOTlkIiwiYXVkIjoiQ2Fwc3RvbmUtV2Vic2l0ZSIsImlhdCI6MTYzMjMxOTMwNiwiZXhwIjoxNjMyNDA1NzA2LCJhenAiOiI5U0tvd20wR0g2V3d2d3dNRFcyVVBBT1JoRHB3ZnJWQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmdyb3VwIiwiZ2V0Omdyb3VwcyIsImdldDpncm91cHMtZGV0YWlscyIsInBhdGNoOmdyb3VwcyIsInBvc3Q6Z3JvdXAiXX0.oXvdJoSd9b-d8YR23J0nDDpj6Z56CJ7gH50krpxdDtJcUSmb25KfXjguTU-6KlYKlMPADNOVcYdOKH11n5w5AwiGAFSPkltYaEgkvkh6ihExBIcrxx7kT_pawQKUK2j15_l7Vn3fXXPELSNce56KLrhyG12j3XdtL7a2v-e0ftO0R2IHu2zzAjsPzl8JoHB9-zLVUVG_-UzcyvwN1vAjavF6R0ICsMVxc6nrM0vleKc5GZvjhQ9X40NaIKMGFPqHNln6vgCinD_v0R2kpXoWIIDc1nTiDD9cAYYy4k-INJWhGSN1-TOH0g2rtuaCid0zkgzwez3k2N2HB1lW_s2xdw"},json=self.edited_group)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['drinks'])  
    
    # Test for FAILED patch request

    def test_failed_update_groups_info(self):
        res = self.client().patch('/Edit-Group/2', headers =
        {'Authorization':"bearer Invalid.Token"},json=self.edited_group)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['description'], "Permissions is not found in the payload.")       
    

# Delete Group Endpoint

    # Test for SUCCESSFUL delete request

    def test_delete_group(self):
        res = self.client().delete('/Delete-Group/1', headers =
        {'Authorization':"bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1IeVdzQktLX1R3X2pqWHFOZy1yRyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXNob3AtcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEwOTViNzIzNTgyYmMwMDY5NDdkOTlkIiwiYXVkIjoiQ2Fwc3RvbmUtV2Vic2l0ZSIsImlhdCI6MTYzMjMxOTMwNiwiZXhwIjoxNjMyNDA1NzA2LCJhenAiOiI5U0tvd20wR0g2V3d2d3dNRFcyVVBBT1JoRHB3ZnJWQiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmdyb3VwIiwiZ2V0Omdyb3VwcyIsImdldDpncm91cHMtZGV0YWlscyIsInBhdGNoOmdyb3VwcyIsInBvc3Q6Z3JvdXAiXX0.oXvdJoSd9b-d8YR23J0nDDpj6Z56CJ7gH50krpxdDtJcUSmb25KfXjguTU-6KlYKlMPADNOVcYdOKH11n5w5AwiGAFSPkltYaEgkvkh6ihExBIcrxx7kT_pawQKUK2j15_l7Vn3fXXPELSNce56KLrhyG12j3XdtL7a2v-e0ftO0R2IHu2zzAjsPzl8JoHB9-zLVUVG_-UzcyvwN1vAjavF6R0ICsMVxc6nrM0vleKc5GZvjhQ9X40NaIKMGFPqHNln6vgCinD_v0R2kpXoWIIDc1nTiDD9cAYYy4k-INJWhGSN1-TOH0g2rtuaCid0zkgzwez3k2N2HB1lW_s2xdw"})
        data = json.loads(res.data)

        group = Group.query.filter(Group.id == 1)
        group.delete()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['delete'],1)

    # Test for FAILED delete request

    def test_failed_delete_group(self):
        res = self.client().delete('/Delete-Group/1', headers =
        {'Authorization':"bearer Invalid.Token"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['description'], "Permissions is not found in the payload.")        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()