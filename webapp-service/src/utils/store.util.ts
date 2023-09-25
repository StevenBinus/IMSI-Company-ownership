import { MenuRequestProps } from '@components/api/getMenu.api'
import { persist, createJSONStorage } from 'zustand/middleware'
import { create } from 'zustand'

export interface UserStore {
	company: number
	menu: MenuRequestProps[]
	module: string
	seed: number
}

const updateMenu = (
	userStore: UserStore,
	menu: MenuRequestProps[]
): UserStore => {
	userStore.menu = menu
	return userStore
}

const updateCompany = (userStore: UserStore, company: number): UserStore => {
	userStore.company = company
	return userStore
}
const updateModule = (userStore: UserStore, module: string): UserStore => {
	userStore.module = module
	return userStore
}

const updateSeed = (userStore: UserStore): UserStore => {
	userStore.seed = Math.random()
	return userStore
}

type Store = {
	userStore: UserStore
	updateUserMenu: (menu: MenuRequestProps[]) => void
	updateUserCompany: (company: number) => void
	updateUserModule: (module: string) => void
	updateUserSeed: () => void
}

const useUserStore = create(
	persist<Store>(
		(set, get): Store => ({
			userStore: {
				company: 0,
				menu: [],
				module: '',
				seed: 0,
			},
			updateUserMenu: (menu: MenuRequestProps[]) =>
				set((state) => ({
					...state,
					userStore: updateMenu(state.userStore, menu),
				})),
			updateUserCompany: (company: number) =>
				set((state) => ({
					...state,
					userStore: updateCompany(state.userStore, company),
				})),
			updateUserModule: (module: string) =>
				set((state) => ({
					...state,
					userStore: updateModule(state.userStore, module),
				})),
			updateUserSeed: () =>
				set((state) => ({
					...state,
					userStore: updateSeed(state.userStore),
				})),
		}),
		{
			name: 'user-storage', // name of the item in the storage (must be unique)
			storage: createJSONStorage(() => localStorage), // (optional) by default, 'localStorage' is used
		}
	)
)

export default useUserStore
