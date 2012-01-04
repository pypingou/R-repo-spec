%global packname  orloca.es
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2
Release:          1%{?dist}
Summary:          Spanish version of orloca package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-orloca 

BuildRequires:    R-devel tex(latex) R-orloca 

%description
Version espanola del paquete orloca que trata de los modelos de
Localizacion en Investigacion Operativa (Operations Research LOCational
Analysis). En particular, el problema de encontrar el punto que minimiza
la suma ponderada de las distancias a un conjunto de puntos dados.

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
%doc %{rlibdir}/orloca.es/html
%doc %{rlibdir}/orloca.es/DESCRIPTION
%{rlibdir}/orloca.es/INDEX
%{rlibdir}/orloca.es/help
%{rlibdir}/orloca.es/Meta
%{rlibdir}/orloca.es/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2-1
- initial package for Fedora