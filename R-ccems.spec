%global packname  ccems
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Combinatorially Complex Equilibrium Model Selection

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-odesolve R-snow R-PolynomF 


BuildRequires:    R-devel tex(latex) R-odesolve R-snow R-PolynomF



%description
Dissociation constants of quasi-equilibriums of enzymes and protein-ligand
binding equilibriums in general are systematically scanned though
possibilities of being infinity and/or equal to others. The automatically
generated space of models is then fitted to data.

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
%doc %{rlibdir}/ccems/doc
%doc %{rlibdir}/ccems/DESCRIPTION
%doc %{rlibdir}/ccems/html
%{rlibdir}/ccems/INDEX
%{rlibdir}/ccems/Meta
%{rlibdir}/ccems/NAMESPACE
%{rlibdir}/ccems/R
%{rlibdir}/ccems/data
%{rlibdir}/ccems/papers
%{rlibdir}/ccems/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora