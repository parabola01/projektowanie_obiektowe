package com.example.zadanie9

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ProductListActivity : AppCompatActivity() {
    private lateinit var recyclerView: RecyclerView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_product_list)

        val categoryId = intent.getIntExtra("categoryId", -1)
        val products = DataProvider.getProductsForCategory(categoryId)

        recyclerView = findViewById(R.id.recyclerViewProducts)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = ProductAdapter(products)
    }
}
