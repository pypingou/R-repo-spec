%global packname  packClassic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Toy example of Pack Classic

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics 

BuildRequires:    R-devel tex(latex) R-graphics 

%description
This package comes to illustrate the book "Petit Manuel de Programmation
Orientee Objet sous R"

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
%doc %{rlibdir}/packClassic/html
%doc %{rlibdir}/packClassic/DESCRIPTION
%{rlibdir}/packClassic/INDEX
%{rlibdir}/packClassic/help
%{rlibdir}/packClassic/data
%{rlibdir}/packClassic/NAMESPACE
%{rlibdir}/packClassic/R
%{rlibdir}/packClassic/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora