%global packname  ecespa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.04
Release:          1%{?dist}
Summary:          Functions for spatial point pattern analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-04.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splancs R-spatstat R-fields R-akima 

BuildRequires:    R-devel tex(latex) R-splancs R-spatstat R-fields R-akima 

%description
Some wrappers, functions and data sets for for spatial point pattern
analysis (mainly based on spatstat), used in the book "Introduccion al
Analisis Espacial de Datos en Ecologia y Ciencias Ambientales: Metodos y

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
%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.04-1
- initial package for Fedora