%global packname  HGLMMM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Hierarchical Generalized Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Matrix R-numDeriv R-methods R-lattice 

BuildRequires:    R-devel tex(latex) R-Matrix R-numDeriv R-methods R-lattice 

%description
Hierarchical Generalized Linear Models

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
%doc %{rlibdir}/HGLMMM/html
%doc %{rlibdir}/HGLMMM/DESCRIPTION
%doc %{rlibdir}/HGLMMM/CITATION
%{rlibdir}/HGLMMM/data
%{rlibdir}/HGLMMM/R
%{rlibdir}/HGLMMM/NAMESPACE
%{rlibdir}/HGLMMM/INDEX
%{rlibdir}/HGLMMM/help
%{rlibdir}/HGLMMM/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora