package com.shopfeed.kafka;

import com.shopfeed.user.User;

public class UserMutationEvent {

    private String eventType;
    private User user;

    public UserMutationEvent(EventType eventType, User user) {
        this.eventType = eventType.name();
        this.user = user;
    }

    public void setEventType(EventType eventType) {
        this.eventType = eventType.name();
    }

    public String getEventType() {
        return this.eventType;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public User getUser() {
        return this.user;
    }
}
