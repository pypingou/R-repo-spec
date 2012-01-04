%global packname  SPECIES
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Statistical package for species richness estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
SPECIES is an R package for estimation of species richness or diversity.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/SPECIES/DESCRIPTION
%doc %{rlibdir}/SPECIES/CITATION
%doc %{rlibdir}/SPECIES/html
%{rlibdir}/SPECIES/R
%{rlibdir}/SPECIES/help
%{rlibdir}/SPECIES/INDEX
%{rlibdir}/SPECIES/data
%{rlibdir}/SPECIES/libs
%{rlibdir}/SPECIES/NAMESPACE
%{rlibdir}/SPECIES/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora