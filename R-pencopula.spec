%global packname  pencopula
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Flexible Copula Density Estimation with Penalized Hierarchical B-Splines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-fda R-quadprog R-spam 

BuildRequires:    R-devel tex(latex) R-lattice R-fda R-quadprog R-spam 

%description
Flexible copula density estimation with penalized hierarchical B-Splines.

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
%doc %{rlibdir}/pencopula/html
%doc %{rlibdir}/pencopula/DESCRIPTION
%{rlibdir}/pencopula/R
%{rlibdir}/pencopula/INDEX
%{rlibdir}/pencopula/NAMESPACE
%{rlibdir}/pencopula/help
%{rlibdir}/pencopula/Meta
%{rlibdir}/pencopula/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora