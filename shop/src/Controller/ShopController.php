<?php

namespace App\Controller;

use App\Entity\Shop;
use App\Repository\ShopRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Uid\Uuid;

/**
 * @Route("/api/shops", name="shop_api")
 */
class ShopController extends AbstractController
{
    // placeholder until data sync is implemented
    private Uuid $defaultOwnerId;

    public function __construct()
    {
        $this->defaultOwnerId = Uuid::fromString('d9e7a184-5d5b-11ea-a62a-3499710062d0');
    }

    /**
     * @Route("/", name="all", methods={"GET"})
     */
    public function getAll(ShopRepository $shopRepository, SerializerInterface $serializer): Response
    {
        $shops = $shopRepository->findAll();
        $data = $serializer->serialize($shops, 'json');

        return new Response($data, 200, ['Content-Type' => 'application/json']);
    }


    /**
     * @Route("/{id}", name="one", methods={"GET"})
     */
    public function get(ShopRepository $shopRepository, Uuid $id, SerializerInterface $serializer): Response
    {
        $shop = $shopRepository->findById($id);

        if (!$shop) {
            return new JsonResponse(['error' => 'Shop not found'], 404);
        }

        $data = $serializer->serialize($shop, 'json');

        return new Response($data, 200, ['Content-Type' => 'application/json']);
    }


    /**
     * @Route("/", name="create", methods={"POST"})
     */
    public function create(Request $request, EntityManagerInterface $entityManager, SerializerInterface $serializer): Response
    {
        $requestData = $request->getContent();

        $shop = $serializer->deserialize($requestData, Shop::class, 'json');

        $shop->setOwnerId($this->defaultOwnerId);
        if (!$shop->getName() || !$shop->getOwnerId()) {
            return new JsonResponse(['error' => 'Missing required fields'], 400);
        }

        $entityManager->persist($shop);
        $entityManager->flush();

        $data = $serializer->serialize($shop, 'json');

        return new JsonResponse(['message' => 'Shop created!', 'shop' => json_decode($data)], 201);
    }


    /**
     * @Route("/{id}", name="update", methods={"PUT"})
     */
    public function update(Shop $shop, Request $request, EntityManagerInterface $entityManager, SerializerInterface $serializer): Response
    {
        $requestData = $request->getContent();
        $updatedShop = $serializer->deserialize($requestData, Shop::class, 'json');

        $shop->setName($updatedShop->getName());
        $shop->setDescription($updatedShop->getDescription());
        $shop->setOwnerId($this->defaultOwnerId);

        $entityManager->flush();

        return new Response('Shop updated!', 200);
    }


    /**
     * @Route("/{id}", name="delete", methods={"DELETE"})
     */
    public function delete(Shop $shop, EntityManagerInterface $entityManager): Response
    {
        $entityManager->remove($shop);
        $entityManager->flush();

        return new Response('Shop deleted!', 200);
    }
}
