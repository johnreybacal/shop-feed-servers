package com.shopfeed.user;

import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public Iterable<User> getAll() {
        return userRepository.findAll();
    }

    @GetMapping(path = "/{id}")
    public User get(@PathVariable(value = "id") UUID id) {
        return getUser(id);
    }

    @PostMapping
    public User create(@RequestBody User user) {
        return userRepository.save(user);
    }

    @PutMapping(path = "/{id}")
    public User update(@PathVariable UUID id, @RequestBody User updatedUser) {
        User user = getUser(id);
        user.setName(updatedUser.getName());
        user.setEmail(updatedUser.getEmail());

        return userRepository.save(user);
    }

    @DeleteMapping(path = "/{id}")
    public String Delete(@PathVariable UUID id) {
        User user = getUser(id);
        userRepository.delete(user);

        return "User has been deleted";
    }

    private User getUser(UUID id) {
        return userRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Unable to find user with id: " + id.toString()));
    }

}
