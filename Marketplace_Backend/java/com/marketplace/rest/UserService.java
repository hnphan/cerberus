package com.marketplace.rest;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;

import com.marketplace.model.User;

@Stateless
@Path("/user")
public class UserService {

	@PersistenceContext(unitName="Marketplace_Backend")
	private EntityManager em;
	
	@POST
	@Path("/post/addUser")
	@Consumes("application/json")
	@Produces("application/json")
	public User addUser(User user){
		em.persist(user);
		return user;
	}
	
}
