"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import {
  Fish,
  Search,
  MapPin,
  Bell,
  User,
  Star,
  Clock,
  Flame,
  Heart,
  ShoppingCart,
  Home,
  List,
  Plus,
} from "lucide-react"
import { useState } from "react"

interface Categoria {
  id: string
  nome: string
  icone: string
  cor: string
}

interface Prato {
  id: string
  nome: string
  descricao: string
  preco: number
  precoOriginal?: number
  imagem: string
  categoria: string
  avaliacao: number
  tempoEntrega: string
  isPromocao?: boolean
  isFavorito?: boolean
  isPopular?: boolean
}

export default function Component() {
  const [searchQuery, setSearchQuery] = useState("")
  const [categoriaAtiva, setCategoriaAtiva] = useState("todos")

  const categorias: Categoria[] = [
    { id: "todos", nome: "Todos", icone: "🍱", cor: "bg-red-100 text-red-700" },
    { id: "sushi", nome: "Sushi", icone: "🍣", cor: "bg-orange-100 text-orange-700" },
    { id: "sashimi", nome: "Sashimi", icone: "🐟", cor: "bg-blue-100 text-blue-700" },
    { id: "hot", nome: "Hot Rolls", icone: "🔥", cor: "bg-red-100 text-red-700" },
    { id: "temaki", nome: "Temaki", icone: "🌯", cor: "bg-green-100 text-green-700" },
    { id: "yakisoba", nome: "Yakisoba", icone: "🍜", cor: "bg-yellow-100 text-yellow-700" },
  ]

  const pratosDestaque: Prato[] = [
    {
      id: "1",
      nome: "Combo Salmão Premium",
      descricao: "10 peças de salmão fresco + 8 uramakis + 2 temakis",
      preco: 79.9,
      precoOriginal: 89.9,
      imagem: "/placeholder.svg?height=120&width=120",
      categoria: "sushi",
      avaliacao: 4.8,
      tempoEntrega: "25-35 min",
      isPromocao: true,
      isFavorito: false,
      isPopular: true,
    },
    {
      id: "2",
      nome: "Hot Philadelphia",
      descricao: "8 peças com salmão, cream cheese e cebolinha",
      preco: 32.9,
      imagem: "/placeholder.svg?height=120&width=120",
      categoria: "hot",
      avaliacao: 4.7,
      tempoEntrega: "20-30 min",
      isFavorito: true,
      isPopular: true,
    },
    {
      id: "3",
      nome: "Sashimi Variado",
      descricao: "12 fatias de peixes frescos selecionados",
      preco: 45.9,
      imagem: "/placeholder.svg?height=120&width=120",
      categoria: "sashimi",
      avaliacao: 4.9,
      tempoEntrega: "15-25 min",
      isFavorito: false,
    },
  ]

  const promocoes = [
    {
      id: "promo1",
      titulo: "Combo Família",
      subtitulo: "50 peças variadas",
      desconto: "30% OFF",
      preco: "R$ 129,90",
      imagem: "/placeholder.svg?height=100&width=200",
    },
    {
      id: "promo2",
      titulo: "Happy Hour",
      subtitulo: "Até 18h",
      desconto: "25% OFF",
      preco: "Em hot rolls",
      imagem: "/placeholder.svg?height=100&width=200",
    },
  ]

  const PratoCard = ({ prato }: { prato: Prato }) => (
    <Card className="hover:shadow-lg transition-all duration-200 cursor-pointer group">
      <CardContent className="p-0">
        <div className="relative">
          <img
            src={prato.imagem || "/placeholder.svg"}
            alt={prato.nome}
            className="w-full h-32 object-cover rounded-t-lg"
          />
          {prato.isPromocao && (
            <Badge className="absolute top-2 left-2 bg-red-600 text-white">
              <Flame className="w-3 h-3 mr-1" />
              Promoção
            </Badge>
          )}
          {prato.isPopular && (
            <Badge className="absolute top-2 right-2 bg-yellow-500 text-white">
              <Star className="w-3 h-3 mr-1" />
              Popular
            </Badge>
          )}
          <button className="absolute bottom-2 right-2 w-8 h-8 bg-white rounded-full shadow-md flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
            <Heart className={`w-4 h-4 ${prato.isFavorito ? "fill-red-500 text-red-500" : "text-gray-400"}`} />
          </button>
        </div>

        <div className="p-4">
          <h3 className="font-semibold text-gray-900 mb-1">{prato.nome}</h3>
          <p className="text-sm text-gray-600 mb-3 line-clamp-2">{prato.descricao}</p>

          <div className="flex items-center gap-2 mb-3">
            <div className="flex items-center">
              <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
              <span className="text-sm font-medium ml-1">{prato.avaliacao}</span>
            </div>
            <span className="text-gray-300">•</span>
            <div className="flex items-center text-sm text-gray-600">
              <Clock className="w-4 h-4 mr-1" />
              {prato.tempoEntrega}
            </div>
          </div>

          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              {prato.precoOriginal && (
                <span className="text-sm text-gray-400 line-through">
                  R$ {prato.precoOriginal.toFixed(2).replace(".", ",")}
                </span>
              )}
              <span className="text-lg font-bold text-red-600">R$ {prato.preco.toFixed(2).replace(".", ",")}</span>
            </div>
            <Button size="sm" className="bg-red-600 hover:bg-red-700">
              <Plus className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-red-600 rounded-full flex items-center justify-center">
                <Fish className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="text-lg font-bold text-gray-900">Olá, João! 👋</h1>
                <div className="flex items-center text-sm text-gray-600">
                  <MapPin className="w-4 h-4 mr-1" />
                  <span>Rua das Flores, 123</span>
                </div>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <Button variant="ghost" size="sm" className="relative">
                <Bell className="w-5 h-5" />
                <span className="absolute -top-1 -right-1 w-3 h-3 bg-red-500 rounded-full"></span>
              </Button>
              <Button variant="ghost" size="sm">
                <User className="w-5 h-5" />
              </Button>
            </div>
          </div>

          {/* Search Bar */}
          <div className="relative">
            <Search className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
            <Input
              placeholder="Buscar pratos, combos..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 h-12 border-gray-200 focus:border-red-500 focus:ring-red-500"
            />
          </div>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Promoções */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Ofertas Especiais 🔥</h2>
          <div className="flex gap-4 overflow-x-auto pb-2">
            {promocoes.map((promo) => (
              <Card
                key={promo.id}
                className="flex-shrink-0 w-80 bg-gradient-to-r from-red-500 to-red-600 text-white cursor-pointer hover:shadow-lg transition-shadow"
              >
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="font-bold text-lg">{promo.titulo}</h3>
                      <p className="text-red-100 mb-2">{promo.subtitulo}</p>
                      <Badge className="bg-white text-red-600 font-bold">{promo.desconto}</Badge>
                      <p className="text-sm mt-2">{promo.preco}</p>
                    </div>
                    <img
                      src={promo.imagem || "/placeholder.svg"}
                      alt={promo.titulo}
                      className="w-20 h-20 rounded-lg object-cover"
                    />
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Categorias */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Categorias</h2>
          <div className="flex gap-3 overflow-x-auto pb-2">
            {categorias.map((categoria) => (
              <button
                key={categoria.id}
                onClick={() => setCategoriaAtiva(categoria.id)}
                className={`flex-shrink-0 flex flex-col items-center p-3 rounded-xl transition-all ${
                  categoriaAtiva === categoria.id
                    ? "bg-red-600 text-white shadow-lg"
                    : "bg-white text-gray-700 hover:bg-gray-50"
                }`}
              >
                <span className="text-2xl mb-1">{categoria.icone}</span>
                <span className="text-sm font-medium whitespace-nowrap">{categoria.nome}</span>
              </button>
            ))}
          </div>
        </section>

        {/* Pratos em Destaque */}
        <section className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-bold text-gray-900">Pratos em Destaque</h2>
            <Button variant="ghost" className="text-red-600 hover:text-red-700">
              Ver todos
            </Button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {pratosDestaque.map((prato) => (
              <PratoCard key={prato.id} prato={prato} />
            ))}
          </div>
        </section>

        {/* Acesso Rápido */}
        <section className="mb-8">
          <h2 className="text-xl font-bold text-gray-900 mb-4">Acesso Rápido</h2>
          <div className="grid grid-cols-2 gap-4">
            <Card className="cursor-pointer hover:shadow-md transition-shadow">
              <CardContent className="p-4 text-center">
                <Clock className="w-8 h-8 text-red-600 mx-auto mb-2" />
                <h3 className="font-semibold text-gray-900">Últimos Pedidos</h3>
                <p className="text-sm text-gray-600">Repita seus favoritos</p>
              </CardContent>
            </Card>
            <Card className="cursor-pointer hover:shadow-md transition-shadow">
              <CardContent className="p-4 text-center">
                <Heart className="w-8 h-8 text-red-600 mx-auto mb-2" />
                <h3 className="font-semibold text-gray-900">Favoritos</h3>
                <p className="text-sm text-gray-600">Seus pratos preferidos</p>
              </CardContent>
            </Card>
          </div>
        </section>
      </div>

      {/* Bottom Navigation */}
      <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 px-4 py-2">
        <div className="max-w-4xl mx-auto">
          <div className="flex items-center justify-around">
            <button className="flex flex-col items-center p-2 text-red-600">
              <Home className="w-5 h-5" />
              <span className="text-xs mt-1">Home</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <Search className="w-5 h-5" />
              <span className="text-xs mt-1">Buscar</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <ShoppingCart className="w-5 h-5" />
              <span className="text-xs mt-1">Carrinho</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <List className="w-5 h-5" />
              <span className="text-xs mt-1">Pedidos</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <User className="w-5 h-5" />
              <span className="text-xs mt-1">Perfil</span>
            </button>
          </div>
        </div>
      </div>

      {/* Espaçamento para o bottom navigation */}
      <div className="h-20"></div>
    </div>
  )
}
