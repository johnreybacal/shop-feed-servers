package com.shopfeed.kafka;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;

@Component
public class MessageProducer {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    public void sendUserMutationMessage(UserMutationEvent event) {
        ObjectWriter ow = new ObjectMapper().writer().withDefaultPrettyPrinter();

        try {
            String json = ow.writeValueAsString(event);

            kafkaTemplate.send("user-mutation", json);
        } catch (JsonProcessingException e) {
            System.out.println(e);
        } catch (Exception e) {
            System.out.println("Unhandled exception");
            System.out.println(e);
        }
    }

}
