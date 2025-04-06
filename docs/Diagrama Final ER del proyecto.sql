CREATE TABLE `clean_product_category_name_translation` (
  `product_category_name` varchar(255),
  `product_category_name_english` varchar(255)
);

CREATE TABLE `clean_olist_sellers_dataset` (
  `seller_id` varchar(255) PRIMARY KEY,
  `seller_zip_code_prefix` int,
  `seller_state` varchar(255)
);

CREATE TABLE `clean_olist_geolocation_dataset` (
  `geolocation_zip_code_prefix` int,
  `geolocation_lat` float,
  `geolocation_lng` float,
  `geolocation_city` varchar(255),
  `geolocation_state` varchar(255)
);

CREATE TABLE `clean_olist_order_items_dataset` (
  `order_id` varchar(255),
  `order_item_id` int,
  `product_id` varchar(255),
  `seller_id` varchar(255),
  `shipping_limit_date` datetime,
  `price` float,
  `freight_value` float,
  `price_normalized` float
);

CREATE TABLE `clean_olist_order_payments_dataset` (
  `order_id` varchar(255),
  `payment_sequential` int,
  `payment_type` varchar(255),
  `payment_installments` int,
  `payment_value` float
);

CREATE TABLE `clean_olist_order_reviews_dataset` (
  `review_id` varchar(255) PRIMARY KEY,
  `order_id` varchar(255),
  `review_score` int,
  `review_comment_title` varchar(255),
  `review_comment_message` varchar(255),
  `review_creation_date` datetime,
  `review_answer_timestamp` datetime,
  `review_sentiment` varchar(255)
);

CREATE TABLE `enriched_olist_customers_dataset` (
  `customer_id` varchar(255) PRIMARY KEY,
  `customer_unique_id` varchar(255),
  `customer_zip_code_prefix` int,
  `customer_city` varchar(255),
  `customer_state` varchar(255),
  `min_purchase` float,
  `segment_id` int,
  `segment_name` varchar(255),
  `discount_rate` float
);

CREATE TABLE `enriched_olist_orders_dataset` (
  `order_id` varchar(255) PRIMARY KEY,
  `customer_id` varchar(255),
  `order_status` varchar(255),
  `order_purchase_timestamp` datetime,
  `order_approved_at` datetime,
  `order_delivered_carrier_date` datetime,
  `order_delivered_customer_date` datetime,
  `order_estimated_delivery_date` datetime,
  `weight_range` varchar(255),
  `base_rate` float,
  `express_rate` float
);

CREATE TABLE `enriched_olist_products_dataset` (
  `product_id` varchar(255) PRIMARY KEY,
  `product_category_name` varchar(255),
  `product_name_length` int,
  `product_description_length` int,
  `product_photos_qty` int,
  `product_weight_g` float,
  `product_length_cm` float,
  `product_height_cm` float,
  `product_width_cm` float,
  `category_name` varchar(255),
  `tax_rate` float
);

ALTER TABLE `clean_olist_order_items_dataset` ADD FOREIGN KEY (`order_id`) REFERENCES `enriched_olist_orders_dataset` (`order_id`);

ALTER TABLE `clean_olist_order_items_dataset` ADD FOREIGN KEY (`product_id`) REFERENCES `enriched_olist_products_dataset` (`product_id`);

ALTER TABLE `clean_olist_order_items_dataset` ADD FOREIGN KEY (`seller_id`) REFERENCES `clean_olist_sellers_dataset` (`seller_id`);

ALTER TABLE `clean_olist_order_payments_dataset` ADD FOREIGN KEY (`order_id`) REFERENCES `enriched_olist_orders_dataset` (`order_id`);

ALTER TABLE `clean_olist_order_reviews_dataset` ADD FOREIGN KEY (`order_id`) REFERENCES `enriched_olist_orders_dataset` (`order_id`);

ALTER TABLE `enriched_olist_orders_dataset` ADD FOREIGN KEY (`customer_id`) REFERENCES `enriched_olist_customers_dataset` (`customer_id`);

ALTER TABLE `enriched_olist_products_dataset` ADD FOREIGN KEY (`product_category_name`) REFERENCES `clean_product_category_name_translation` (`product_category_name`);

ALTER TABLE `clean_olist_sellers_dataset` ADD FOREIGN KEY (`seller_zip_code_prefix`) REFERENCES `clean_olist_geolocation_dataset` (`geolocation_zip_code_prefix`);

ALTER TABLE `enriched_olist_customers_dataset` ADD FOREIGN KEY (`customer_zip_code_prefix`) REFERENCES `clean_olist_geolocation_dataset` (`geolocation_zip_code_prefix`);
